"""超逼真紧固件产品图生成器 - 干净写法，无 f-string 嵌套"""
import math

# ===== 通用 SVG 元素 =====
BG_GRADIENT = '''<defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="70%">
      <stop offset="0%" stop-color="#f6f8fb"/>
      <stop offset="100%" stop-color="#b8c2cf"/>
    </radialGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg)"/>'''

DS_FILTER = '''<filter id="ds" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="4"/>
      <feOffset dx="0" dy="10"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.4"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>'''

# 金属主渐变（横向，圆柱体）
SHAFT_GRADIENT = '''<linearGradient id="shaft" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3a4250"/>
      <stop offset="25%" stop-color="#7e8896"/>
      <stop offset="50%" stop-color="#e0e6ee"/>
      <stop offset="75%" stop-color="#7e8896"/>
      <stop offset="100%" stop-color="#3a4250"/>
    </linearGradient>'''

def svg_wrap(content, w=512, h=512):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + str(w) + ' ' + str(h) + '" width="' + str(w) + '" height="' + str(h) + '">\n'
            + BG_GRADIENT + '\n' + DS_FILTER + '\n' + SHAFT_GRADIENT + '\n' + content + '\n</svg>')

def thread_lines(x1, y_start, count, spacing=12, color='#2a3038', width=1.5, opacity=0.65, slant=2):
    """生成螺纹暗线"""
    s = ''
    for i in range(count):
        y = y_start + i * spacing
        s += '  <line x1="' + str(x1) + '" y1="' + str(y) + '" x2="' + str(x1 + 60) + '" y2="' + str(y + slant) + '" stroke="' + color + '" stroke-width="' + str(width) + '" opacity="' + str(opacity) + '"/>\n'
    return s

def thread_highlights(x1, y_start, count, spacing=12, color='#fff', width=0.8, opacity=0.35, slant=2):
    """生成螺纹高光线"""
    s = ''
    for i in range(count):
        y = y_start + 2 + i * spacing
        s += '  <line x1="' + str(x1 + 4) + '" y1="' + str(y) + '" x2="' + str(x1 + 56) + '" y2="' + str(y + slant) + '" stroke="' + color + '" stroke-width="' + str(width) + '" opacity="' + str(opacity) + '"/>\n'
    return s

def shadow_ellipse():
    return '<ellipse cx="256" cy="455" rx="115" ry="14" fill="#000" opacity="0.25" filter="url(#ds)"/>'

# ===== 各类型螺栓 =====

