"""照片级紧固件 SVG - v3.2
- HSL 色彩空间金属渐变
- 多光源照明
- 真实摄影噪点/颗粒
- 景深模糊
- 边缘磨损/反光
- 镜面反射高光
"""

import os

# ===== 通用样式 =====
SVG_OPEN = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">'''

# 背景：摄影棚渐变 + 微噪点
BG_DEFS = '''  <defs>
    <radialGradient id="bg" cx="50%" cy="42%" r="75%">
      <stop offset="0%" stop-color="#f5f7fa"/>
      <stop offset="50%" stop-color="#e2e8f0"/>
      <stop offset="100%" stop-color="#a8b2bf"/>
    </radialGradient>
    <!-- 摄影噪点 -->
    <filter id="grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" seed="5"/>
      <feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.08 0"/>
      <feComposite in2="SourceGraphic" operator="in"/>
    </filter>
    <!-- 软景深模糊 -->
    <filter id="depthBlur">
      <feGaussianBlur stdDeviation="1.5"/>
    </filter>
    <!-- 真实阴影 -->
    <filter id="realShadow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="6"/>
      <feOffset dx="0" dy="14"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.55"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <!-- 边缘磨损 -->
    <filter id="worn">
      <feTurbulence type="turbulence" baseFrequency="0.04" numOctaves="2" seed="3"/>
      <feDisplacementMap in="SourceGraphic" scale="3"/>
    </filter>'''

# 金属渐变（更逼真 — 暗→中→亮→镜面高光→中→暗）
def metal_grad(rotation=0, base_color="#8a92a0"):
    """生成 HSL 风格的金属渐变"""
    return f'''    <linearGradient id="metal" x1="0%" y1="0%" x2="100%" y2="0%" gradientTransform="rotate({rotation})">
      <stop offset="0%" stop-color="#2a3038"/>
      <stop offset="15%" stop-color="#5a6370"/>
      <stop offset="30%" stop-color="{base_color}"/>
      <stop offset="45%" stop-color="#e8edf4"/>
      <stop offset="52%" stop-color="#ffffff" stop-opacity="0.9"/>
      <stop offset="58%" stop-color="#e8edf4"/>
      <stop offset="75%" stop-color="{base_color}"/>
      <stop offset="100%" stop-color="#2a3038"/>
    </linearGradient>'''

# 高光顶端
def top_shine():
    return '''    <linearGradient id="topShine" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.55"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>'''

# 螺纹渐变（更暗更深邃）
def thread_grad():
    return '''    <linearGradient id="thread" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1a1e25"/>
      <stop offset="50%" stop-color="#6a7280"/>
      <stop offset="100%" stop-color="#1a1e25"/>
    </linearGradient>'''

def svg_wrap(content):
    return SVG_OPEN + '\n' + BG_DEFS + '\n' + metal_grad() + '\n' + top_shine() + '\n' + thread_grad() + '\n  </defs>\n' + content + '\n</svg>'

def bg_rect():
    return '  <rect width="100%" height="100%" fill="url(#bg)"/>\n  <rect width="100%" height="100%" fill="url(#bg)" filter="url(#grain)" opacity="0.4"/>'

def shadow_ground():
    """地面投影（带模糊）"""
    return '  <ellipse cx="256" cy="460" rx="125" ry="14" fill="#000" opacity="0.35" filter="url(#depthBlur)"/>'

def thread_lines(x, y_start, count, spacing=10, color='#0a0d14'):
    """真实螺纹暗线"""
    s = ''
    for i in range(count):
        y = y_start + i * spacing
        # 主暗线
        s += f'  <line x1="{x}" y1="{y}" x2="{x+60}" y2="{y+1}" stroke="{color}" stroke-width="2" opacity="0.75"/>\n'
        # 阴影深度
        s += f'  <line x1="{x}" y1="{y+1}" x2="{x+60}" y2="{y+2}" stroke="#000" stroke-width="1" opacity="0.5"/>\n'
        # 高光
        s += f'  <line x1="{x+2}" y1="{y-1}" x2="{x+58}" y2="{y}" stroke="#fff" stroke-width="1" opacity="0.5"/>\n'
    return s

