"""100 SKU 专属 SVG 生成器
- 每张图按真实尺寸比例绘制（d 越大头部越大，L 越长杆身越长）
- 每张图自带规格文字标注（M6 × 20 / UNC 1/4" 等）
- 每张图只属于一个 SKU（绝不重复）
"""

import json
import os
import re

with open('/tmp/sku_parsed.json') as f:
    SKUS = json.load(f)

SVG_HEAD = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <radialGradient id="bg" cx="50%" cy="42%" r="75%">
      <stop offset="0%" stop-color="#f5f7fa"/><stop offset="50%" stop-color="#e2e8f0"/><stop offset="100%" stop-color="#a8b2bf"/>
    </radialGradient>
    <linearGradient id="metal" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2a3038"/><stop offset="15%" stop-color="#5a6370"/><stop offset="30%" stop-color="#8a92a0"/><stop offset="45%" stop-color="#e8edf4"/><stop offset="52%" stop-color="#ffffff" stop-opacity="0.9"/><stop offset="58%" stop-color="#e8edf4"/><stop offset="75%" stop-color="#8a92a0"/><stop offset="100%" stop-color="#2a3038"/>
    </linearGradient>
    <linearGradient id="topShine" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.55"/><stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <filter id="shadow"><feGaussianBlur in="SourceAlpha" stdDeviation="4"/><feOffset dx="0" dy="6"/><feComponentTransfer><feFuncA type="linear" slope="0.45"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" seed="5"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.06 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg)"/>