def hex_bolt():
    """六角头螺栓"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    # 螺杆
    body += '  <rect x="226" y="240" width="60" height="205" fill="url(#shaft)"/>\n'
    # 螺纹
    body += thread_lines(226, 252, 16)
    body += thread_highlights(226, 252, 16)
    
    # 六角头 3D 透视
    body += '''  <!-- 六角头 3D -->
  <polygon points="156,210 256,160 356,210 256,260" fill="#3a4250" opacity="0.85"/>
  <polygon points="156,210 256,260 356,210 356,238 256,288 156,238" fill="#a8b3c0" stroke="#2a3038" stroke-width="1.2"/>
  <polygon points="256,160 356,210 256,260 156,210" fill="#c8d0dc" stroke="#2a3038" stroke-width="1.2"/>
  <polygon points="256,166 348,212 256,254" fill="#fff" opacity="0.22"/>
  <polygon points="256,166 164,212 256,254" fill="#000" opacity="0.10"/>
</g>'''
    return svg_wrap(body)

def socket_cap():
    """内六角圆柱头"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '  <rect x="226" y="260" width="60" height="185" fill="url(#shaft)"/>\n'
    body += thread_lines(226, 272, 14)
    body += thread_highlights(226, 272, 14)
    # 圆柱头
    body += '''  <ellipse cx="256" cy="232" rx="78" ry="22" fill="#dde3eb" stroke="#3a4250" stroke-width="1"/>
  <rect x="178" y="232" width="156" height="22" fill="url(#shaft)"/>
  <ellipse cx="256" cy="254" rx="78" ry="22" fill="#424956" opacity="0.6"/>
  <ellipse cx="256" cy="230" rx="78" ry="20" fill="#fff" opacity="0.18"/>
  <!-- 六角凹孔 -->
  <ellipse cx="256" cy="228" rx="32" ry="10" fill="#1a1e25"/>
  <ellipse cx="256" cy="228" rx="32" ry="10" fill="none" stroke="#525a68" stroke-width="1.5"/>
  <polygon points="256,222 272,228 272,234 256,240 240,234 240,228" fill="none" stroke="#0a0d14" stroke-width="1.2"/>
</g>'''
    return svg_wrap(body)

def countersunk():
    """沉头"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    # 螺杆
    body += '  <rect x="226" y="295" width="60" height="155" fill="url(#shaft)"/>\n'
    body += thread_lines(226, 305, 12)
    body += thread_highlights(226, 305, 12)
    # 沉头
    body += '''  <polygon points="156,200 256,295 356,200" fill="#a8b3c0" stroke="#3a4250" stroke-width="1"/>
  <ellipse cx="256" cy="200" rx="100" ry="22" fill="#dde3eb" stroke="#3a4250" stroke-width="1"/>
  <ellipse cx="256" cy="200" rx="100" ry="22" fill="#fff" opacity="0.2"/>
  <line x1="256" y1="178" x2="256" y2="222" stroke="#1a1e25" stroke-width="5"/>
  <line x1="234" y1="200" x2="278" y2="200" stroke="#1a1e25" stroke-width="5"/>
</g>'''
    return svg_wrap(body)

def carriage():
    """马车螺栓（圆头方颈）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '  <rect x="226" y="270" width="60" height="180" fill="url(#shaft)"/>\n'
    body += thread_lines(226, 280, 14)
    body += thread_highlights(226, 280, 14)
    body += '''  <ellipse cx="256" cy="178" rx="80" ry="40" fill="#a8b3c0" stroke="#2a3038" stroke-width="1"/>
  <ellipse cx="246" cy="166" rx="50" ry="22" fill="#fff" opacity="0.4"/>
  <rect x="220" y="212" width="72" height="58" fill="#7e8896" stroke="#2a3038" stroke-width="1"/>
  <line x1="220" y1="212" x2="292" y2="212" stroke="#fff" stroke-width="1.2" opacity="0.4"/>
</g>'''
    return svg_wrap(body)

def t_bolt():
    """T 型螺栓"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '  <rect x="226" y="300" width="60" height="150" fill="url(#shaft)"/>\n'
    body += thread_lines(226, 312, 12)
    body += thread_highlights(226, 312, 12)
    body += '''  <!-- T 型头 -->
  <rect x="146" y="260" width="220" height="40" rx="6" fill="url(#shaft)"/>
  <rect x="146" y="260" width="220" height="40" rx="6" fill="none" stroke="#2a3038" stroke-width="1"/>
  <rect x="146" y="262" width="220" height="8" fill="#fff" opacity="0.25"/>
  <rect x="146" y="290" width="220" height="8" fill="#000" opacity="0.2"/>
</g>'''
    return svg_wrap(body)

def u_bolt():
    """U 型螺栓"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <!-- U 型：两个杆 + 弧顶 -->
  <path d="M 180 200 Q 256 100 332 200 L 332 450 L 312 450 L 312 215 Q 256 145 200 215 L 200 450 L 180 450 Z" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.5"/>
  <!-- 螺纹 -->
  <line x1="180" y1="350" x2="180" y2="445" stroke="#2a3038" stroke-width="1.5" opacity="0.7"/>
  <line x1="180" y1="352" x2="180" y2="445" stroke="#fff" stroke-width="0.8" opacity="0.4"/>
  <line x1="184" y1="354" x2="184" y2="445" stroke="#fff" stroke-width="0.5" opacity="0.5"/>
  <line x1="332" y1="350" x2="332" y2="445" stroke="#2a3038" stroke-width="1.5" opacity="0.7"/>
  <line x1="332" y1="352" x2="332" y2="445" stroke="#fff" stroke-width="0.8" opacity="0.4"/>
  <line x1="328" y1="354" x2="328" y2="445" stroke="#fff" stroke-width="0.5" opacity="0.5"/>
  <!-- 顶部高光 -->
  <path d="M 190 200 Q 256 115 322 200" fill="none" stroke="#fff" stroke-width="2" opacity="0.4"/>
</g>'''
    return svg_wrap(body)

def anchor_bolt():
    """膨胀/锚栓（带套筒）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <!-- 锚栓主体（锥形） -->
  <polygon points="216,160 296,160 296,260 286,290 226,290 216,260" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.2"/>
  <rect x="216" y="160" width="80" height="100" fill="url(#shaft)"/>
  <!-- 顶部螺母 -->
  <polygon points="186,150 326,150 336,180 176,180" fill="#a8b3c0" stroke="#2a3038" stroke-width="1.2"/>
  <polygon points="186,150 326,150 256,130" fill="#c8d0dc" stroke="#2a3038" stroke-width="1.2"/>
  <!-- 套筒 -->
  <rect x="190" y="290" width="132" height="60" fill="#6a7280" stroke="#2a3038" stroke-width="1.2"/>
  <rect x="190" y="290" width="132" height="6" fill="#fff" opacity="0.3"/>
  <!-- 楔形夹片 -->
  <polygon points="200,350 230,310 260,310 230,350" fill="#3a4250"/>
  <polygon points="280,350 310,310 282,310 252,350" fill="#3a4250"/>
  <!-- 锥形尖端 -->
  <polygon points="226,290 286,290 256,330" fill="#3a4250" stroke="#2a3038" stroke-width="0.8"/>
</g>'''
    return svg_wrap(body)

def flange_bolt():
    """法兰螺栓（带垫圈头）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '  <rect x="226" y="280" width="60" height="170" fill="url(#shaft)"/>\n'
    body += thread_lines(226, 292, 13)
    body += thread_highlights(226, 292, 13)
    # 法兰头（圆形 + 内六角）
    body += '''  <!-- 法兰盘 -->
  <ellipse cx="256" cy="270" rx="100" ry="20" fill="#a8b3c0" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="256" cy="268" rx="100" ry="20" fill="url(#shaft)"/>
  <ellipse cx="256" cy="268" rx="100" ry="20" fill="#fff" opacity="0.18"/>
  <!-- 内六角 -->
  <ellipse cx="256" cy="255" rx="32" ry="10" fill="#1a1e25"/>
  <ellipse cx="256" cy="255" rx="32" ry="10" fill="none" stroke="#525a68" stroke-width="1.5"/>
  <polygon points="256,249 272,255 272,261 256,267 240,261 240,255" fill="none" stroke="#0a0d14" stroke-width="1.2"/>
</g>'''
    return svg_wrap(body)

def eye_bolt():
    """吊环螺栓（环形头）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '  <rect x="226" y="280" width="60" height="170" fill="url(#shaft)"/>\n'
    body += thread_lines(226, 292, 13)
    body += thread_highlights(226, 292, 13)
    # 吊环
    body += '''  <circle cx="256" cy="180" r="80" fill="none" stroke="#3a4250" stroke-width="22" stroke-linecap="round"/>
  <circle cx="256" cy="180" r="80" fill="none" stroke="url(#shaft)" stroke-width="18" stroke-linecap="round"/>
  <circle cx="256" cy="180" r="80" fill="none" stroke="#fff" stroke-width="2" opacity="0.4"/>
  <!-- 杆连接处 -->
  <rect x="230" y="240" width="52" height="50" fill="url(#shaft)" stroke="#2a3038" stroke-width="1"/>
</g>'''
    return svg_wrap(body)

def wing_bolt():
    """翼型螺栓（蝴蝶头）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '  <rect x="226" y="290" width="60" height="160" fill="url(#shaft)"/>\n'
    body += thread_lines(226, 302, 12)
    body += thread_highlights(226, 302, 12)
    # 翼
    body += '''  <!-- 左右翼 -->
  <ellipse cx="120" cy="260" rx="60" ry="30" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="392" cy="260" rx="60" ry="30" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="120" cy="260" rx="60" ry="30" fill="#fff" opacity="0.15"/>
  <ellipse cx="392" cy="260" rx="60" ry="30" fill="#fff" opacity="0.15"/>
  <!-- 中心圆 -->
  <ellipse cx="256" cy="260" rx="40" ry="22" fill="#a8b3c0" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="256" cy="260" rx="40" ry="22" fill="url(#shaft)"/>
</g>'''
    return svg_wrap(body)

def self_tapping():
    """自攻螺丝"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    # 尖头
    body += '  <polygon points="226,440 286,440 256,470" fill="#3a4250"/>\n'
    body += '  <rect x="226" y="290" width="60" height="155" fill="url(#shaft)"/>\n'
    body += thread_lines(226, 300, 12)
    body += thread_highlights(226, 300, 12)
    # 盘头 + 十字
    body += '''  <ellipse cx="256" cy="240" rx="70" ry="20" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="256" cy="238" rx="70" ry="20" fill="#fff" opacity="0.2"/>
  <line x1="256" y1="222" x2="256" y2="258" stroke="#1a1e25" stroke-width="5"/>
  <line x1="234" y1="240" x2="278" y2="240" stroke="#1a1e25" stroke-width="5"/>
</g>'''
    return svg_wrap(body)

def self_drilling():
    """自钻螺丝（带钻尾）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    # 钻尾（带凹槽）
    body += '''  <polygon points="226,440 286,440 276,455 236,455" fill="#3a4250"/>
  <line x1="246" y1="440" x2="256" y2="470" stroke="#1a1e25" stroke-width="2"/>
  <line x1="266" y1="440" x2="256" y2="470" stroke="#1a1e25" stroke-width="2"/>
'''
    body += '  <rect x="226" y="300" width="60" height="145" fill="url(#shaft)"/>\n'
    body += thread_lines(226, 310, 11)
    body += thread_highlights(226, 310, 11)
    # 六角垫圈头
    body += '''  <polygon points="180,250 332,250 350,275 162,275" fill="#a8b3c0" stroke="#2a3038" stroke-width="1.2"/>
  <polygon points="180,250 332,250 256,225" fill="#dde3eb" stroke="#2a3038" stroke-width="1.2"/>
  <polygon points="180,250 332,250 256,275" fill="#3a4250" opacity="0.3"/>
  <polygon points="256,255 270,265 270,275 256,285 242,275 242,265" fill="#1a1e25"/>
</g>'''
    return svg_wrap(body)

# ===== 螺母类 =====

def hex_nut():
    """六角螺母"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <!-- 六角螺母 3D -->
  <polygon points="106,230 256,160 406,230 256,300" fill="#3a4250" opacity="0.7"/>
  <polygon points="106,230 256,300 406,230 406,300 256,370 106,300" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.5"/>
  <polygon points="256,160 406,230 256,300 106,230" fill="#c8d0dc" stroke="#2a3038" stroke-width="1.5"/>
  <polygon points="256,170 396,232 256,294" fill="#fff" opacity="0.25"/>
  <!-- 中心螺孔 -->
  <ellipse cx="256" cy="230" rx="40" ry="12" fill="#1a1e25"/>
  <ellipse cx="256" cy="228" rx="40" ry="10" fill="#0a0d14"/>
  <ellipse cx="256" cy="230" rx="40" ry="12" fill="none" stroke="#525a68" stroke-width="1"/>
</g>'''
    return svg_wrap(body)

def lock_nut():
    """锁紧螺母（带尼龙圈）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <polygon points="106,220 256,150 406,220 256,290" fill="#3a4250" opacity="0.7"/>
  <polygon points="106,220 256,290 406,220 406,310 256,380 106,310" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.5"/>
  <polygon points="256,150 406,220 256,290 106,220" fill="#c8d0dc" stroke="#2a3038" stroke-width="1.5"/>
  <!-- 顶部尼龙圈（黄色） -->
  <ellipse cx="256" cy="220" rx="40" ry="12" fill="#1a1e25"/>
  <ellipse cx="256" cy="218" rx="40" ry="10" fill="#e0c060"/>
  <ellipse cx="256" cy="220" rx="40" ry="12" fill="none" stroke="#7a6533" stroke-width="1"/>
  <!-- 底部螺纹指示 -->
  <ellipse cx="256" cy="290" rx="36" ry="10" fill="#1a1e25"/>
</g>'''
    return svg_wrap(body)

def flange_nut():
    """法兰螺母"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <!-- 法兰盘 -->
  <ellipse cx="256" cy="240" rx="140" ry="22" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="256" cy="238" rx="140" ry="22" fill="#fff" opacity="0.18"/>
  <!-- 六角主体 -->
  <polygon points="186,250 326,250 336,290 176,290" fill="#a8b3c0" stroke="#2a3038" stroke-width="1.2"/>
  <polygon points="186,250 326,250 256,235" fill="#c8d0dc" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="256" cy="250" rx="32" ry="10" fill="#1a1e25"/>
  <ellipse cx="256" cy="248" rx="32" ry="8" fill="#0a0d14"/>
</g>'''
    return svg_wrap(body)

def cap_nut():
    """盖帽螺母（球面封顶）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <polygon points="106,240 256,170 406,240 256,310" fill="#3a4250" opacity="0.7"/>
  <polygon points="106,240 256,310 406,240 406,310 256,380 106,310" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.5"/>
  <polygon points="256,170 406,240 256,310 106,240" fill="#c8d0dc" stroke="#2a3038" stroke-width="1.5"/>
  <polygon points="256,180 396,242 256,302" fill="#fff" opacity="0.3"/>
  <!-- 圆顶封盖 -->
  <ellipse cx="256" cy="170" rx="150" ry="34" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.5"/>
  <ellipse cx="256" cy="166" rx="150" ry="34" fill="#fff" opacity="0.25"/>
</g>'''
    return svg_wrap(body)

def square_nut():
    """方形螺母"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <polygon points="106,230 256,170 406,230 256,290" fill="#3a4250" opacity="0.7"/>
  <polygon points="106,230 256,290 406,230 406,320 256,380 106,320" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.5"/>
  <polygon points="256,170 406,230 256,290 106,230" fill="#c8d0dc" stroke="#2a3038" stroke-width="1.5"/>
  <ellipse cx="256" cy="230" rx="40" ry="12" fill="#1a1e25"/>
  <ellipse cx="256" cy="228" rx="40" ry="10" fill="#0a0d14"/>
</g>'''
    return svg_wrap(body)

def wing_nut():
    """翼型螺母"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <ellipse cx="120" cy="260" rx="60" ry="30" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="392" cy="260" rx="60" ry="30" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="120" cy="260" rx="60" ry="30" fill="#fff" opacity="0.15"/>
  <ellipse cx="392" cy="260" rx="60" ry="30" fill="#fff" opacity="0.15"/>
  <ellipse cx="256" cy="260" rx="50" ry="26" fill="#a8b3c0" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="256" cy="258" rx="50" ry="26" fill="url(#shaft)"/>
  <ellipse cx="256" cy="258" rx="20" ry="8" fill="#1a1e25"/>
</g>'''
    return svg_wrap(body)

def t_slot_nut():
    """T 型槽螺母"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <rect x="156" y="220" width="200" height="80" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.5"/>
  <rect x="156" y="220" width="200" height="6" fill="#fff" opacity="0.3"/>
  <rect x="156" y="295" width="200" height="6" fill="#000" opacity="0.3"/>
  <!-- 中心螺孔 -->
  <ellipse cx="256" cy="260" rx="36" ry="12" fill="#1a1e25"/>
  <ellipse cx="256" cy="258" rx="36" ry="10" fill="#0a0d14"/>
</g>'''
    return svg_wrap(body)

def weld_nut():
    """焊接螺母（带凸点）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <polygon points="106,240 256,170 406,240 256,310" fill="#3a4250" opacity="0.7"/>
  <polygon points="106,240 256,310 406,240 406,300 256,370 106,300" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.5"/>
  <polygon points="256,170 406,240 256,310 106,240" fill="#c8d0dc" stroke="#2a3038" stroke-width="1.5"/>
  <!-- 焊接凸点（4 个） -->
  <circle cx="170" cy="320" r="10" fill="#3a4250"/>
  <circle cx="342" cy="320" r="10" fill="#3a4250"/>
  <circle cx="170" cy="280" r="10" fill="#3a4250"/>
  <circle cx="342" cy="280" r="10" fill="#3a4250"/>
  <ellipse cx="256" cy="240" rx="40" ry="12" fill="#1a1e25"/>
  <ellipse cx="256" cy="238" rx="40" ry="10" fill="#0a0d14"/>
</g>'''
    return svg_wrap(body)

def rivet_nut():
    """拉铆螺母"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <!-- 圆筒形 -->
  <ellipse cx="256" cy="200" rx="100" ry="22" fill="#a8b3c0" stroke="#2a3038" stroke-width="1.2"/>
  <rect x="156" y="200" width="200" height="120" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="256" cy="320" rx="100" ry="22" fill="#3a4250" opacity="0.85"/>
  <!-- 螺纹刻线 -->
'''
    for i in range(8):
        y = 210 + i * 14
        body += '  <line x1="156" y1="' + str(y) + '" x2="356" y2="' + str(y + 2) + '" stroke="#1a1e25" stroke-width="1.2" opacity="0.5"/>\n'
    body += '''  <!-- 顶面螺孔 -->
  <ellipse cx="256" cy="200" rx="30" ry="8" fill="#1a1e25"/>
  <ellipse cx="256" cy="199" rx="30" ry="6" fill="#0a0d14"/>
</g>'''
    return svg_wrap(body)

# ===== 螺杆类 =====

def threaded_rod():
    """全螺纹螺杆"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '  <rect x="216" y="120" width="80" height="320" fill="url(#shaft)"/>\n'
    # 大量螺纹
    body += thread_lines(216, 130, 26)
    body += thread_highlights(216, 130, 26)
    body += '  <rect x="220" y="120" width="72" height="40" fill="#fff" opacity="0.15"/>\n'
    body += '</g>'
    return svg_wrap(body)

def stud_1end():
    """单头螺柱"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    # 上部无螺纹（光杆）
    body += '  <rect x="226" y="150" width="60" height="100" fill="url(#shaft)"/>\n'
    # 下部螺纹
    body += '  <rect x="226" y="260" width="60" height="190" fill="url(#shaft)"/>\n'
    body += thread_lines(226, 270, 15)
    body += thread_highlights(226, 270, 15)
    # 倒角
    body += '<polygon points="226,150 286,150 256,135" fill="#3a4250"/>\n'
    body += '</g>'
    return svg_wrap(body)

def stud_2end():
    """双头螺柱"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    # 上部螺纹
    body += '  <rect x="226" y="120" width="60" height="100" fill="url(#shaft)"/>\n'
    body += thread_lines(226, 130, 8)
    body += thread_highlights(226, 130, 8)
    # 中间光杆
    body += '  <rect x="226" y="225" width="60" height="80" fill="url(#shaft)"/>\n'
    # 下部螺纹
    body += '  <rect x="226" y="310" width="60" height="130" fill="url(#shaft)"/>\n'
    body += thread_lines(226, 320, 10)
    body += thread_highlights(226, 320, 10)
    body += '</g>'
    return svg_wrap(body)

# ===== 紧固件类 =====

def flat_washer():
    """平垫圈"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <!-- 平垫圈：圆环 3D -->
  <ellipse cx="256" cy="220" rx="170" ry="38" fill="url(#shaft)" stroke="#2a3038" stroke-width="2"/>
  <ellipse cx="256" cy="218" rx="170" ry="38" fill="#fff" opacity="0.2"/>
  <ellipse cx="256" cy="290" rx="170" ry="38" fill="#3a4250" opacity="0.6"/>
  <rect x="86" y="220" width="340" height="70" fill="url(#shaft)"/>
  <line x1="86" y1="220" x2="426" y2="220" stroke="#fff" stroke-width="1.5" opacity="0.4"/>
  <line x1="86" y1="290" x2="426" y2="290" stroke="#000" stroke-width="1.5" opacity="0.3"/>
  <!-- 中心孔 -->
  <ellipse cx="256" cy="256" rx="80" ry="14" fill="#1a1e25"/>
  <ellipse cx="256" cy="254" rx="80" ry="12" fill="#0a0d14"/>
</g>'''
    return svg_wrap(body)

def spring_washer():
    """弹簧垫圈（切口）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <!-- 弹簧垫圈：斜切圆环 -->
  <path d="M 256 130 A 130 130 0 1 1 220 250 L 256 130 Z" fill="url(#shaft)" stroke="#2a3038" stroke-width="2"/>
  <path d="M 256 130 A 130 130 0 0 1 380 220 L 220 250 L 256 130 Z" fill="#a8b3c0" opacity="0.4"/>
  <ellipse cx="256" cy="256" rx="100" ry="22" fill="url(#shaft)"/>
  <ellipse cx="256" cy="254" rx="100" ry="20" fill="#fff" opacity="0.15"/>
  <line x1="220" y1="250" x2="256" y2="130" stroke="#1a1e25" stroke-width="2"/>
  <ellipse cx="256" cy="256" rx="60" ry="12" fill="#1a1e25"/>
</g>'''
    return svg_wrap(body)

def cotter_pin():
    """开口销"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <!-- 销体 -->
  <rect x="246" y="100" width="20" height="280" fill="url(#shaft)" stroke="#2a3038" stroke-width="1"/>
  <ellipse cx="256" cy="100" rx="10" ry="14" fill="#a8b3c0" stroke="#2a3038" stroke-width="1"/>
  <!-- 开口端分叉 -->
  <polygon points="246,380 256,440 266,380" fill="#3a4250"/>
  <line x1="256" y1="350" x2="256" y2="430" stroke="#1a1e25" stroke-width="2"/>
  <!-- 头部圆环 -->
  <ellipse cx="256" cy="100" rx="14" ry="18" fill="none" stroke="#3a4250" stroke-width="6"/>
</g>'''
    return svg_wrap(body)

def spring_pin():
    """弹簧销（卷管）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <rect x="216" y="180" width="80" height="220" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.5"/>
  <!-- 卷簧螺旋线 -->
  <line x1="216" y1="200" x2="296" y2="200" stroke="#1a1e25" stroke-width="1.5" opacity="0.7"/>
  <line x1="216" y1="220" x2="296" y2="220" stroke="#1a1e25" stroke-width="1.5" opacity="0.7"/>
  <line x1="216" y1="240" x2="296" y2="240" stroke="#1a1e25" stroke-width="1.5" opacity="0.7"/>
  <line x1="216" y1="260" x2="296" y2="260" stroke="#1a1e25" stroke-width="1.5" opacity="0.7"/>
  <line x1="216" y1="280" x2="296" y2="280" stroke="#1a1e25" stroke-width="1.5" opacity="0.7"/>
  <line x1="216" y1="300" x2="296" y2="300" stroke="#1a1e25" stroke-width="1.5" opacity="0.7"/>
  <line x1="216" y1="320" x2="296" y2="320" stroke="#1a1e25" stroke-width="1.5" opacity="0.7"/>
  <line x1="216" y1="340" x2="296" y2="340" stroke="#1a1e25" stroke-width="1.5" opacity="0.7"/>
  <line x1="216" y1="360" x2="296" y2="360" stroke="#1a1e25" stroke-width="1.5" opacity="0.7"/>
  <!-- 锥形端 -->
  <ellipse cx="256" cy="180" rx="40" ry="12" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="256" cy="400" rx="40" ry="12" fill="#3a4250" stroke="#2a3038" stroke-width="1.2"/>
</g>'''
    return svg_wrap(body)

def dowel_pin():
    """圆柱销（实心）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <rect x="226" y="120" width="60" height="320" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="256" cy="120" rx="30" ry="10" fill="#c8d0dc" stroke="#2a3038" stroke-width="1"/>
  <ellipse cx="256" cy="440" rx="30" ry="10" fill="#3a4250" stroke="#2a3038" stroke-width="1"/>
  <line x1="226" y1="120" x2="286" y2="120" stroke="#fff" stroke-width="2" opacity="0.4"/>
</g>'''
    return svg_wrap(body)

def rivet_round():
    """圆头铆钉"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <ellipse cx="256" cy="200" rx="50" ry="50" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="244" cy="188" rx="22" ry="22" fill="#fff" opacity="0.45"/>
  <rect x="226" y="240" width="60" height="160" fill="url(#shaft)"/>
  <ellipse cx="256" cy="400" rx="40" ry="14" fill="#3a4250" stroke="#2a3038" stroke-width="1"/>
</g>'''
    return svg_wrap(body)

def rivet_csk():
    """沉头铆钉"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <polygon points="206,220 256,160 306,220" fill="url(#shaft)" stroke="#2a3038" stroke-width="1"/>
  <ellipse cx="256" cy="220" rx="50" ry="14" fill="url(#shaft)" stroke="#2a3038" stroke-width="1"/>
  <ellipse cx="256" cy="218" rx="50" ry="14" fill="#fff" opacity="0.2"/>
  <rect x="226" y="234" width="60" height="170" fill="url(#shaft)"/>
  <ellipse cx="256" cy="404" rx="40" ry="14" fill="#3a4250" stroke="#2a3038" stroke-width="1"/>
</g>'''
    return svg_wrap(body)

def rivet_blind():
    """拉铆钉（盲铆）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <ellipse cx="256" cy="170" rx="50" ry="50" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.2"/>
  <ellipse cx="244" cy="158" rx="22" ry="22" fill="#fff" opacity="0.45"/>
  <rect x="226" y="200" width="60" height="100" fill="url(#shaft)" stroke="#2a3038" stroke-width="1"/>
  <ellipse cx="256" cy="300" rx="36" ry="12" fill="#3a4250" stroke="#2a3038" stroke-width="1"/>
  <!-- 拉断芯 -->
  <rect x="252" y="310" width="8" height="120" fill="#7e8896" stroke="#2a3038" stroke-width="0.5"/>
  <circle cx="256" cy="430" r="8" fill="#a8b3c0" stroke="#2a3038" stroke-width="0.5"/>
</g>'''
    return svg_wrap(body)

def retaining_ext():
    """外卡簧"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <path d="M 100 256 Q 100 130 256 130 Q 412 130 412 256 Q 412 290 380 280 L 380 256 Q 380 170 256 170 Q 132 170 132 256 L 132 280 Q 100 290 100 256 Z" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.5"/>
  <ellipse cx="256" cy="256" rx="120" ry="26" fill="#1a1e25"/>
</g>'''
    return svg_wrap(body)

def retaining_int():
    """内卡簧"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <path d="M 100 256 Q 100 130 256 130 Q 412 130 412 256 Q 412 290 380 280 L 380 256 Q 380 170 256 170 Q 132 170 132 256 L 132 280 Q 100 290 100 256 Z" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.5" transform="scale(-1,1) translate(-512,0)"/>
  <ellipse cx="256" cy="256" rx="120" ry="26" fill="#1a1e25"/>
</g>'''
    return svg_wrap(body)

def hose_clamp():
    """喉箍"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    body += '''  <!-- 钢带环 -->
  <ellipse cx="256" cy="256" rx="160" ry="160" fill="none" stroke="url(#shaft)" stroke-width="20"/>
  <ellipse cx="256" cy="256" rx="160" ry="160" fill="none" stroke="#fff" stroke-width="2" opacity="0.3"/>
  <!-- 螺丝锁紧机构 -->
  <rect x="216" y="80" width="80" height="50" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.5"/>
  <circle cx="256" cy="90" r="12" fill="#1a1e25"/>
  <line x1="250" y1="84" x2="262" y2="96" stroke="#fff" stroke-width="2"/>
  <line x1="262" y1="84" x2="250" y2="96" stroke="#fff" stroke-width="2"/>
  <rect x="246" y="40" width="20" height="40" fill="url(#shaft)"/>
</g>'''
    return svg_wrap(body)

def combo_screw():
    """组合螺钉（垫圈+螺丝）"""
    body = shadow_ellipse() + '\n<g filter="url(#ds)">\n'
    # 垫圈
    body += '  <ellipse cx="256" cy="240" rx="100" ry="18" fill="url(#shaft)" stroke="#2a3038" stroke-width="1.2"/>\n'
    body += '  <ellipse cx="256" cy="238" rx="100" ry="18" fill="#fff" opacity="0.2"/>\n'
    body += '  <rect x="156" y="240" width="200" height="20" fill="url(#shaft)"/>\n'
    # 螺丝头
    body += '''  <polygon points="206,200 306,200 316,230 196,230" fill="#a8b3c0" stroke="#2a3038" stroke-width="1.2"/>
  <polygon points="206,200 306,200 256,185" fill="#c8d0dc" stroke="#2a3038" stroke-width="1.2"/>
  <polygon points="256,210 270,220 270,230 256,240 242,230 242,220" fill="#1a1e25"/>
'''
    # 螺杆
    body += '  <rect x="226" y="260" width="60" height="190" fill="url(#shaft)"/>\n'
    body += thread_lines(226, 272, 14)
    body += thread_highlights(226, 272, 14)
    body += '</g>'
    return svg_wrap(body)

# ===== 批量生成 =====

BOLTS = {
    'hex-bolt': hex_bolt,
    'socket-cap': socket_cap,
    'countersunk-socket': countersunk,
    'carriage-bolt': carriage,
    't-bolt': t_bolt,
    'u-bolt': u_bolt,
    'anchor-bolt': anchor_bolt,
    'flange-bolt': flange_bolt,
    'eye-bolt': eye_bolt,
    'wing-bolt': wing_bolt,
    'self-tapping': self_tapping,
    'self-drilling': self_drilling,
}

NUTS = {
    'hex-nut': hex_nut,
    'lock-nut': lock_nut,
    'flange-nut': flange_nut,
    'cap-nut': cap_nut,
    'square-nut': square_nut,
    'wing-nut': wing_nut,
    't-slot-nut': t_slot_nut,
    'weld-nut': weld_nut,
    'rivet-nut': rivet_nut,
}

RODS = {
    'threaded-rod': threaded_rod,
    'stud-bolt-1end': stud_1end,
    'stud-bolt-2end': stud_2end,
}

MISC = {
    'flat-washer': flat_washer,
    'spring-washer': spring_washer,
    'cotter-pin': cotter_pin,
    'spring-pin': spring_pin,
    'dowel-pin': dowel_pin,
    'rivet-round': rivet_round,
    'rivet-csk': rivet_csk,
    'rivet-blind': rivet_blind,
    'retaining-ring-ext': retaining_ext,
    'retaining-ring-int': retaining_int,
    'hose-clamp': hose_clamp,
    'combination-screw': combo_screw,
}

ALL = {}
ALL.update(BOLTS)
ALL.update(NUTS)
ALL.update(RODS)
ALL.update(MISC)

print('开始生成 ' + str(len(ALL)) + ' 张 SVG...')
for name, func in ALL.items():
    svg = func()
    with open('images/' + name + '.svg', 'w') as f:
        f.write(svg)
print('✓ 全部生成完成')

import os
total = 0
for f in os.listdir('images'):
    if f.endswith('.svg'):
        s = os.path.getsize('images/' + f)
        total += s
        print('  ' + f + ': ' + str(s) + ' B')
print('\\n总大小: ' + str(total/1024) + ' KB')