# ===== 1. 六角头螺栓（照片级）=====
def hex_bolt():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    # 螺杆（高分辨率圆柱体）
    s += '    <rect x="226" y="232" width="60" height="218" fill="url(#metal)"/>\n'
    # 顶部高光层
    s += '    <rect x="226" y="232" width="60" height="50" fill="url(#topShine)"/>\n'
    # 螺纹
    s += thread_lines(226, 244, 18, spacing=12)
    # 六角头 3D
    s += '''    <!-- 六角头侧 -->
    <polygon points="146,212 256,156 366,212 366,242 256,298 146,242" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <!-- 六角头顶 -->
    <polygon points="256,156 366,212 256,268 146,212" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.2"/>
    <!-- 顶部高光 -->
    <polygon points="256,162 360,212 256,260" fill="#fff" opacity="0.28"/>
    <polygon points="256,162 152,212 256,260" fill="#000" opacity="0.12"/>
    <!-- 边缘反光 -->
    <line x1="146" y1="212" x2="146" y2="242" stroke="#fff" stroke-width="1" opacity="0.4"/>
    <line x1="366" y1="212" x2="366" y2="242" stroke="#1a1e25" stroke-width="1" opacity="0.5"/>
  </g>'''
    # 整体噪点
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def socket_cap():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '    <rect x="226" y="262" width="60" height="186" fill="url(#metal)"/>\n'
    s += '    <rect x="226" y="262" width="60" height="40" fill="url(#topShine)"/>\n'
    s += thread_lines(226, 274, 14, spacing=12)
    # 圆柱头
    s += '''    <ellipse cx="256" cy="232" rx="82" ry="24" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.2"/>
    <rect x="174" y="232" width="164" height="24" fill="url(#metal)"/>
    <ellipse cx="256" cy="256" rx="82" ry="24" fill="#3a4250" opacity="0.7"/>
    <ellipse cx="256" cy="230" rx="82" ry="22" fill="#fff" opacity="0.25"/>
    <!-- 内六角 -->
    <ellipse cx="256" cy="228" rx="34" ry="10" fill="#0a0d14"/>
    <ellipse cx="256" cy="228" rx="34" ry="10" fill="none" stroke="#525a68" stroke-width="1.5"/>
    <polygon points="256,221 274,228 274,235 256,242 238,235 238,228" fill="none" stroke="#000" stroke-width="1.5"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def countersunk():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '    <rect x="226" y="298" width="60" height="152" fill="url(#metal)"/>\n'
    s += '    <rect x="226" y="298" width="60" height="40" fill="url(#topShine)"/>\n'
    s += thread_lines(226, 308, 12, spacing=12)
    # 沉头锥
    s += '''    <polygon points="146,200 256,295 366,200" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1"/>
    <ellipse cx="256" cy="200" rx="110" ry="24" fill="#dde3eb" stroke="#1a1e25" stroke-width="1"/>
    <ellipse cx="256" cy="198" rx="110" ry="24" fill="#fff" opacity="0.3"/>
    <line x1="256" y1="176" x2="256" y2="224" stroke="#0a0d14" stroke-width="6"/>
    <line x1="232" y1="200" x2="280" y2="200" stroke="#0a0d14" stroke-width="6"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def carriage():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '    <rect x="226" y="270" width="60" height="180" fill="url(#metal)"/>\n'
    s += '    <rect x="226" y="270" width="60" height="40" fill="url(#topShine)"/>\n'
    s += thread_lines(226, 282, 14, spacing=12)
    s += '''    <ellipse cx="256" cy="178" rx="86" ry="42" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="244" cy="166" rx="56" ry="26" fill="#fff" opacity="0.5"/>
    <rect x="220" y="212" width="72" height="58" fill="#7e8896" stroke="#1a1e25" stroke-width="1"/>
    <line x1="220" y1="212" x2="292" y2="212" stroke="#fff" stroke-width="1.5" opacity="0.5"/>
    <line x1="220" y1="270" x2="292" y2="270" stroke="#000" stroke-width="1.5" opacity="0.4"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def t_bolt():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '    <rect x="226" y="300" width="60" height="150" fill="url(#metal)"/>\n'
    s += '    <rect x="226" y="300" width="60" height="40" fill="url(#topShine)"/>\n'
    s += thread_lines(226, 312, 12, spacing=12)
    s += '''    <rect x="136" y="258" width="240" height="44" rx="6" fill="url(#metal)"/>
    <rect x="136" y="258" width="240" height="44" rx="6" fill="none" stroke="#1a1e25" stroke-width="1.2"/>
    <rect x="136" y="262" width="240" height="10" fill="#fff" opacity="0.35"/>
    <rect x="136" y="294" width="240" height="8" fill="#000" opacity="0.25"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def u_bolt():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <path d="M 180 200 Q 256 90 332 200 L 332 450 L 312 450 L 312 215 Q 256 138 200 215 L 200 450 L 180 450 Z" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>
    <line x1="180" y1="350" x2="180" y2="445" stroke="#0a0d14" stroke-width="2" opacity="0.8"/>
    <line x1="180" y1="352" x2="180" y2="445" stroke="#fff" stroke-width="1" opacity="0.5"/>
    <line x1="184" y1="354" x2="184" y2="445" stroke="#fff" stroke-width="0.5" opacity="0.4"/>
    <line x1="332" y1="350" x2="332" y2="445" stroke="#0a0d14" stroke-width="2" opacity="0.8"/>
    <line x1="332" y1="352" x2="332" y2="445" stroke="#fff" stroke-width="1" opacity="0.5"/>
    <path d="M 190 200 Q 256 108 322 200" fill="none" stroke="#fff" stroke-width="2.5" opacity="0.5"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def anchor_bolt():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <polygon points="216,160 296,160 296,260 286,290 226,290 216,260" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <polygon points="186,150 326,150 336,180 176,180" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>
    <polygon points="186,150 326,150 256,130" fill="#dde3eb" stroke="#1a1e25" stroke-width="1.2"/>
    <rect x="190" y="290" width="132" height="60" fill="#6a7280" stroke="#1a1e25" stroke-width="1.2"/>
    <rect x="190" y="290" width="132" height="6" fill="#fff" opacity="0.4"/>
    <polygon points="200,350 230,310 260,310 230,350" fill="#3a4250"/>
    <polygon points="280,350 310,310 282,310 252,350" fill="#3a4250"/>
    <polygon points="226,290 286,290 256,330" fill="#3a4250" stroke="#1a1e25" stroke-width="0.8"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def flange_bolt():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '    <rect x="226" y="280" width="60" height="170" fill="url(#metal)"/>\n'
    s += '    <rect x="226" y="280" width="60" height="40" fill="url(#topShine)"/>\n'
    s += thread_lines(226, 292, 13, spacing=12)
    s += '''    <ellipse cx="256" cy="270" rx="106" ry="22" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="256" cy="268" rx="106" ry="22" fill="url(#metal)"/>
    <ellipse cx="256" cy="268" rx="106" ry="22" fill="#fff" opacity="0.25"/>
    <ellipse cx="256" cy="255" rx="34" ry="10" fill="#0a0d14"/>
    <ellipse cx="256" cy="255" rx="34" ry="10" fill="none" stroke="#525a68" stroke-width="1.5"/>
    <polygon points="256,248 274,255 274,262 256,269 238,262 238,255" fill="none" stroke="#000" stroke-width="1.5"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def eye_bolt():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '    <rect x="226" y="280" width="60" height="170" fill="url(#metal)"/>\n'
    s += '    <rect x="226" y="280" width="60" height="40" fill="url(#topShine)"/>\n'
    s += thread_lines(226, 292, 13, spacing=12)
    s += '''    <circle cx="256" cy="180" r="80" fill="none" stroke="#3a4250" stroke-width="24"/>
    <circle cx="256" cy="180" r="80" fill="none" stroke="url(#metal)" stroke-width="20"/>
    <circle cx="256" cy="180" r="80" fill="none" stroke="#fff" stroke-width="2.5" opacity="0.5"/>
    <circle cx="256" cy="180" r="80" fill="none" stroke="#000" stroke-width="1" opacity="0.3" transform="translate(0,2)"/>
    <rect x="230" y="240" width="52" height="50" fill="url(#metal)" stroke="#1a1e25" stroke-width="1"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def wing_bolt():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '    <rect x="226" y="290" width="60" height="160" fill="url(#metal)"/>\n'
    s += '    <rect x="226" y="290" width="60" height="40" fill="url(#topShine)"/>\n'
    s += thread_lines(226, 302, 12, spacing=12)
    s += '''    <ellipse cx="116" cy="262" rx="64" ry="32" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="396" cy="262" rx="64" ry="32" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="116" cy="260" rx="64" ry="32" fill="#fff" opacity="0.2"/>
    <ellipse cx="396" cy="260" rx="64" ry="32" fill="#fff" opacity="0.2"/>
    <ellipse cx="256" cy="262" rx="42" ry="24" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="256" cy="262" rx="42" ry="24" fill="url(#metal)"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def self_tapping():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '    <polygon points="226,440 286,440 256,470" fill="#3a4250"/>\n'
    s += '    <rect x="226" y="288" width="60" height="155" fill="url(#metal)"/>\n'
    s += '    <rect x="226" y="288" width="60" height="40" fill="url(#topShine)"/>\n'
    s += thread_lines(226, 300, 12, spacing=12)
    s += '''    <ellipse cx="256" cy="238" rx="74" ry="22" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="256" cy="236" rx="74" ry="22" fill="#fff" opacity="0.3"/>
    <line x1="256" y1="218" x2="256" y2="258" stroke="#0a0d14" stroke-width="6"/>
    <line x1="232" y1="238" x2="280" y2="238" stroke="#0a0d14" stroke-width="6"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def self_drilling():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <polygon points="226,440 286,440 276,455 236,455" fill="#3a4250"/>
    <line x1="246" y1="440" x2="256" y2="470" stroke="#0a0d14" stroke-width="2.5"/>
    <line x1="266" y1="440" x2="256" y2="470" stroke="#0a0d14" stroke-width="2.5"/>
    '''
    s += '    <rect x="226" y="298" width="60" height="148" fill="url(#metal)"/>\n'
    s += '    <rect x="226" y="298" width="60" height="40" fill="url(#topShine)"/>\n'
    s += thread_lines(226, 310, 11, spacing=12)
    s += '''    <polygon points="180,250 332,250 350,275 162,275" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>
    <polygon points="180,250 332,250 256,225" fill="#dde3eb" stroke="#1a1e25" stroke-width="1.2"/>
    <polygon points="256,255 270,265 270,275 256,285 242,275 242,265" fill="#0a0d14"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