'''

# 通用：尺寸标尺 + 规格标签（每个图都有）
def spec_overlay(sku_id, spec, std_short, grade_short):
    """规格文字覆盖层：右上角规格标签 + 左上角 SKU 编号"""
    return f'''
  <!-- 规格标签（右上） -->
  <rect x="320" y="20" width="180" height="58" rx="6" fill="#fff" stroke="#0a0d14" stroke-width="2" opacity="0.95"/>
  <text x="332" y="48" font-family="Consolas,monospace" font-size="22" font-weight="700" fill="#0a0d14">{spec}</text>
  <text x="332" y="68" font-family="Consolas,monospace" font-size="12" fill="#666">{std_short} · {grade_short}</text>
  <!-- SKU 编号（左上） -->
  <rect x="14" y="14" width="68" height="30" rx="4" fill="#f7811a" opacity="0.95"/>
  <text x="48" y="34" font-family="Consolas,monospace" font-size="16" font-weight="700" fill="#fff" text-anchor="middle">{sku_id}</text>'''

# 比例换算：直径 d (mm) → 视觉宽度 shaft_d_px (clamped 18-72)
def d_to_px(d):
    return max(20, min(72, d * 3.6))

# 比例换算：长度 L (mm) → 视觉长度 shaft_L_px (clamped 50-380)
def L_to_px(L):
    if L >= 1000:  # 螺杆
        return 360
    return max(40, min(360, L * 2.2))

# 头部高度 (mm) → 视觉 head_h_px
def head_h_px(d, factor=0.7):
    return max(20, min(80, d * factor * 3))

# 螺纹
def thread_lines(x, y, count, spacing, color='#0a0d14'):
    s = ''
    for i in range(count):
        yp = y + i * spacing
        s += f'  <line x1="{x}" y1="{yp}" x2="{x+60}" y2="{yp+1}" stroke="{color}" stroke-width="2" opacity="0.75"/>\n'
        s += f'  <line x1="{x}" y1="{yp+1}" x2="{x+60}" y2="{yp+2}" stroke="#000" stroke-width="1" opacity="0.5"/>\n'
        s += f'  <line x1="{x+2}" y1="{yp-1}" x2="{x+58}" y2="{yp}" stroke="#fff" stroke-width="1" opacity="0.5"/>\n'
    return s

def shadow_ground(y):
    return f'  <ellipse cx="256" cy="{y}" rx="120" ry="12" fill="#000" opacity="0.3" filter="url(#shadow)"/>'

# ========== 螺栓渲染 ==========
def render_hex_bolt(sku):
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d)
    shaft_L = L_to_px(L)
    head_h = head_h_px(d, 0.7)
    head_w = shaft_d * 1.8  # 六角对边 AF ≈ 1.5-1.7d
    head_top_y = 256 - shaft_L/2 - head_h
    shaft_top_y = head_top_y + head_h
    shaft_bottom_y = shaft_top_y + shaft_L
    
    # 中心 X = 256
    cx = 256
    sx = cx - shaft_d/2
    
    body = ''
    body += shadow_ground(shaft_bottom_y + 5)
    body += '  <g filter="url(#shadow)">\n'
    # 螺杆
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{shaft_L}" fill="url(#metal)"/>\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{min(40, shaft_L*0.3)}" fill="url(#topShine)"/>\n'
    # 螺纹
    thread_count = int(shaft_L / 12)
    body += thread_lines(sx, shaft_top_y + 14, thread_count, 12)
    # 六角头
    hhx1, hhx2 = cx - head_w/2, cx + head_w/2
    body += f'    <polygon points="{hhx1},{head_top_y+head_h*0.3} {cx},{head_top_y} {hhx2},{head_top_y+head_h*0.3} {hhx2},{head_top_y+head_h*0.7} {cx},{head_top_y+head_h} {hhx1},{head_top_y+head_h*0.7}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <polygon points="{hhx1},{head_top_y+head_h*0.3} {cx},{head_top_y} {hhx2},{head_top_y+head_h*0.3}" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <polygon points="{cx},{head_top_y+8} {hhx2-4},{head_top_y+head_h*0.3-2} {cx},{head_top_y+head_h*0.3+4}" fill="#fff" opacity="0.28"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_socket_cap(sku):
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d)
    shaft_L = L_to_px(L)
    head_h = head_h_px(d, 0.6)
    head_r = shaft_d * 1.4
    cx = 256
    sx = cx - shaft_d/2
    head_top_y = 256 - shaft_L/2 - head_h
    shaft_top_y = head_top_y + head_h
    shaft_bottom_y = shaft_top_y + shaft_L
    
    body = ''
    body += shadow_ground(shaft_bottom_y + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{shaft_L}" fill="url(#metal)"/>\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{min(40, shaft_L*0.3)}" fill="url(#topShine)"/>\n'
    thread_count = int(shaft_L / 12)
    body += thread_lines(sx, shaft_top_y + 14, thread_count, 12)
    # 圆柱头
    body += f'    <ellipse cx="{cx}" cy="{head_top_y + head_h/2}" rx="{head_r}" ry="{head_h/2}" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <rect x="{cx-head_r}" y="{head_top_y + head_h/2}" width="{head_r*2}" height="{head_h/2}" fill="url(#metal)"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y + head_h/2}" rx="{head_r}" ry="{head_h/2}" fill="#fff" opacity="0.18"/>\n'
    # 内六角
    body += f'    <ellipse cx="{cx}" cy="{head_top_y + head_h/2}" rx="{head_r*0.45}" ry="{head_h*0.18}" fill="#0a0d14"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y + head_h/2}" rx="{head_r*0.45}" ry="{head_h*0.18}" fill="none" stroke="#525a68" stroke-width="1.5"/>\n'
    body += f'    <polygon points="{cx},{head_top_y + head_h/2 - head_h*0.13} {cx+head_r*0.4},{head_top_y + head_h/2} {cx},{head_top_y + head_h/2 + head_h*0.13} {cx-head_r*0.4},{head_top_y + head_h/2}" fill="none" stroke="#000" stroke-width="1.5"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_countersunk_socket(sku):
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d)
    shaft_L = L_to_px(L)
    head_h = head_h_px(d, 0.5)
    head_r = shaft_d * 2.0
    cx = 256
    sx = cx - shaft_d/2
    head_top_y = 256 - shaft_L/2 - head_h
    shaft_top_y = head_top_y + head_h
    shaft_bottom_y = shaft_top_y + shaft_L
    
    body = ''
    body += shadow_ground(shaft_bottom_y + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{shaft_L}" fill="url(#metal)"/>\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{min(40, shaft_L*0.3)}" fill="url(#topShine)"/>\n'
    thread_count = int(shaft_L / 12)
    body += thread_lines(sx, shaft_top_y + 14, thread_count, 12)
    # 沉头
    body += f'    <polygon points="{cx-head_r},{head_top_y+head_h*0.3} {cx},{head_top_y+head_h} {cx+head_r},{head_top_y+head_h*0.3}" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y+head_h*0.3}" rx="{head_r}" ry="{head_h*0.4}" fill="#dde3eb" stroke="#1a1e25" stroke-width="1"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y+head_h*0.3-2}" rx="{head_r}" ry="{head_h*0.4}" fill="#fff" opacity="0.3"/>\n'
    # 内六角
    body += f'    <line x1="{cx}" y1="{head_top_y+head_h*0.1}" x2="{cx}" y2="{head_top_y+head_h*0.5}" stroke="#0a0d14" stroke-width="6"/>\n'
    body += f'    <line x1="{cx-head_r*0.3}" y1="{head_top_y+head_h*0.3}" x2="{cx+head_r*0.3}" y2="{head_top_y+head_h*0.3}" stroke="#0a0d14" stroke-width="6"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_carriage(sku):
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d)
    shaft_L = L_to_px(L)
    head_h = head_h_px(d, 0.5)
    head_r = shaft_d * 1.4
    cx = 256
    sx = cx - shaft_d/2
    head_top_y = 256 - shaft_L/2 - head_h - 10
    neck_top_y = head_top_y + head_h
    neck_h = head_h * 0.6
    shaft_top_y = neck_top_y + neck_h
    shaft_bottom_y = shaft_top_y + shaft_L
    
    body = ''
    body += shadow_ground(shaft_bottom_y + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{shaft_L}" fill="url(#metal)"/>\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{min(40, shaft_L*0.3)}" fill="url(#topShine)"/>\n'
    thread_count = int(shaft_L / 12)
    body += thread_lines(sx, shaft_top_y + 14, thread_count, 12)
    # 圆头
    body += f'    <ellipse cx="{cx}" cy="{head_top_y}" rx="{head_r}" ry="{head_r*0.5}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx-head_r*0.2}" cy="{head_top_y-head_r*0.15}" rx="{head_r*0.6}" ry="{head_r*0.25}" fill="#fff" opacity="0.5"/>\n'
    # 方颈
    body += f'    <rect x="{cx-head_r*0.35}" y="{neck_top_y}" width="{head_r*0.7}" height="{neck_h}" fill="#7e8896" stroke="#1a1e25" stroke-width="1"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_t_bolt(sku):
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d)
    shaft_L = L_to_px(L)
    head_h = head_h_px(d, 0.8)
    cx = 256
    sx = cx - shaft_d/2
    head_top_y = 256 - shaft_L/2 - head_h
    shaft_top_y = head_top_y + head_h
    shaft_bottom_y = shaft_top_y + shaft_L
    
    body = ''
    body += shadow_ground(shaft_bottom_y + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{shaft_L}" fill="url(#metal)"/>\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{min(40, shaft_L*0.3)}" fill="url(#topShine)"/>\n'
    thread_count = int(shaft_L / 12)
    body += thread_lines(sx, shaft_top_y + 14, thread_count, 12)
    # T 型头
    tbar_w = shaft_d * 4
    body += f'    <rect x="{cx-tbar_w/2}" y="{head_top_y}" width="{tbar_w}" height="{head_h}" rx="3" fill="url(#metal)"/>\n'
    body += f'    <rect x="{cx-tbar_w/2}" y="{head_top_y}" width="{tbar_w}" height="{head_h*0.25}" fill="#fff" opacity="0.35"/>\n'
    body += f'    <rect x="{cx-tbar_w/2}" y="{head_top_y+head_h*0.75}" width="{tbar_w}" height="{head_h*0.25}" fill="#000" opacity="0.25"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_u_bolt(sku):
    p = sku['parsed']
    d = p.get('d', 12)
    shaft_d = d_to_px(d)
    span = 200
    cx = 256
    body = ''
    body += shadow_ground(450)
    body += '  <g filter="url(#shadow)">\n'
    # U 形
    body += f'    <path d="M {cx-span/2} 200 Q {cx} {200-span/2.5} {cx+span/2} 200 L {cx+span/2} 420 L {cx+span/2-shaft_d} 420 L {cx+span/2-shaft_d} 215 Q {cx} {200-span/2.5+shaft_d/2} {cx-span/2+shaft_d} 215 L {cx-span/2+shaft_d} 420 L {cx-span/2} 420 Z" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>\n'
    # 螺纹
    for i in range(15):
        y = 280 + i * 9
        body += f'    <line x1="{cx-span/2}" y1="{y}" x2="{cx-span/2+6}" y2="{y+1}" stroke="#0a0d14" stroke-width="1.5" opacity="0.75"/>\n'
        body += f'    <line x1="{cx+span/2-6}" y1="{y}" x2="{cx+span/2}" y2="{y+1}" stroke="#0a0d14" stroke-width="1.5" opacity="0.75"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_anchor(sku):
    p = sku['parsed']
    d, L = p.get('d', 16), p.get('L', 300)
    shaft_d = d_to_px(d)
    # 上部直杆 + 下部弯钩
    body = ''
    body += shadow_ground(450)
    body += '  <g filter="url(#shadow)">\n'
    # 头
    body += f'    <rect x="{256-shaft_d*1.4}" y="120" width="{shaft_d*2.8}" height="{shaft_d*1.4}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    # 头斜面
    body += f'    <polygon points="{256-shaft_d*1.6},120 {256+shaft_d*1.6},120 {256+shaft_d*1.4},135 {256-shaft_d*1.4},135" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1"/>\n'
    # 杆
    body += f'    <rect x="{256-shaft_d/2}" y="135" width="{shaft_d}" height="180" fill="url(#metal)"/>\n'
    # 弯钩
    body += f'    <path d="M {256-shaft_d/2} 315 L {256-shaft_d/2} 350 Q {256-shaft_d/2} 400 {256-shaft_d*1.5} 400 L {256-shaft_d*1.5} 360" fill="none" stroke="url(#metal)" stroke-width="{shaft_d}" stroke-linecap="round"/>\n'
    body += f'    <path d="M {256-shaft_d/2} 315 L {256-shaft_d/2} 350 Q {256-shaft_d/2} 400 {256-shaft_d*1.5} 400 L {256-shaft_d*1.5} 360" fill="none" stroke="#fff" stroke-width="{shaft_d*0.3}" opacity="0.4"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_flange_bolt(sku):
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d)
    shaft_L = L_to_px(L)
    flange_r = shaft_d * 1.8
    cx = 256
    sx = cx - shaft_d/2
    head_top_y = 256 - shaft_L/2 - 18
    shaft_top_y = head_top_y + 18
    shaft_bottom_y = shaft_top_y + shaft_L
    
    body = ''
    body += shadow_ground(shaft_bottom_y + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{shaft_L}" fill="url(#metal)"/>\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{min(40, shaft_L*0.3)}" fill="url(#topShine)"/>\n'
    thread_count = int(shaft_L / 12)
    body += thread_lines(sx, shaft_top_y + 14, thread_count, 12)
    # 法兰盘
    body += f'    <ellipse cx="{cx}" cy="{head_top_y+10}" rx="{flange_r}" ry="10" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y+8}" rx="{flange_r}" ry="10" fill="url(#metal)"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y+8}" rx="{flange_r}" ry="10" fill="#fff" opacity="0.25"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y+5}" rx="{flange_r*0.4}" ry="5" fill="#0a0d14"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_eye_bolt(sku):
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d)
    shaft_L = L_to_px(L)
    ring_r = shaft_d * 3.2
    cx = 256
    sx = cx - shaft_d/2
    head_top_y = 256 - shaft_L/2 - ring_r - 20
    shaft_top_y = head_top_y + ring_r + 20
    shaft_bottom_y = shaft_top_y + shaft_L
    
    body = ''
    body += shadow_ground(shaft_bottom_y + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{shaft_L}" fill="url(#metal)"/>\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{min(40, shaft_L*0.3)}" fill="url(#topShine)"/>\n'
    thread_count = int(shaft_L / 12)
    body += thread_lines(sx, shaft_top_y + 14, thread_count, 12)
    # 圆环
    body += f'    <circle cx="{cx}" cy="{head_top_y + ring_r}" r="{ring_r}" fill="none" stroke="#3a4250" stroke-width="{shaft_d*1.2}"/>\n'
    body += f'    <circle cx="{cx}" cy="{head_top_y + ring_r}" r="{ring_r}" fill="none" stroke="url(#metal)" stroke-width="{shaft_d}"/>\n'
    body += f'    <circle cx="{cx}" cy="{head_top_y + ring_r}" r="{ring_r}" fill="none" stroke="#fff" stroke-width="2" opacity="0.5"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_wing_bolt(sku):
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d)
    shaft_L = L_to_px(L)
    wing_r = shaft_d * 3.5
    cx = 256
    sx = cx - shaft_d/2
    head_top_y = 256 - shaft_L/2 - wing_r
    shaft_top_y = head_top_y + wing_r
    shaft_bottom_y = shaft_top_y + shaft_L
    
    body = ''
    body += shadow_ground(shaft_bottom_y + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{shaft_L}" fill="url(#metal)"/>\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{min(40, shaft_L*0.3)}" fill="url(#topShine)"/>\n'
    thread_count = int(shaft_L / 12)
    body += thread_lines(sx, shaft_top_y + 14, thread_count, 12)
    # 双翼
    body += f'    <ellipse cx="{cx-wing_r*1.2}" cy="{head_top_y+wing_r*0.6}" rx="{wing_r}" ry="{wing_r*0.5}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx+wing_r*1.2}" cy="{head_top_y+wing_r*0.6}" rx="{wing_r}" ry="{wing_r*0.5}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx-wing_r*1.2}" cy="{head_top_y+wing_r*0.6-3}" rx="{wing_r}" ry="{wing_r*0.5}" fill="#fff" opacity="0.18"/>\n'
    body += f'    <ellipse cx="{cx+wing_r*1.2}" cy="{head_top_y+wing_r*0.6-3}" rx="{wing_r}" ry="{wing_r*0.5}" fill="#fff" opacity="0.18"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y+wing_r*0.6}" rx="{shaft_d*0.7}" ry="{shaft_d*0.4}" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_self_tap(sku):
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d, scale=5) * 0.7
    shaft_L = L_to_px(L) * 0.8
    head_h = 18
    head_r = shaft_d * 2.5
    cx = 256
    sx = cx - shaft_d/2
    head_top_y = 256 - shaft_L/2 - head_h - 5
    shaft_top_y = head_top_y + head_h + 5
    shaft_bottom_y = shaft_top_y + shaft_L
    
    body = ''
    body += shadow_ground(shaft_bottom_y + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{shaft_L-8}" fill="url(#metal)"/>\n'
    body += thread_lines(sx, shaft_top_y + 10, max(3, int((shaft_L-8)/10)), 10)
    # 尖锐尾部
    body += f'    <polygon points="{sx},{shaft_bottom_y-8} {sx+shaft_d},{shaft_bottom_y-8} {cx},{shaft_bottom_y+4}" fill="#3a4250"/>\n'
    # 盘头
    body += f'    <ellipse cx="{cx}" cy="{head_top_y + head_h*0.5}" rx="{head_r}" ry="{head_h*0.5}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y + head_h*0.5 - 3}" rx="{head_r}" ry="{head_h*0.5}" fill="#fff" opacity="0.3"/>\n'
    # 十字槽
    body += f'    <line x1="{cx}" y1="{head_top_y + head_h*0.1}" x2="{cx}" y2="{head_top_y + head_h*0.9}" stroke="#0a0d14" stroke-width="3"/>\n'
    body += f'    <line x1="{cx-head_r*0.4}" y1="{head_top_y + head_h*0.5}" x2="{cx+head_r*0.4}" y2="{head_top_y + head_h*0.5}" stroke="#0a0d14" stroke-width="3"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_self_drill(sku):
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d, scale=5) * 0.7
    shaft_L = L_to_px(L) * 0.8
    head_h = 22
    head_r = shaft_d * 3
    cx = 256
    sx = cx - shaft_d/2
    head_top_y = 256 - shaft_L/2 - head_h - 5
    shaft_top_y = head_top_y + head_h + 5
    shaft_bottom_y = shaft_top_y + shaft_L
    
    body = ''
    body += shadow_ground(shaft_bottom_y + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{shaft_L-12}" fill="url(#metal)"/>\n'
    body += thread_lines(sx, shaft_top_y + 10, max(3, int((shaft_L-12)/10)), 10)
    # 钻头
    body += f'    <polygon points="{sx},{shaft_bottom_y-12} {sx+shaft_d},{shaft_bottom_y-12} {sx+shaft_d-3},{shaft_bottom_y-2} {sx+3},{shaft_bottom_y-2}" fill="#3a4250"/>\n'
    body += f'    <line x1="{cx}" y1="{shaft_bottom_y-12}" x2="{cx}" y2="{shaft_bottom_y+5}" stroke="#0a0d14" stroke-width="2"/>\n'
    # 六角华司头
    body += f'    <polygon points="{cx-head_r},{head_top_y+head_h*0.3} {cx},{head_top_y} {cx+head_r},{head_top_y+head_h*0.3} {cx+head_r},{head_top_y+head_h*0.7} {cx},{head_top_y+head_h} {cx-head_r},{head_top_y+head_h*0.7}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <polygon points="{cx-head_r},{head_top_y+head_h*0.3} {cx},{head_top_y} {cx+head_r},{head_top_y+head_h*0.3}" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def d_to_px(d, scale=3.6):
    return max(18, min(72, d * scale))

# ========== 螺母渲染 ==========
def render_hex_nut(sku):
    p = sku['parsed']
    d = p.get('d', 10)
    nut_w = d_to_px(d) * 1.8  # 对边 AF
    nut_h = head_h_px(d, 0.95)  # 厚度
    cx, cy = 256, 256
    body = ''
    body += shadow_ground(cy + nut_h + 10)
    body += '  <g filter="url(#shadow)">\n'
    nwx1, nwx2 = cx - nut_w/2, cx + nut_w/2
    body += f'    <polygon points="{nwx1},{cy-nut_h*0.3} {cx},{cy-nut_h*0.7} {nwx2},{cy-nut_h*0.3} {nwx2},{cy+nut_h*0.3} {cx},{cy+nut_h*0.7} {nwx1},{cy+nut_h*0.3}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>\n'
    body += f'    <polygon points="{nwx1},{cy-nut_h*0.3} {cx},{cy-nut_h*0.7} {nwx2},{cy-nut_h*0.3} {nwx2},{cy+nut_h*0.3} {cx},{cy+nut_h*0.7} {nwx1},{cy+nut_h*0.3}" fill="none" stroke="#1a1e25" stroke-width="1.5"/>\n'
    body += f'    <polygon points="{nwx1},{cy-nut_h*0.3} {cx},{cy-nut_h*0.7} {nwx2},{cy-nut_h*0.3}" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.5"/>\n'
    body += f'    <polygon points="{cx},{cy-nut_h*0.6} {nwx2-4},{cy-nut_h*0.3+2} {cx},{cy}" fill="#fff" opacity="0.3"/>\n'
    # 中心孔
    body += f'    <ellipse cx="{cx}" cy="{cy-nut_h*0.3}" rx="{nut_w*0.35}" ry="{nut_h*0.12}" fill="#0a0d14"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy-nut_h*0.32}" rx="{nut_w*0.35}" ry="{nut_h*0.1}" fill="#000"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_lock_nut(sku):
    p = sku['parsed']
    d = p.get('d', 10)
    nut_w = d_to_px(d) * 1.8
    nut_h = head_h_px(d, 1.0)  # 锁紧螺母更高
    cx, cy = 256, 256
    body = ''
    body += shadow_ground(cy + nut_h + 10)
    body += '  <g filter="url(#shadow)">\n'
    nwx1, nwx2 = cx - nut_w/2, cx + nut_w/2
    body += f'    <polygon points="{nwx1},{cy-nut_h*0.5} {cx},{cy-nut_h*0.9} {nwx2},{cy-nut_h*0.5} {nwx2},{cy+nut_h*0.5} {cx},{cy+nut_h*0.9} {nwx1},{cy+nut_h*0.5}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>\n'
    body += f'    <polygon points="{nwx1},{cy-nut_h*0.5} {cx},{cy-nut_h*0.9} {nwx2},{cy-nut_h*0.5} {nwx2},{cy+nut_h*0.5} {cx},{cy+nut_h*0.9} {nwx1},{cy+nut_h*0.5}" fill="none" stroke="#1a1e25" stroke-width="1.5"/>\n'
    body += f'    <polygon points="{nwx1},{cy-nut_h*0.5} {cx},{cy-nut_h*0.9} {nwx2},{cy-nut_h*0.5}" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.5"/>\n'
    # 尼龙环（黄色表示）
    body += f'    <ellipse cx="{cx}" cy="{cy-nut_h*0.5}" rx="{nut_w*0.35}" ry="{nut_h*0.12}" fill="#1a1e25"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy-nut_h*0.52}" rx="{nut_w*0.35}" ry="{nut_h*0.1}" fill="#e0c060"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy-nut_h*0.5}" rx="{nut_w*0.35}" ry="{nut_h*0.12}" fill="none" stroke="#7a6533" stroke-width="1"/>\n'
    # 底部孔
    body += f'    <ellipse cx="{cx}" cy="{cy+nut_h*0.5}" rx="{nut_w*0.32}" ry="{nut_h*0.1}" fill="#0a0d14"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_flange_nut(sku):
    p = sku['parsed']
    d = p.get('d', 10)
    nut_w = d_to_px(d) * 1.6
    nut_h = head_h_px(d, 0.9)
    flange_r = nut_w * 1.3
    cx, cy = 256, 240
    body = ''
    body += shadow_ground(cy + nut_h/2 + 10)
    body += '  <g filter="url(#shadow)">\n'
    # 法兰盘
    body += f'    <ellipse cx="{cx}" cy="{cy}" rx="{flange_r}" ry="{flange_r*0.18}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy-2}" rx="{flange_r}" ry="{flange_r*0.18}" fill="#fff" opacity="0.25"/>\n'
    # 六角主体
    body += f'    <polygon points="{cx-nut_w/2},{cy+nut_h*0.3} {cx},{cy-nut_h*0.1} {cx+nut_w/2},{cy+nut_h*0.3} {cx+nut_w/2},{cy+nut_h*0.8} {cx},{cy+nut_h*1.2} {cx-nut_w/2},{cy+nut_h*0.8}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <polygon points="{cx-nut_w/2},{cy+nut_h*0.3} {cx},{cy-nut_h*0.1} {cx+nut_w/2},{cy+nut_h*0.3}" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy+nut_h*0.3}" rx="{nut_w*0.3}" ry="{nut_h*0.1}" fill="#0a0d14"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_cap_nut(sku):
    p = sku['parsed']
    d = p.get('d', 10)
    nut_w = d_to_px(d) * 1.8
    nut_h = head_h_px(d, 1.1)
    cap_h = head_h_px(d, 0.5)
    cx, cy = 256, 256
    body = ''
    body += shadow_ground(cy + nut_h + 10)
    body += '  <g filter="url(#shadow)">\n'
    nwx1, nwx2 = cx - nut_w/2, cx + nut_w/2
    body += f'    <polygon points="{nwx1},{cy-nut_h*0.3} {cx},{cy-nut_h*0.7} {nwx2},{cy-nut_h*0.3} {nwx2},{cy+nut_h*0.3} {cx},{cy+nut_h*0.7} {nwx1},{cy+nut_h*0.3}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>\n'
    body += f'    <polygon points="{nwx1},{cy-nut_h*0.3} {cx},{cy-nut_h*0.7} {nwx2},{cy-nut_h*0.3}" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.5"/>\n'
    # 圆顶
    body += f'    <ellipse cx="{cx}" cy="{cy-nut_h*0.7}" rx="{nut_w}" ry="{cap_h}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy-nut_h*0.7-3}" rx="{nut_w}" ry="{cap_h}" fill="#fff" opacity="0.32"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_square_nut(sku):
    p = sku['parsed']
    d = p.get('d', 10)
    nut_w = d_to_px(d) * 1.8
    nut_h = head_h_px(d, 0.9)
    cx, cy = 256, 256
    body = ''
    body += shadow_ground(cy + nut_h + 10)
    body += '  <g filter="url(#shadow)">\n'
    # 方块 3D 透视
    body += f'    <polygon points="{cx-nut_w/2},{cy-nut_h*0.3} {cx},{cy-nut_h*0.7} {cx+nut_w/2},{cy-nut_h*0.3} {cx+nut_w/2},{cy+nut_h*0.3} {cx},{cy+nut_h*0.7} {cx-nut_w/2},{cy+nut_h*0.3}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>\n'
    body += f'    <polygon points="{cx-nut_w/2},{cy-nut_h*0.3} {cx},{cy-nut_h*0.7} {cx+nut_w/2},{cy-nut_h*0.3}" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.5"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy-nut_h*0.3}" rx="{nut_w*0.35}" ry="{nut_h*0.12}" fill="#0a0d14"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_wing_nut(sku):
    p = sku['parsed']
    d = p.get('d', 10)
    nut_w = d_to_px(d) * 1.6
    nut_h = head_h_px(d, 1.0)
    wing_r = nut_w * 1.3
    cx, cy = 256, 256
    body = ''
    body += shadow_ground(cy + nut_h + 10)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <ellipse cx="{cx-wing_r*1.2}" cy="{cy}" rx="{wing_r}" ry="{wing_r*0.5}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx+wing_r*1.2}" cy="{cy}" rx="{wing_r}" ry="{wing_r*0.5}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx-wing_r*1.2}" cy="{cy-3}" rx="{wing_r}" ry="{wing_r*0.5}" fill="#fff" opacity="0.2"/>\n'
    body += f'    <ellipse cx="{cx+wing_r*1.2}" cy="{cy-3}" rx="{wing_r}" ry="{wing_r*0.5}" fill="#fff" opacity="0.2"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy}" rx="{nut_w*0.65}" ry="{nut_h*0.4}" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy-2}" rx="{nut_w*0.65}" ry="{nut_h*0.4}" fill="url(#metal)"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy-2}" rx="{nut_w*0.25}" ry="{nut_h*0.15}" fill="#0a0d14"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_t_slot_nut(sku):
    p = sku['parsed']
    d = p.get('d', 10)
    nut_w = d_to_px(d) * 1.6
    nut_h = head_h_px(d, 0.7)
    block_w = nut_w * 4
    block_h = nut_h * 1.8
    cx, cy = 256, 256
    body = ''
    body += shadow_ground(cy + block_h/2 + 10)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{cx-block_w/2}" y="{cy-block_h/2}" width="{block_w}" height="{block_h}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>\n'
    body += f'    <rect x="{cx-block_w/2}" y="{cy-block_h/2}" width="{block_w}" height="{block_h*0.15}" fill="#fff" opacity="0.4"/>\n'
    body += f'    <rect x="{cx-block_w/2}" y="{cy+block_h*0.35}" width="{block_w}" height="{block_h*0.15}" fill="#000" opacity="0.35"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy}" rx="{nut_w*0.4}" ry="{nut_h*0.15}" fill="#0a0d14"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_weld_nut(sku):
    p = sku['parsed']
    d = p.get('d', 10)
    nut_w = d_to_px(d) * 1.8
    nut_h = head_h_px(d, 0.7)
    cx, cy = 256, 256
    body = ''
    body += shadow_ground(cy + nut_h + 10)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <polygon points="{cx-nut_w/2},{cy-nut_h*0.3} {cx},{cy-nut_h*0.7} {cx+nut_w/2},{cy-nut_h*0.3} {cx+nut_w/2},{cy+nut_h*0.3} {cx},{cy+nut_h*0.7} {cx-nut_w/2},{cy+nut_h*0.3}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>\n'
    body += f'    <polygon points="{cx-nut_w/2},{cy-nut_h*0.3} {cx},{cy-nut_h*0.7} {cx+nut_w/2},{cy-nut_h*0.3}" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.5"/>\n'
    # 4 个焊点
    body += f'    <circle cx="{cx-nut_w*0.5}" cy="{cy+nut_h*0.4}" r="6" fill="#3a4250"/>\n'
    body += f'    <circle cx="{cx+nut_w*0.5}" cy="{cy+nut_h*0.4}" r="6" fill="#3a4250"/>\n'
    body += f'    <circle cx="{cx-nut_w*0.5}" cy="{cy-nut_h*0.05}" r="6" fill="#3a4250"/>\n'
    body += f'    <circle cx="{cx+nut_w*0.5}" cy="{cy-nut_h*0.05}" r="6" fill="#3a4250"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy-nut_h*0.3}" rx="{nut_w*0.35}" ry="{nut_h*0.12}" fill="#0a0d14"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_rivet_nut(sku):
    p = sku['parsed']
    d = p.get('d', 6)
    nut_w = d_to_px(d) * 1.8
    nut_h = head_h_px(d, 1.8)  # 拉铆螺母较高
    cx, cy = 256, 240
    body = ''
    body += shadow_ground(cy + nut_h/2 + 10)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <ellipse cx="{cx}" cy="{cy}" rx="{nut_w}" ry="{nut_w*0.18}" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <rect x="{cx-nut_w}" y="{cy}" width="{nut_w*2}" height="{nut_h}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy+nut_h}" rx="{nut_w}" ry="{nut_w*0.18}" fill="#3a4250" stroke="#1a1e25" stroke-width="1"/>\n'
    # 螺纹
    for i in range(int(nut_h/8)):
        y = cy + 10 + i * 8
        body += f'    <line x1="{cx-nut_w+4}" y1="{y}" x2="{cx+nut_w-4}" y2="{y+2}" stroke="#0a0d14" stroke-width="1.2" opacity="0.6"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy}" rx="{nut_w*0.3}" ry="{nut_w*0.08}" fill="#0a0d14"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

# ========== 螺杆 ==========
def render_threaded_rod(sku):
    p = sku['parsed']
    d = p.get('d', 10)
    shaft_d = d_to_px(d)
    shaft_L = L_to_px(p.get('L', 1000))
    cx = 256
    sx = cx - shaft_d/2
    top_y = 256 - shaft_L/2
    body = ''
    body += shadow_ground(top_y + shaft_L + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{sx}" y="{top_y}" width="{shaft_d}" height="{shaft_L}" fill="url(#metal)"/>\n'
    body += f'    <rect x="{sx}" y="{top_y}" width="{shaft_d}" height="{min(50, shaft_L*0.2)}" fill="url(#topShine)"/>\n'
    thread_count = int(shaft_L / 12)
    body += thread_lines(sx, top_y + 14, thread_count, 12)
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_stud_1end(sku):
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d)
    shaft_L = L_to_px(L)
    thread_L = shaft_L * 0.55
    cx = 256
    sx = cx - shaft_d/2
    top_y = 256 - shaft_L/2
    body = ''
    body += shadow_ground(top_y + shaft_L + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{sx}" y="{top_y}" width="{shaft_d}" height="{shaft_L-thread_L}" fill="url(#metal)"/>\n'
    body += f'    <rect x="{sx}" y="{top_y+shaft_L-thread_L}" width="{shaft_d}" height="{thread_L}" fill="url(#metal)"/>\n'
    thread_count = int(thread_L / 12)
    body += thread_lines(sx, top_y + shaft_L - thread_L + 14, thread_count, 12)
    body += f'    <polygon points="{sx},{top_y} {sx+shaft_d},{top_y} {cx},{top_y-12}" fill="#3a4250"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_stud_2end(sku):
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d)
    shaft_L = L_to_px(L)
    thread_L = shaft_L * 0.4
    cx = 256
    sx = cx - shaft_d/2
    top_y = 256 - shaft_L/2
    body = ''
    body += shadow_ground(top_y + shaft_L + 5)
    body += '  <g filter="url(#shadow)">\n'
    # 中间光杆
    body += f'    <rect x="{sx}" y="{top_y+thread_L}" width="{shaft_d}" height="{shaft_L-thread_L*2}" fill="url(#metal)"/>\n'
    # 上螺纹
    body += f'    <rect x="{sx}" y="{top_y}" width="{shaft_d}" height="{thread_L}" fill="url(#metal)"/>\n'
    body += thread_lines(sx, top_y + 14, int(thread_L/12), 12)
    # 下螺纹
    body += f'    <rect x="{sx}" y="{top_y+shaft_L-thread_L}" width="{shaft_d}" height="{thread_L}" fill="url(#metal)"/>\n'
    body += thread_lines(sx, top_y + shaft_L - thread_L + 14, int(thread_L/12), 12)
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

# ========== 紧固件 ==========
def render_flat_washer(sku):
    p = sku['parsed']
    od = p.get('od', 20)
    t = max(2, od * 0.1)
    inner_d = p.get('d', 10)
    od_px = max(60, min(280, od * 8))
    inner_px = max(20, min(100, inner_d * 6))
    thickness_px = max(20, min(60, t * 12))
    cx, cy = 256, 240
    body = ''
    body += shadow_ground(cy + thickness_px/2 + 10)
    body += '  <g filter="url(#shadow)">\n'
    # 椭圆（透视）
    body += f'    <ellipse cx="{cx}" cy="{cy}" rx="{od_px/2}" ry="{od_px*0.18}" fill="url(#metal)" stroke="#1a1e25" stroke-width="2"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy-2}" rx="{od_px/2}" ry="{od_px*0.18}" fill="#fff" opacity="0.25"/>\n'
    # 厚度
    body += f'    <rect x="{cx-od_px/2}" y="{cy}" width="{od_px}" height="{thickness_px}" fill="url(#metal)"/>\n'
    body += f'    <line x1="{cx-od_px/2}" y1="{cy}" x2="{cx+od_px/2}" y2="{cy}" stroke="#fff" stroke-width="2" opacity="0.5"/>\n'
    body += f'    <line x1="{cx-od_px/2}" y1="{cy+thickness_px}" x2="{cx+od_px/2}" y2="{cy+thickness_px}" stroke="#000" stroke-width="2" opacity="0.4"/>\n'
    # 底部椭圆
    body += f'    <ellipse cx="{cx}" cy="{cy+thickness_px}" rx="{od_px/2}" ry="{od_px*0.18}" fill="#3a4250" opacity="0.7"/>\n'
    # 中心孔
    body += f'    <ellipse cx="{cx}" cy="{cy+thickness_px/2}" rx="{inner_px/2}" ry="{inner_px*0.18}" fill="#0a0d14"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_spring_washer(sku):
    p = sku['parsed']
    d = p.get('d', 10)
    od_px = max(100, min(280, d * 16))
    cx, cy = 256, 256
    body = ''
    body += shadow_ground(cy + 30)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <path d="M {cx} {cy-od_px/2} A {od_px/2} {od_px/2} 0 1 1 {cx-30} {cy+od_px*0.3} L {cx} {cy-od_px/2} Z" fill="url(#metal)" stroke="#1a1e25" stroke-width="2"/>\n'
    body += f'    <path d="M {cx} {cy-od_px/2} A {od_px/2} {od_px/2} 0 0 1 {cx+od_px*0.5} {cy+od_px*0.2} L {cx-30} {cy+od_px*0.3} L {cx} {cy-od_px/2} Z" fill="#a8b3c0" opacity="0.45"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy}" rx="{od_px*0.4}" ry="{od_px*0.1}" fill="url(#metal)"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy-2}" rx="{od_px*0.4}" ry="{od_px*0.1}" fill="#fff" opacity="0.2"/>\n'
    body += f'    <line x1="{cx-30}" y1="{cy+od_px*0.3}" x2="{cx}" y2="{cy-od_px/2}" stroke="#0a0d14" stroke-width="2.5"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy}" rx="{od_px*0.25}" ry="{od_px*0.06}" fill="#0a0d14"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_cotter_pin(sku):
    p = sku['parsed']
    d, L = p.get('d', 3), p.get('L', 30)
    pin_d = max(10, min(20, d * 3))
    pin_L = L_to_px(L)
    cx = 256
    top_y = 256 - pin_L/2
    body = ''
    body += shadow_ground(top_y + pin_L + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{cx-pin_d/2}" y="{top_y+pin_d*1.5}" width="{pin_d}" height="{pin_L-pin_d*2}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{top_y+pin_d*1.5}" rx="{pin_d/2}" ry="{pin_d*0.7}" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{top_y+pin_d}" rx="{pin_d/2*1.4}" ry="{pin_d*1}" fill="none" stroke="#3a4250" stroke-width="{pin_d*0.6}"/>\n'
    body += f'    <polygon points="{cx-pin_d/2},{top_y+pin_L-pin_d*0.5} {cx+pin_d/2},{top_y+pin_L-pin_d*0.5} {cx},{top_y+pin_L+pin_d*2}" fill="#3a4250"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_spring_pin(sku):
    p = sku['parsed']
    d, L = p.get('d', 6), p.get('L', 30)
    pin_d = max(16, min(50, d * 4))
    pin_L = L_to_px(L)
    cx = 256
    top_y = 256 - pin_L/2
    body = ''
    body += shadow_ground(top_y + pin_L + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{cx-pin_d/2}" y="{top_y}" width="{pin_d}" height="{pin_L}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>\n'
    # 槽
    for i in range(int(pin_L/14)):
        y = top_y + 12 + i * 14
        body += f'    <line x1="{cx-pin_d/2+2}" y1="{y}" x2="{cx+pin_d/2-2}" y2="{y}" stroke="#0a0d14" stroke-width="1.5" opacity="0.7"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{top_y}" rx="{pin_d/2}" ry="{pin_d*0.25}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{top_y+pin_L}" rx="{pin_d/2}" ry="{pin_d*0.25}" fill="#3a4250" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_dowel_pin(sku):
    p = sku['parsed']
    d, L = p.get('d', 8), p.get('L', 40)
    pin_d = max(16, min(50, d * 4))
    pin_L = L_to_px(L)
    cx = 256
    top_y = 256 - pin_L/2
    body = ''
    body += shadow_ground(top_y + pin_L + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{cx-pin_d/2}" y="{top_y}" width="{pin_d}" height="{pin_L}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{top_y}" rx="{pin_d/2}" ry="{pin_d*0.3}" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{top_y+pin_L}" rx="{pin_d/2}" ry="{pin_d*0.3}" fill="#3a4250" stroke="#1a1e25" stroke-width="1"/>\n'
    body += f'    <line x1="{cx-pin_d/2}" y1="{top_y}" x2="{cx+pin_d/2}" y2="{top_y}" stroke="#fff" stroke-width="2" opacity="0.5"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_rivet_round(sku):
    p = sku['parsed']
    d, L = p.get('d', 4), p.get('L', 12)
    head_r = max(20, min(60, d * 6))
    shaft_d = head_r * 0.4
    shaft_L = L_to_px(L) * 0.6
    cx = 256
    head_top_y = 256 - shaft_L/2 - head_r
    body = ''
    body += shadow_ground(head_top_y + shaft_L + head_r*0.5 + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y}" rx="{head_r}" ry="{head_r}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx-head_r*0.25}" cy="{head_top_y-head_r*0.25}" rx="{head_r*0.45}" ry="{head_r*0.45}" fill="#fff" opacity="0.55"/>\n'
    body += f'    <rect x="{cx-shaft_d/2}" y="{head_top_y+head_r*0.5}" width="{shaft_d}" height="{shaft_L}" fill="url(#metal)"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y+head_r*0.5+shaft_L}" rx="{shaft_d*0.6}" ry="{shaft_d*0.3}" fill="#3a4250" stroke="#1a1e25" stroke-width="1"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_rivet_csk(sku):
    p = sku['parsed']
    d, L = p.get('d', 4), p.get('L', 12)
    head_r = max(20, min(60, d * 6))
    shaft_d = head_r * 0.4
    shaft_L = L_to_px(L) * 0.6
    cx = 256
    head_top_y = 256 - shaft_L/2 - head_r*0.7
    body = ''
    body += shadow_ground(head_top_y + shaft_L + head_r*0.3 + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <polygon points="{cx-head_r},{head_top_y+head_r*0.3} {cx},{head_top_y+head_r*1.0} {cx+head_r},{head_top_y+head_r*0.3}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y+head_r*0.3}" rx="{head_r}" ry="{head_r*0.25}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y+head_r*0.3-2}" rx="{head_r}" ry="{head_r*0.25}" fill="#fff" opacity="0.3"/>\n'
    body += f'    <rect x="{cx-shaft_d/2}" y="{head_top_y+head_r*0.3}" width="{shaft_d}" height="{shaft_L}" fill="url(#metal)"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_rivet_blind(sku):
    p = sku['parsed']
    d, L = p.get('d', 4.8), p.get('L', 12)
    head_r = max(20, min(60, d * 6))
    body = ''
    body += shadow_ground(420)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <ellipse cx="256" cy="170" rx="{head_r}" ry="{head_r}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{256-head_r*0.25}" cy="{170-head_r*0.25}" rx="{head_r*0.45}" ry="{head_r*0.45}" fill="#fff" opacity="0.55"/>\n'
    body += f'    <rect x="{256-head_r*0.4}" y="200" width="{head_r*0.8}" height="80" fill="url(#metal)" stroke="#1a1e25" stroke-width="1"/>\n'
    body += f'    <ellipse cx="256" cy="280" rx="{head_r*0.32}" ry="{head_r*0.18}" fill="#3a4250" stroke="#1a1e25" stroke-width="1"/>\n'
    body += f'    <rect x="252" y="290" width="8" height="100" fill="#7e8896"/>\n'
    body += f'    <circle cx="256" cy="395" r="6" fill="#a8b3c0" stroke="#1a1e25" stroke-width="0.5"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_retaining_ring(sku):
    p = sku['parsed']
    d = p.get('d', 20)
    od_px = max(160, min(300, d * 12))
    cx, cy = 256, 256
    body = ''
    body += shadow_ground(cy + od_px/2 + 10)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <path d="M {cx-od_px/2} {cy} Q {cx-od_px/2} {cy-od_px/2} {cx} {cy-od_px/2} Q {cx+od_px/2} {cy-od_px/2} {cx+od_px/2} {cy} Q {cx+od_px/2} {cy+od_px*0.2} {cx+od_px*0.85} {cy+od_px*0.15} L {cx+od_px*0.85} {cy} Q {cx+od_px*0.85} {cy-od_px*0.35} {cx} {cy-od_px*0.35} Q {cx-od_px*0.85} {cy-od_px*0.35} {cx-od_px*0.85} {cy} L {cx-od_px*0.85} {cy+od_px*0.15} Q {cx-od_px/2} {cy+od_px*0.2} {cx-od_px/2} {cy} Z" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{cy}" rx="{od_px*0.5}" ry="{od_px*0.12}" fill="#0a0d14"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_retaining_ring_int(sku):
    return render_retaining_ring(sku)

def render_hose_clamp(sku):
    body = ''
    body += shadow_ground(420)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <ellipse cx="256" cy="256" rx="160" ry="160" fill="none" stroke="url(#metal)" stroke-width="22"/>\n'
    body += f'    <ellipse cx="256" cy="256" rx="160" ry="160" fill="none" stroke="#fff" stroke-width="2.5" opacity="0.4"/>\n'
    body += f'    <rect x="216" y="80" width="80" height="50" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>\n'
    body += f'    <circle cx="256" cy="90" r="13" fill="#0a0d14"/>\n'
    body += f'    <line x1="249" y1="83" x2="263" y2="97" stroke="#fff" stroke-width="2"/>\n'
    body += f'    <line x1="263" y1="83" x2="249" y2="97" stroke="#fff" stroke-width="2"/>\n'
    body += f'    <rect x="246" y="40" width="20" height="40" fill="url(#metal)"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_combination_screw(sku):
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d)
    shaft_L = L_to_px(L)
    head_h = 18
    head_r = shaft_d * 1.6
    cx = 256
    sx = cx - shaft_d/2
    head_top_y = 256 - shaft_L/2 - head_h - 5
    shaft_top_y = head_top_y + head_h + 5
    shaft_bottom_y = shaft_top_y + shaft_L
    
    body = ''
    body += shadow_ground(shaft_bottom_y + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{shaft_L}" fill="url(#metal)"/>\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{min(40, shaft_L*0.3)}" fill="url(#topShine)"/>\n'
    thread_count = int(shaft_L / 12)
    body += thread_lines(sx, shaft_top_y + 14, thread_count, 12)
    # 平垫圈 + 弹垫 + 头（堆叠）
    body += f'    <ellipse cx="{cx}" cy="{head_top_y-12}" rx="{head_r*1.5}" ry="6" fill="url(#metal)" stroke="#1a1e25" stroke-width="1"/>\n'
    body += f'    <path d="M {cx-head_r*1.2} {head_top_y-22} A {head_r*1.2} {head_r*1.2} 0 1 1 {cx-head_r*0.5} {head_top_y-12} L {cx-head_r*0.5} {head_top_y-12} Z" fill="url(#metal)" stroke="#1a1e25" stroke-width="1"/>\n'
    # 六角头
    body += f'    <polygon points="{cx-head_r},{head_top_y-head_h*0.4} {cx},{head_top_y-head_h} {cx+head_r},{head_top_y-head_h*0.4}" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <polygon points="{cx-head_r},{head_top_y-head_h*0.4} {cx},{head_top_y-head_h} {cx+head_r},{head_top_y-head_h*0.4}" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

def render_f028_low_head(sku):
    """F028 薄头内六角 - 用 socket_cap 但头部更薄"""
    return render_socket_cap(sku)

def render_f029_reamed(sku):
    """F029 铰制孔螺栓 - 类似 socket cap 但头部圆柱较高"""
    p = sku['parsed']
    d, L = p['d'], p['L']
    shaft_d = d_to_px(d)
    shaft_L = L_to_px(L)
    head_h = head_h_px(d, 1.0)  # 较高
    head_r = shaft_d * 1.2  # 较窄
    cx = 256
    sx = cx - shaft_d/2
    head_top_y = 256 - shaft_L/2 - head_h
    shaft_top_y = head_top_y + head_h
    shaft_bottom_y = shaft_top_y + shaft_L
    
    body = ''
    body += shadow_ground(shaft_bottom_y + 5)
    body += '  <g filter="url(#shadow)">\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{shaft_L}" fill="url(#metal)"/>\n'
    body += f'    <rect x="{sx}" y="{shaft_top_y}" width="{shaft_d}" height="{min(40, shaft_L*0.3)}" fill="url(#topShine)"/>\n'
    thread_count = int(shaft_L / 12)
    body += thread_lines(sx, shaft_top_y + 14, thread_count, 12)
    body += f'    <rect x="{cx-head_r}" y="{head_top_y}" width="{head_r*2}" height="{head_h}" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <ellipse cx="{cx}" cy="{head_top_y}" rx="{head_r}" ry="{head_r*0.18}" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.2"/>\n'
    body += f'    <rect x="{cx-head_r}" y="{head_top_y+head_h-4}" width="{head_r*2}" height="4" fill="#3a4250"/>\n'
    body += '  </g>'
    body += spec_overlay(sku['id'], sku['spec'], sku['std'].split('/')[0].strip()[:10], sku['mat'].split(' ')[0])
    body += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return SVG_HEAD + body + '\n</svg>'

# ========== 路由表 ==========
RENDERERS = {
    'B001': render_hex_bolt, 'B002': render_hex_bolt, 'B003': render_hex_bolt,
    'B004': render_hex_bolt, 'B005': render_hex_bolt, 'B006': render_hex_bolt,
    'B007': render_hex_bolt, 'B008': render_hex_bolt, 'B009': render_hex_bolt,
    'B010': render_hex_bolt,
    'B011': render_socket_cap, 'B012': render_socket_cap, 'B013': render_countersunk_socket,
    'B014': render_socket_cap, 'B015': render_socket_cap,
    'B016': render_carriage, 'B017': render_carriage, 'B018': render_t_bolt,
    'B019': render_u_bolt, 'B020': render_anchor,
    'B021': render_flange_bolt, 'B022': render_flange_bolt,
    'B023': render_eye_bolt, 'B024': render_wing_bolt, 'B025': render_carriage,
    'B026': render_self_tap, 'B027': render_self_tap, 'B028': render_self_drill,
    'B029': render_self_tap, 'B030': render_self_drill,
    'N001': render_hex_nut, 'N002': render_hex_nut, 'N003': render_hex_nut,
    'N004': render_hex_nut, 'N005': render_hex_nut, 'N006': render_hex_nut,
    'N007': render_hex_nut, 'N008': render_hex_nut, 'N028': render_hex_nut,
    'N009': render_lock_nut, 'N010': render_lock_nut, 'N011': render_lock_nut,
    'N012': render_lock_nut, 'N013': render_lock_nut,
    'N014': render_flange_nut, 'N015': render_flange_nut, 'N016': render_flange_nut,
    'N017': render_flange_nut,
    'N018': render_cap_nut, 'N019': render_cap_nut, 'N020': render_cap_nut,
    'N021': render_square_nut, 'N022': render_wing_nut, 'N023': render_wing_nut,
    'N024': render_t_slot_nut, 'N025': render_cap_nut, 'N026': render_weld_nut,
    'N027': render_rivet_nut,
    'R001': render_threaded_rod, 'R002': render_threaded_rod, 'R003': render_threaded_rod,
    'R004': render_threaded_rod, 'R005': render_threaded_rod, 'R006': render_threaded_rod,
    'R007': render_threaded_rod, 'R008': render_threaded_rod, 'R009': render_threaded_rod,
    'R010': render_stud_1end, 'R011': render_stud_2end, 'R012': render_stud_2end,
    'F001': render_flat_washer, 'F002': render_flat_washer, 'F003': render_flat_washer,
    'F004': render_flat_washer, 'F005': render_flat_washer,
    'F006': render_spring_washer, 'F007': render_spring_washer, 'F008': render_spring_washer,
    'F009': render_cotter_pin, 'F010': render_cotter_pin,
    'F011': render_spring_pin, 'F012': render_spring_pin,
    'F013': render_dowel_pin,
    'F014': render_rivet_csk, 'F015': render_rivet_csk,
    'F016': render_rivet_round, 'F017': render_rivet_blind, 'F018': render_rivet_blind,
    'F019': render_retaining_ring, 'F020': render_retaining_ring,
    'F021': render_retaining_ring_int, 'F022': render_retaining_ring_int,
    'F023': render_hose_clamp, 'F024': render_hose_clamp, 'F025': render_hose_clamp,
    'F026': render_hose_clamp,
    'F027': render_combination_screw, 'F028': render_f028_low_head,
    'F029': render_f029_reamed, 'F030': render_carriage,
}

# 生成 100 SVG
os.makedirs('images/per-sku', exist_ok=True)
print(f'生成 {len(RENDERERS)} 张专属 SVG...')
total_size = 0
errors = []
for sku in SKUS:
    sid = sku['id']
    if sid not in RENDERERS:
        errors.append(sid)
        continue
    try:
        svg = RENDERERS[sid](sku)
        path = f'images/per-sku/{sid}.svg'
        with open(path, 'w') as f:
            f.write(svg)
        total_size += os.path.getsize(path)
    except Exception as e:
        errors.append(f'{sid}: {e}')

print(f'✓ 完成，总大小 {total_size/1024:.1f} KB')
if errors:
    print(f'⚠️ 错误 {len(errors)}: {errors[:5]}')