# ===== 螺母类 =====
def hex_nut():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <polygon points="100,230 256,158 412,230 256,302" fill="#3a4250" opacity="0.75"/>
    <polygon points="100,230 256,302 412,230 412,300 256,372 100,300" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>
    <polygon points="256,158 412,230 256,302 100,230" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.5"/>
    <polygon points="256,168 402,232 256,294" fill="#fff" opacity="0.3"/>
    <ellipse cx="256" cy="230" rx="42" ry="13" fill="#0a0d14"/>
    <ellipse cx="256" cy="228" rx="42" ry="11" fill="#000"/>
    <ellipse cx="256" cy="230" rx="42" ry="13" fill="none" stroke="#525a68" stroke-width="1"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def lock_nut():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <polygon points="100,220 256,148 412,220 256,292" fill="#3a4250" opacity="0.75"/>
    <polygon points="100,220 256,292 412,220 412,310 256,382 100,310" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>
    <polygon points="256,148 412,220 256,292 100,220" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.5"/>
    <ellipse cx="256" cy="220" rx="42" ry="13" fill="#1a1e25"/>
    <ellipse cx="256" cy="218" rx="42" ry="11" fill="#e0c060"/>
    <ellipse cx="256" cy="220" rx="42" ry="13" fill="none" stroke="#7a6533" stroke-width="1"/>
    <ellipse cx="256" cy="292" rx="38" ry="11" fill="#0a0d14"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def flange_nut():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <ellipse cx="256" cy="240" rx="146" ry="24" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="256" cy="238" rx="146" ry="24" fill="#fff" opacity="0.25"/>
    <polygon points="186,250 326,250 336,290 176,290" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>
    <polygon points="186,250 326,250 256,235" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="256" cy="250" rx="34" ry="11" fill="#0a0d14"/>
    <ellipse cx="256" cy="248" rx="34" ry="9" fill="#000"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def cap_nut():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <polygon points="100,240 256,168 412,240 256,312" fill="#3a4250" opacity="0.75"/>
    <polygon points="100,240 256,312 412,240 412,310 256,382 100,310" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>
    <polygon points="256,168 412,240 256,312 100,240" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.5"/>
    <ellipse cx="256" cy="170" rx="156" ry="36" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>
    <ellipse cx="256" cy="166" rx="156" ry="36" fill="#fff" opacity="0.32"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def square_nut():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <polygon points="100,230 256,168 412,230 256,292" fill="#3a4250" opacity="0.75"/>
    <polygon points="100,230 256,292 412,230 412,320 256,382 100,320" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>
    <polygon points="256,168 412,230 256,292 100,230" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.5"/>
    <ellipse cx="256" cy="230" rx="42" ry="13" fill="#0a0d14"/>
    <ellipse cx="256" cy="228" rx="42" ry="11" fill="#000"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def wing_nut():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <ellipse cx="116" cy="260" rx="64" ry="32" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="396" cy="260" rx="64" ry="32" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="116" cy="258" rx="64" ry="32" fill="#fff" opacity="0.2"/>
    <ellipse cx="396" cy="258" rx="64" ry="32" fill="#fff" opacity="0.2"/>
    <ellipse cx="256" cy="260" rx="52" ry="28" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="256" cy="258" rx="52" ry="28" fill="url(#metal)"/>
    <ellipse cx="256" cy="258" rx="22" ry="9" fill="#0a0d14"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def t_slot_nut():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <rect x="146" y="218" width="220" height="86" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>
    <rect x="146" y="218" width="220" height="8" fill="#fff" opacity="0.4"/>
    <rect x="146" y="298" width="220" height="6" fill="#000" opacity="0.35"/>
    <ellipse cx="256" cy="260" rx="38" ry="13" fill="#0a0d14"/>
    <ellipse cx="256" cy="258" rx="38" ry="11" fill="#000"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def weld_nut():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <polygon points="100,240 256,168 412,240 256,312" fill="#3a4250" opacity="0.75"/>
    <polygon points="100,240 256,312 412,240 412,300 256,372 100,300" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>
    <polygon points="256,168 412,240 256,312 100,240" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.5"/>
    <circle cx="170" cy="320" r="11" fill="#3a4250"/>
    <circle cx="342" cy="320" r="11" fill="#3a4250"/>
    <circle cx="170" cy="278" r="11" fill="#3a4250"/>
    <circle cx="342" cy="278" r="11" fill="#3a4250"/>
    <ellipse cx="256" cy="240" rx="42" ry="13" fill="#0a0d14"/>
    <ellipse cx="256" cy="238" rx="42" ry="11" fill="#000"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def rivet_nut():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <ellipse cx="256" cy="200" rx="106" ry="24" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>
    <rect x="150" y="200" width="212" height="120" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="256" cy="320" rx="106" ry="24" fill="#3a4250" opacity="0.85"/>
'''
    for i in range(8):
        y = 210 + i * 14
        s += f'    <line x1="150" y1="{y}" x2="362" y2="{y+2}" stroke="#0a0d14" stroke-width="1.5" opacity="0.6"/>\n'
    s += '''    <ellipse cx="256" cy="200" rx="32" ry="9" fill="#0a0d14"/>
    <ellipse cx="256" cy="199" rx="32" ry="7" fill="#000"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

# ===== 螺杆 =====
def threaded_rod():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '    <rect x="216" y="116" width="80" height="330" fill="url(#metal)"/>\n'
    s += '    <rect x="216" y="116" width="80" height="50" fill="url(#topShine)"/>\n'
    s += thread_lines(216, 126, 26, spacing=12)
    s += '  </g>'
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def stud_1end():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '    <rect x="226" y="148" width="60" height="110" fill="url(#metal)"/>\n'
    s += '    <rect x="226" y="148" width="60" height="40" fill="url(#topShine)"/>\n'
    s += '    <rect x="226" y="258" width="60" height="195" fill="url(#metal)"/>\n'
    s += thread_lines(226, 270, 15, spacing=12)
    s += '<polygon points="226,148 286,148 256,132" fill="#3a4250"/>\n  </g>'
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def stud_2end():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '    <rect x="226" y="116" width="60" height="105" fill="url(#metal)"/>\n'
    s += '    <rect x="226" y="116" width="60" height="40" fill="url(#topShine)"/>\n'
    s += thread_lines(226, 126, 8, spacing=12)
    s += '    <rect x="226" y="222" width="60" height="86" fill="url(#metal)"/>\n'
    s += '    <rect x="226" y="308" width="60" height="138" fill="url(#metal)"/>\n'
    s += thread_lines(226, 318, 10, spacing=12)
    s += '  </g>'
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

# ===== 紧固件 =====
def flat_washer():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <ellipse cx="256" cy="220" rx="178" ry="40" fill="url(#metal)" stroke="#1a1e25" stroke-width="2"/>
    <ellipse cx="256" cy="218" rx="178" ry="40" fill="#fff" opacity="0.25"/>
    <ellipse cx="256" cy="290" rx="178" ry="40" fill="#3a4250" opacity="0.7"/>
    <rect x="78" y="220" width="356" height="70" fill="url(#metal)"/>
    <line x1="78" y1="220" x2="434" y2="220" stroke="#fff" stroke-width="2" opacity="0.5"/>
    <line x1="78" y1="290" x2="434" y2="290" stroke="#000" stroke-width="2" opacity="0.4"/>
    <ellipse cx="256" cy="256" rx="86" ry="15" fill="#0a0d14"/>
    <ellipse cx="256" cy="254" rx="86" ry="13" fill="#000"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def spring_washer():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <path d="M 256 130 A 130 130 0 1 1 220 250 L 256 130 Z" fill="url(#metal)" stroke="#1a1e25" stroke-width="2"/>
    <path d="M 256 130 A 130 130 0 0 1 380 220 L 220 250 L 256 130 Z" fill="#a8b3c0" opacity="0.45"/>
    <ellipse cx="256" cy="256" rx="106" ry="24" fill="url(#metal)"/>
    <ellipse cx="256" cy="254" rx="106" ry="22" fill="#fff" opacity="0.2"/>
    <line x1="220" y1="250" x2="256" y2="130" stroke="#0a0d14" stroke-width="2.5"/>
    <ellipse cx="256" cy="256" rx="64" ry="13" fill="#0a0d14"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def cotter_pin():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <rect x="246" y="100" width="20" height="280" fill="url(#metal)" stroke="#1a1e25" stroke-width="1"/>
    <ellipse cx="256" cy="100" rx="10" ry="14" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1"/>
    <polygon points="246,380 256,440 266,380" fill="#3a4250"/>
    <line x1="256" y1="350" x2="256" y2="430" stroke="#0a0d14" stroke-width="2.5"/>
    <ellipse cx="256" cy="100" rx="14" ry="18" fill="none" stroke="#3a4250" stroke-width="6"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def spring_pin():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <rect x="216" y="180" width="80" height="220" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>
'''
    for i in range(9):
        y = 200 + i * 22
        s += f'    <line x1="216" y1="{y}" x2="296" y2="{y}" stroke="#0a0d14" stroke-width="1.8" opacity="0.7"/>\n'
    s += '''    <ellipse cx="256" cy="180" rx="40" ry="12" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="256" cy="400" rx="40" ry="12" fill="#3a4250" stroke="#1a1e25" stroke-width="1.2"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def dowel_pin():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <rect x="226" y="120" width="60" height="320" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="256" cy="120" rx="30" ry="10" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1"/>
    <ellipse cx="256" cy="440" rx="30" ry="10" fill="#3a4250" stroke="#1a1e25" stroke-width="1"/>
    <line x1="226" y1="120" x2="286" y2="120" stroke="#fff" stroke-width="2.5" opacity="0.5"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def rivet_round():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <ellipse cx="256" cy="200" rx="52" ry="52" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="244" cy="186" rx="24" ry="24" fill="#fff" opacity="0.55"/>
    <rect x="226" y="240" width="60" height="160" fill="url(#metal)"/>
    <ellipse cx="256" cy="400" rx="40" ry="14" fill="#3a4250" stroke="#1a1e25" stroke-width="1"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def rivet_csk():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <polygon points="206,220 256,160 306,220" fill="url(#metal)" stroke="#1a1e25" stroke-width="1"/>
    <ellipse cx="256" cy="220" rx="52" ry="15" fill="url(#metal)" stroke="#1a1e25" stroke-width="1"/>
    <ellipse cx="256" cy="218" rx="52" ry="15" fill="#fff" opacity="0.3"/>
    <rect x="226" y="234" width="60" height="170" fill="url(#metal)"/>
    <ellipse cx="256" cy="404" rx="40" ry="14" fill="#3a4250" stroke="#1a1e25" stroke-width="1"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def rivet_blind():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <ellipse cx="256" cy="170" rx="52" ry="52" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="244" cy="158" rx="24" ry="24" fill="#fff" opacity="0.55"/>
    <rect x="226" y="200" width="60" height="100" fill="url(#metal)" stroke="#1a1e25" stroke-width="1"/>
    <ellipse cx="256" cy="300" rx="38" ry="13" fill="#3a4250" stroke="#1a1e25" stroke-width="1"/>
    <rect x="252" y="310" width="8" height="120" fill="#7e8896" stroke="#1a1e25" stroke-width="0.5"/>
    <circle cx="256" cy="430" r="8" fill="#a8b3c0" stroke="#1a1e25" stroke-width="0.5"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def retaining_ext():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <path d="M 100 256 Q 100 130 256 130 Q 412 130 412 256 Q 412 290 380 280 L 380 256 Q 380 170 256 170 Q 132 170 132 256 L 132 280 Q 100 290 100 256 Z" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>
    <ellipse cx="256" cy="256" rx="120" ry="26" fill="#0a0d14"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def retaining_int():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <path d="M 100 256 Q 100 130 256 130 Q 412 130 412 256 Q 412 290 380 280 L 380 256 Q 380 170 256 170 Q 132 170 132 256 L 132 280 Q 100 290 100 256 Z" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5" transform="scale(-1,1) translate(-512,0)"/>
    <ellipse cx="256" cy="256" rx="120" ry="26" fill="#0a0d14"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def hose_clamp():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <ellipse cx="256" cy="256" rx="160" ry="160" fill="none" stroke="url(#metal)" stroke-width="22"/>
    <ellipse cx="256" cy="256" rx="160" ry="160" fill="none" stroke="#fff" stroke-width="2.5" opacity="0.4"/>
    <rect x="216" y="80" width="80" height="50" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.5"/>
    <circle cx="256" cy="90" r="13" fill="#0a0d14"/>
    <line x1="249" y1="83" x2="263" y2="97" stroke="#fff" stroke-width="2"/>
    <line x1="263" y1="83" x2="249" y2="97" stroke="#fff" stroke-width="2"/>
    <rect x="246" y="40" width="20" height="40" fill="url(#metal)"/>
  </g>'''
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

def combo_screw():
    s = bg_rect() + '\n' + shadow_ground() + '\n'
    s += '  <g filter="url(#realShadow)">\n'
    s += '''    <ellipse cx="256" cy="240" rx="106" ry="20" fill="url(#metal)" stroke="#1a1e25" stroke-width="1.2"/>
    <ellipse cx="256" cy="238" rx="106" ry="20" fill="#fff" opacity="0.25"/>
    <rect x="150" y="240" width="212" height="20" fill="url(#metal)"/>
    <polygon points="206,200 306,200 316,230 196,230" fill="#a8b3c0" stroke="#1a1e25" stroke-width="1.2"/>
    <polygon points="206,200 306,200 256,185" fill="#c8d0dc" stroke="#1a1e25" stroke-width="1.2"/>
    <polygon points="256,210 270,220 270,230 256,240 242,230 242,220" fill="#0a0d14"/>
    <rect x="226" y="260" width="60" height="190" fill="url(#metal)"/>
'''
    s += thread_lines(226, 272, 14, spacing=12)
    s += '  </g>'
    s += '\n  <rect width="100%" height="100%" fill="#000" filter="url(#grain)" opacity="0.3" pointer-events="none"/>'
    return svg_wrap(s)

# ===== 批量生成 =====
BOLTS = {
    'hex-bolt': hex_bolt, 'socket-cap': socket_cap, 'countersunk-socket': countersunk,
    'carriage-bolt': carriage, 't-bolt': t_bolt, 'u-bolt': u_bolt,
    'anchor-bolt': anchor_bolt, 'flange-bolt': flange_bolt, 'eye-bolt': eye_bolt,
    'wing-bolt': wing_bolt, 'self-tapping': self_tapping, 'self-drilling': self_drilling,
}
NUTS = {
    'hex-nut': hex_nut, 'lock-nut': lock_nut, 'flange-nut': flange_nut,
    'cap-nut': cap_nut, 'square-nut': square_nut, 'wing-nut': wing_nut,
    't-slot-nut': t_slot_nut, 'weld-nut': weld_nut, 'rivet-nut': rivet_nut,
}
RODS = {
    'threaded-rod': threaded_rod, 'stud-bolt-1end': stud_1end, 'stud-bolt-2end': stud_2end,
}
MISC = {
    'flat-washer': flat_washer, 'spring-washer': spring_washer, 'cotter-pin': cotter_pin,
    'spring-pin': spring_pin, 'dowel-pin': dowel_pin, 'rivet-round': rivet_round,
    'rivet-csk': rivet_csk, 'rivet-blind': rivet_blind, 'retaining-ring-ext': retaining_ext,
    'retaining-ring-int': retaining_int, 'hose-clamp': hose_clamp, 'combination-screw': combo_screw,
}
ALL = {}
ALL.update(BOLTS); ALL.update(NUTS); ALL.update(RODS); ALL.update(MISC)

print(f'生成 {len(ALL)} 张照片级 SVG...')
for name, func in ALL.items():
    svg = func()
    with open(f'images/{name}.svg', 'w') as f:
        f.write(svg)
total = sum(os.path.getsize(f'images/{f}') for f in os.listdir('images') if f.endswith('.svg'))
print(f'✓ 全部生成完成，总大小 {total/1024:.1f} KB')
