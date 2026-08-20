#!/usr/bin/env python3
"""
生成 35 个 SVG 产品技术图纸
设计风格：工业蓝图风格（线条简洁，单色调 + 强调色）
"""
import os

OUT_DIR = '/Users/baidelongxia/.openclaw/workspace/hardware-website/images'
os.makedirs(OUT_DIR, exist_ok=True)

# 颜色：钢蓝主线 + 橙色螺纹
STROKE_MAIN = '#7ba7d4'      # 钢蓝（轮廓线）
STROKE_DETAIL = '#5a89bd'    # 深一档（细节线）
STROKE_THREAD = '#f7811a'    # 橙色（螺纹强调）
BG_LIGHT = '#1a2535'          # 深背景填充（透明）

# 通用 viewBox
VB = 'viewBox="0 0 200 200"'

def svg_wrap(content, vb=VB, bg=True):
    """包装 SVG，包含背景矩形"""
    bg_rect = '<rect width="200" height="200" fill="#11151d" rx="8"/>' if bg else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" {vb}>
{bg_rect}
{content}
</svg>'''

def write(name, content):
    path = os.path.join(OUT_DIR, f'{name}.svg')
    with open(path, 'w') as f:
        f.write(content)

# ===== 螺栓系列 =====

# 1. 六角螺栓 (DIN 933 / ISO 4017)
hex_bolt = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none" stroke-linecap="round">
  <!-- 六角头 -->
  <polygon points="60,55 140,55 165,75 165,95 140,115 60,115 35,95 35,75" fill="#1a2535"/>
  <polygon points="68,68 132,68 148,82 148,88 132,102 68,102 52,88 52,82" stroke-width="1" opacity="0.4"/>
  <!-- 杆部 -->
  <rect x="92" y="115" width="16" height="50" fill="#1a2535"/>
</g>
<!-- 螺纹 -->
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="92" y1="120" x2="108" y2="120"/>
  <line x1="92" y1="125" x2="108" y2="125"/>
  <line x1="92" y1="130" x2="108" y2="130"/>
  <line x1="92" y1="135" x2="108" y2="135"/>
  <line x1="92" y1="140" x2="108" y2="140"/>
  <line x1="92" y1="145" x2="108" y2="145"/>
  <line x1="92" y1="150" x2="108" y2="150"/>
  <line x1="92" y1="155" x2="108" y2="155"/>
  <line x1="92" y1="160" x2="108" y2="160"/>
</g>
<!-- 底部尖角 -->
<g stroke="#7ba7d4" stroke-width="2" fill="none">
  <line x1="92" y1="165" x2="100" y2="180"/>
  <line x1="108" y1="165" x2="100" y2="180"/>
</g>
<!-- 尺寸标注 -->
<g stroke="#5a89bd" stroke-width="0.5" fill="#5a89bd" font-family="monospace" font-size="7">
  <line x1="170" y1="55" x2="180" y2="55"/>
  <line x1="170" y1="115" x2="180" y2="115"/>
  <line x1="178" y1="55" x2="178" y2="115"/>
  <text x="182" y="88">A/F</text>
</g>
''')
write('hex-bolt', hex_bolt)

# 2. 内六角圆柱头螺栓 (DIN 912)
socket_cap = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none" stroke-linecap="round">
  <!-- 圆柱头 -->
  <rect x="60" y="50" width="80" height="30" rx="2" fill="#1a2535"/>
  <!-- 内六角孔 -->
  <polygon points="88,55 112,55 122,65 122,75 112,85 88,85 78,75 78,65" stroke-width="1.5"/>
  <!-- 杆部 -->
  <rect x="92" y="80" width="16" height="80" fill="#1a2535"/>
</g>
<!-- 螺纹 -->
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="92" y1="85" x2="108" y2="85"/>
  <line x1="92" y1="92" x2="108" y2="92"/>
  <line x1="92" y1="99" x2="108" y2="99"/>
  <line x1="92" y1="106" x2="108" y2="106"/>
  <line x1="92" y1="113" x2="108" y2="113"/>
  <line x1="92" y1="120" x2="108" y2="120"/>
  <line x1="92" y1="127" x2="108" y2="127"/>
  <line x1="92" y1="134" x2="108" y2="134"/>
  <line x1="92" y1="141" x2="108" y2="141"/>
  <line x1="92" y1="148" x2="108" y2="148"/>
</g>
<!-- 顶部圆角 -->
<g stroke="#7ba7d4" stroke-width="2" fill="none">
  <line x1="92" y1="160" x2="100" y2="175"/>
  <line x1="108" y1="160" x2="100" y2="175"/>
</g>
''')
write('socket-cap', socket_cap)

# 3. 内六角沉头螺栓 (DIN 7991)
countersunk = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 沉头（锥形）-->
  <polygon points="60,80 140,80 100,40" fill="#1a2535"/>
  <polygon points="78,68 122,68 100,52" stroke-width="1" opacity="0.4"/>
  <!-- 内六角 -->
  <polygon points="88,53 112,53 118,60 118,68 112,75 88,75 82,68 82,60" stroke-width="1.5"/>
  <!-- 杆部 -->
  <rect x="92" y="80" width="16" height="85" fill="#1a2535"/>
</g>
<!-- 螺纹 -->
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="92" y1="88" x2="108" y2="88"/>
  <line x1="92" y1="95" x2="108" y2="95"/>
  <line x1="92" y1="102" x2="108" y2="102"/>
  <line x1="92" y1="109" x2="108" y2="109"/>
  <line x1="92" y1="116" x2="108" y2="116"/>
  <line x1="92" y1="123" x2="108" y2="123"/>
  <line x1="92" y1="130" x2="108" y2="130"/>
  <line x1="92" y1="137" x2="108" y2="137"/>
  <line x1="92" y1="144" x2="108" y2="144"/>
  <line x1="92" y1="151" x2="108" y2="151"/>
</g>
<g stroke="#7ba7d4" stroke-width="2" fill="none">
  <line x1="92" y1="165" x2="100" y2="178"/>
  <line x1="108" y1="165" x2="100" y2="178"/>
</g>
''')
write('countersunk-socket', countersunk)

# 4. 马车螺栓 (DIN 603) - 圆头 + 方颈
carriage = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 圆头（蘑菇头）-->
  <path d="M70 60 Q70 35 100 35 Q130 35 130 60 L130 70 L70 70 Z" fill="#1a2535"/>
  <!-- 方颈 -->
  <rect x="92" y="70" width="16" height="20" fill="#1a2535"/>
  <!-- 杆部 -->
  <rect x="92" y="90" width="16" height="75" fill="#1a2535"/>
</g>
<!-- 螺纹 -->
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="92" y1="98" x2="108" y2="98"/>
  <line x1="92" y1="105" x2="108" y2="105"/>
  <line x1="92" y1="112" x2="108" y2="112"/>
  <line x1="92" y1="119" x2="108" y2="119"/>
  <line x1="92" y1="126" x2="108" y2="126"/>
  <line x1="92" y1="133" x2="108" y2="133"/>
  <line x1="92" y1="140" x2="108" y2="140"/>
  <line x1="92" y1="147" x2="108" y2="147"/>
  <line x1="92" y1="154" x2="108" y2="154"/>
</g>
''')
write('carriage-bolt', carriage)

# 5. T 型螺栓
tbolt = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- T 头 -->
  <rect x="50" y="40" width="100" height="14" rx="2" fill="#1a2535"/>
  <rect x="88" y="54" width="24" height="20" fill="#1a2535"/>
  <!-- 杆部 -->
  <rect x="92" y="74" width="16" height="90" fill="#1a2535"/>
</g>
<!-- 螺纹 -->
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="92" y1="82" x2="108" y2="82"/>
  <line x1="92" y1="90" x2="108" y2="90"/>
  <line x1="92" y1="98" x2="108" y2="98"/>
  <line x1="92" y1="106" x2="108" y2="106"/>
  <line x1="92" y1="114" x2="108" y2="114"/>
  <line x1="92" y1="122" x2="108" y2="122"/>
  <line x1="92" y1="130" x2="108" y2="130"/>
  <line x1="92" y1="138" x2="108" y2="138"/>
  <line x1="92" y1="146" x2="108" y2="146"/>
</g>
<g stroke="#7ba7d4" stroke-width="2" fill="none">
  <line x1="92" y1="164" x2="100" y2="178"/>
  <line x1="108" y1="164" x2="100" y2="178"/>
</g>
''')
write('t-bolt', tbolt)

# 6. U 型螺栓
ubolt = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- U 形 -->
  <path d="M50 70 Q50 30 100 30 Q150 30 150 70 L150 170 L130 170 L130 75 Q130 50 100 50 Q70 50 70 75 L70 170 L50 170 Z" fill="#1a2535"/>
</g>
<!-- 螺纹 -->
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="50" y1="90" x2="70" y2="90"/>
  <line x1="50" y1="100" x2="70" y2="100"/>
  <line x1="50" y1="110" x2="70" y2="110"/>
  <line x1="50" y1="120" x2="70" y2="120"/>
  <line x1="50" y1="130" x2="70" y2="130"/>
  <line x1="50" y1="140" x2="70" y2="140"/>
  <line x1="50" y1="150" x2="70" y2="150"/>
  <line x1="50" y1="160" x2="70" y2="160"/>
  <line x1="130" y1="90" x2="150" y2="90"/>
  <line x1="130" y1="100" x2="150" y2="100"/>
  <line x1="130" y1="110" x2="150" y2="110"/>
  <line x1="130" y1="120" x2="150" y2="120"/>
  <line x1="130" y1="130" x2="150" y2="130"/>
  <line x1="130" y1="140" x2="150" y2="140"/>
  <line x1="130" y1="150" x2="150" y2="150"/>
  <line x1="130" y1="160" x2="150" y2="160"/>
</g>
''')
write('u-bolt', ubolt)

# 7. 地脚螺栓 (弯钩)
anchor = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- L 形弯钩 -->
  <path d="M50 30 L100 30 Q150 30 150 80 Q150 130 100 130 L100 175" stroke-width="3" fill="none"/>
  <rect x="92" y="40" width="16" height="20" fill="#1a2535" stroke="none"/>
</g>
<!-- 螺纹 -->
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="92" y1="65" x2="108" y2="65"/>
  <line x1="92" y1="75" x2="108" y2="75"/>
  <line x1="92" y1="85" x2="108" y2="85"/>
  <line x1="92" y1="95" x2="108" y2="95"/>
  <line x1="92" y1="105" x2="108" y2="105"/>
  <line x1="92" y1="115" x2="108" y2="115"/>
  <line x1="92" y1="125" x2="108" y2="125"/>
  <line x1="92" y1="135" x2="108" y2="135"/>
  <line x1="92" y1="145" x2="108" y2="145"/>
  <line x1="92" y1="155" x2="108" y2="155"/>
</g>
<g stroke="#7ba7d4" stroke-width="2" fill="none">
  <line x1="92" y1="165" x2="100" y2="178"/>
  <line x1="108" y1="165" x2="100" y2="178"/>
</g>
''')
write('anchor-bolt', anchor)

# 8. 法兰面螺栓
flange_bolt = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 六角头 -->
  <polygon points="65,55 135,55 155,75 155,95 135,115 65,115 45,95 45,75" fill="#1a2535"/>
  <polygon points="73,68 127,68 142,82 142,88 127,102 73,102 58,88 58,82" stroke-width="1" opacity="0.4"/>
  <!-- 法兰盘（带齿）-->
  <ellipse cx="100" cy="125" rx="40" ry="10" fill="#1a2535"/>
  <ellipse cx="100" cy="125" rx="40" ry="10" stroke-width="1.5"/>
  <!-- 杆部 -->
  <rect x="92" y="125" width="16" height="50" fill="#1a2535"/>
</g>
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="92" y1="130" x2="108" y2="130"/>
  <line x1="92" y1="138" x2="108" y2="138"/>
  <line x1="92" y1="146" x2="108" y2="146"/>
  <line x1="92" y1="154" x2="108" y2="154"/>
  <line x1="92" y1="162" x2="108" y2="162"/>
</g>
<g stroke="#7ba7d4" stroke-width="2" fill="none">
  <line x1="92" y1="175" x2="100" y2="185"/>
  <line x1="108" y1="175" x2="100" y2="185"/>
</g>
''')
write('flange-bolt', flange_bolt)

# 9. 吊环螺栓
eyebolt = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 圆环 -->
  <circle cx="100" cy="55" r="22" fill="#1a2535"/>
  <circle cx="100" cy="55" r="14" stroke-width="2"/>
  <!-- 颈部 -->
  <rect x="92" y="77" width="16" height="18" fill="#1a2535"/>
  <!-- 杆部 -->
  <rect x="92" y="95" width="16" height="80" fill="#1a2535"/>
</g>
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="92" y1="105" x2="108" y2="105"/>
  <line x1="92" y1="113" x2="108" y2="113"/>
  <line x1="92" y1="121" x2="108" y2="121"/>
  <line x1="92" y1="129" x2="108" y2="129"/>
  <line x1="92" y1="137" x2="108" y2="137"/>
  <line x1="92" y1="145" x2="108" y2="145"/>
  <line x1="92" y1="153" x2="108" y2="153"/>
  <line x1="92" y1="161" x2="108" y2="161"/>
</g>
''')
write('eye-bolt', eyebolt)

# 10. 蝶形螺栓
wingbolt = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 蝶形翼 -->
  <path d="M40 60 L70 60 L70 40 L130 40 L130 60 L160 60 L160 80 L130 80 L130 100 L70 100 L70 80 L40 80 Z" fill="#1a2535"/>
  <!-- 杆部 -->
  <rect x="92" y="80" width="16" height="90" fill="#1a2535"/>
</g>
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="92" y1="90" x2="108" y2="90"/>
  <line x1="92" y1="98" x2="108" y2="98"/>
  <line x1="92" y1="106" x2="108" y2="106"/>
  <line x1="92" y1="114" x2="108" y2="114"/>
  <line x1="92" y1="122" x2="108" y2="122"/>
  <line x1="92" y1="130" x2="108" y2="130"/>
  <line x1="92" y1="138" x2="108" y2="138"/>
  <line x1="92" y1="146" x2="108" y2="146"/>
  <line x1="92" y1="154" x2="108" y2="154"/>
</g>
''')
write('wing-bolt', wingbolt)

# 11. 自攻螺丝 (尖头)
selftap = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 盘头 -->
  <ellipse cx="100" cy="55" rx="30" ry="14" fill="#1a2535"/>
  <ellipse cx="100" cy="55" rx="30" ry="14" stroke-width="2"/>
  <!-- 十字槽 -->
  <line x1="88" y1="55" x2="112" y2="55" stroke-width="1.5"/>
  <line x1="100" y1="43" x2="100" y2="67" stroke-width="1.5"/>
  <!-- 杆部 -->
  <rect x="93" y="69" width="14" height="70" fill="#1a2535"/>
</g>
<!-- 螺纹（尖头自攻）-->
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="93" y1="76" x2="107" y2="76"/>
  <line x1="93" y1="82" x2="107" y2="82"/>
  <line x1="93" y1="88" x2="107" y2="88"/>
  <line x1="93" y1="94" x2="107" y2="94"/>
  <line x1="93" y1="100" x2="107" y2="100"/>
  <line x1="93" y1="106" x2="107" y2="106"/>
  <line x1="93" y1="112" x2="107" y2="112"/>
  <line x1="93" y1="118" x2="107" y2="118"/>
  <line x1="93" y1="124" x2="107" y2="124"/>
  <line x1="93" y1="130" x2="107" y2="130"/>
</g>
<!-- 尖头 -->
<g stroke="#7ba7d4" stroke-width="2" fill="none">
  <line x1="93" y1="139" x2="100" y2="155"/>
  <line x1="107" y1="139" x2="100" y2="155"/>
  <line x1="100" y1="155" x2="100" y2="160"/>
</g>
''')
write('self-tapping', selftap)

# 12. 自钻螺丝 (钻头尖)
selfdrill = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 六角华司头 -->
  <polygon points="65,45 135,45 150,60 150,72 135,87 65,87 50,72 50,60" fill="#1a2535"/>
  <polygon points="73,55 127,55 138,64 138,68 127,77 73,77 62,68 62,64" stroke-width="1" opacity="0.4"/>
  <!-- 华司垫 -->
  <ellipse cx="100" cy="95" rx="38" ry="8" fill="#1a2535"/>
  <ellipse cx="100" cy="95" rx="38" ry="8" stroke-width="1.5"/>
  <!-- 杆部 -->
  <rect x="93" y="95" width="14" height="55" fill="#1a2535"/>
</g>
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="93" y1="102" x2="107" y2="102"/>
  <line x1="93" y1="108" x2="107" y2="108"/>
  <line x1="93" y1="114" x2="107" y2="114"/>
  <line x1="93" y1="120" x2="107" y2="120"/>
  <line x1="93" y1="126" x2="107" y2="126"/>
  <line x1="93" y1="132" x2="107" y2="132"/>
  <line x1="93" y1="138" x2="107" y2="138"/>
</g>
<!-- 钻头尖 -->
<g stroke="#7ba7d4" stroke-width="2" fill="none">
  <line x1="93" y1="150" x2="100" y2="170"/>
  <line x1="107" y1="150" x2="100" y2="170"/>
  <line x1="98" y1="160" x2="105" y2="155" stroke-width="1"/>
</g>
''')
write('self-drilling', selfdrill)

# ===== 螺母系列 =====

# 13. 六角螺母 (DIN 934)
hex_nut = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 顶面六边形 -->
  <polygon points="100,50 145,75 145,125 100,150 55,125 55,75" fill="#1a2535"/>
  <!-- 中心孔 -->
  <circle cx="100" cy="100" r="20" fill="#11151d" stroke-width="2"/>
  <!-- 螺纹孔示意 -->
  <line x1="80" y1="100" x2="120" y2="100" stroke="#f7811a" stroke-width="1"/>
</g>
<!-- 侧面厚度 -->
<g stroke="#7ba7d4" stroke-width="1" fill="none" opacity="0.5">
  <line x1="55" y1="75" x2="55" y2="115"/>
  <line x1="145" y1="75" x2="145" y2="115"/>
  <line x1="145" y1="125" x2="145" y2="135"/>
  <line x1="55" y1="125" x2="55" y2="135"/>
</g>
<!-- 尺寸标注 -->
<g stroke="#5a89bd" stroke-width="0.5" fill="#5a89bd" font-family="monospace" font-size="7">
  <line x1="155" y1="75" x2="165" y2="75"/>
  <line x1="155" y1="125" x2="165" y2="125"/>
  <line x1="163" y1="75" x2="163" y2="125"/>
  <text x="167" y="103">S</text>
</g>
''')
write('hex-nut', hex_nut)

# 14. 尼龙锁紧螺母
lock_nut = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <polygon points="100,50 145,75 145,125 100,150 55,125 55,75" fill="#1a2535"/>
  <!-- 中心孔 -->
  <circle cx="100" cy="100" r="20" fill="#11151d" stroke-width="2"/>
  <!-- 尼龙环（橙色强调）-->
  <circle cx="100" cy="100" r="13" stroke="#f7811a" stroke-width="2" fill="none"/>
  <circle cx="100" cy="100" r="6" stroke="#f7811a" stroke-width="1" fill="none"/>
</g>
<g stroke="#7ba7d4" stroke-width="1" fill="none" opacity="0.5">
  <line x1="55" y1="75" x2="55" y2="115"/>
  <line x1="145" y1="75" x2="145" y2="115"/>
</g>
<!-- N 标记 -->
<g fill="#f7811a" font-family="monospace" font-size="8" font-weight="bold">
  <text x="93" y="103">N</text>
</g>
''')
write('lock-nut', lock_nut)

# 15. 法兰螺母
flange_nut = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 六角头 -->
  <polygon points="100,30 135,50 135,90 100,110 65,90 65,50" fill="#1a2535"/>
  <!-- 法兰盘 -->
  <ellipse cx="100" cy="115" rx="50" ry="12" fill="#1a2535"/>
  <ellipse cx="100" cy="115" rx="50" ry="12" stroke-width="2"/>
  <!-- 齿纹 -->
  <line x1="55" y1="115" x2="60" y2="125"/>
  <line x1="65" y1="120" x2="70" y2="130"/>
  <line x1="80" y1="125" x2="85" y2="135"/>
  <line x1="95" y1="127" x2="98" y2="137"/>
  <line x1="105" y1="127" x2="102" y2="137"/>
  <line x1="120" y1="125" x2="115" y2="135"/>
  <line x1="135" y1="120" x2="130" y2="130"/>
  <line x1="145" y1="115" x2="140" y2="125"/>
  <!-- 中心孔 -->
  <circle cx="100" cy="73" r="15" fill="#11151d" stroke-width="2"/>
</g>
<!-- 螺纹孔 -->
<line x1="85" y1="73" x2="115" y2="73" stroke="#f7811a" stroke-width="1"/>
''')
write('flange-nut', flange_nut)

# 16. 盖帽螺母 (DIN 917)
cap_nut = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 圆顶 -->
  <path d="M55 110 Q55 80 70 70 L130 70 Q145 80 145 110 L145 130 L55 130 Z" fill="#1a2535"/>
  <!-- 六角底部 -->
  <line x1="60" y1="125" x2="60" y2="145" stroke-width="2"/>
  <line x1="140" y1="125" x2="140" y2="145" stroke-width="2"/>
  <polygon points="60,145 140,145 130,158 70,158" fill="#1a2535"/>
  <!-- 中心 -->
  <circle cx="100" cy="90" r="18" fill="#11151d" stroke-width="2"/>
</g>
<g stroke="#7ba7d4" stroke-width="1" fill="none" opacity="0.5">
  <line x1="60" y1="110" x2="60" y2="125"/>
  <line x1="140" y1="110" x2="140" y2="125"/>
</g>
<line x1="82" y1="90" x2="118" y2="90" stroke="#f7811a" stroke-width="1"/>
''')
write('cap-nut', cap_nut)

# 17. 方形螺母
square_nut = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 顶面 -->
  <polygon points="60,55 140,55 140,145 60,145" fill="#1a2535"/>
  <!-- 透视边 -->
  <line x1="60" y1="55" x2="75" y2="40" stroke-width="1" opacity="0.5"/>
  <line x1="140" y1="55" x2="155" y2="40" stroke-width="1" opacity="0.5"/>
  <line x1="155" y1="40" x2="155" y2="130" stroke-width="1" opacity="0.5"/>
  <line x1="75" y1="40" x2="155" y2="40" stroke-width="1" opacity="0.5"/>
  <line x1="60" y1="145" x2="75" y2="130" stroke-width="1" opacity="0.5"/>
  <line x1="140" y1="145" x2="155" y2="130" stroke-width="1" opacity="0.5"/>
  <!-- 中心孔 -->
  <circle cx="100" cy="100" r="22" fill="#11151d" stroke-width="2"/>
</g>
<line x1="78" y1="100" x2="122" y2="100" stroke="#f7811a" stroke-width="1"/>
''')
write('square-nut', square_nut)

# 18. 蝶形螺母
wing_nut = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 左右蝶翼 -->
  <path d="M30 70 Q30 60 40 60 L75 60 Q80 70 80 90 L80 110 Q80 120 75 120 L40 120 Q30 120 30 110 Z" fill="#1a2535"/>
  <path d="M170 70 Q170 60 160 60 L125 60 Q120 70 120 90 L120 110 Q120 120 125 120 L160 120 Q170 120 170 110 Z" fill="#1a2535"/>
  <!-- 中心 -->
  <ellipse cx="100" cy="90" rx="25" ry="22" fill="#1a2535"/>
  <ellipse cx="100" cy="90" rx="25" ry="22" stroke-width="2"/>
  <!-- 中心孔 -->
  <circle cx="100" cy="90" r="14" fill="#11151d" stroke-width="2"/>
</g>
<line x1="86" y1="90" x2="114" y2="90" stroke="#f7811a" stroke-width="1"/>
<!-- 底部锥形 -->
<g stroke="#7ba7d4" stroke-width="2" fill="none">
  <line x1="78" y1="112" x2="122" y2="112"/>
  <line x1="82" y1="125" x2="118" y2="125"/>
</g>
''')
write('wing-nut', wing_nut)

# 19. T 型螺母
tslot_nut = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- T 头（俯视）-->
  <rect x="50" y="60" width="100" height="14" rx="2" fill="#1a2535"/>
  <!-- 中间块 -->
  <rect x="80" y="74" width="40" height="60" fill="#1a2535"/>
  <!-- 透视顶 -->
  <ellipse cx="100" cy="60" rx="50" ry="6" fill="#1a2535" stroke-width="1.5"/>
  <!-- 中心螺纹孔 -->
  <circle cx="100" cy="100" r="13" fill="#11151d" stroke-width="2"/>
</g>
<line x1="87" y1="100" x2="113" y2="100" stroke="#f7811a" stroke-width="1"/>
''')
write('t-slot-nut', tslot_nut)

# 20. 焊接螺母
weld_nut = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <polygon points="100,50 145,75 145,125 100,150 55,125 55,75" fill="#1a2535"/>
  <!-- 焊接凸点 -->
  <circle cx="100" cy="75" r="3" fill="#f7811a"/>
  <circle cx="120" cy="100" r="3" fill="#f7811a"/>
  <circle cx="100" cy="125" r="3" fill="#f7811a"/>
  <circle cx="80" cy="100" r="3" fill="#f7811a"/>
  <!-- 中心孔 -->
  <circle cx="100" cy="100" r="18" fill="#11151d" stroke-width="2"/>
</g>
<line x1="82" y1="100" x2="118" y2="100" stroke="#f7811a" stroke-width="1"/>
''')
write('weld-nut', weld_nut)

# 21. 拉铆螺母
rivet_nut = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 圆柱主体 -->
  <rect x="65" y="40" width="70" height="100" rx="2" fill="#1a2535"/>
  <!-- 顶部法兰 -->
  <rect x="55" y="40" width="90" height="15" rx="2" fill="#1a2535"/>
  <!-- 底部锥形 -->
  <polygon points="65,140 135,140 125,160 75,160" fill="#1a2535"/>
  <!-- 中心孔 -->
  <circle cx="100" cy="80" r="14" fill="#11151d" stroke-width="2"/>
</g>
<line x1="86" y1="80" x2="114" y2="80" stroke="#f7811a" stroke-width="1"/>
<!-- 螺纹线 -->
<g stroke="#f7811a" stroke-width="0.8" fill="none" opacity="0.6">
  <line x1="65" y1="50" x2="135" y2="50"/>
  <line x1="65" y1="58" x2="135" y2="58"/>
  <line x1="65" y1="66" x2="135" y2="66"/>
  <line x1="65" y1="100" x2="135" y2="100"/>
  <line x1="65" y1="108" x2="135" y2="108"/>
  <line x1="65" y1="116" x2="135" y2="116"/>
</g>
''')
write('rivet-nut', rivet_nut)

# ===== 螺杆系列 =====

# 22. 全螺纹螺杆
threaded_rod = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 杆部 -->
  <rect x="20" y="92" width="160" height="16" fill="#1a2535"/>
</g>
<!-- 全螺纹 -->
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="25" y1="92" x2="30" y2="108"/>
  <line x1="35" y1="92" x2="40" y2="108"/>
  <line x1="45" y1="92" x2="50" y2="108"/>
  <line x1="55" y1="92" x2="60" y2="108"/>
  <line x1="65" y1="92" x2="70" y2="108"/>
  <line x1="75" y1="92" x2="80" y2="108"/>
  <line x1="85" y1="92" x2="90" y2="108"/>
  <line x1="95" y1="92" x2="100" y2="108"/>
  <line x1="105" y1="92" x2="110" y2="108"/>
  <line x1="115" y1="92" x2="120" y2="108"/>
  <line x1="125" y1="92" x2="130" y2="108"/>
  <line x1="135" y1="92" x2="140" y2="108"/>
  <line x1="145" y1="92" x2="150" y2="108"/>
  <line x1="155" y1="92" x2="160" y2="108"/>
  <line x1="165" y1="92" x2="170" y2="108"/>
</g>
<!-- 端面圆角 -->
<g stroke="#7ba7d4" stroke-width="2" fill="none">
  <path d="M20 92 Q15 100 20 108"/>
  <path d="M180 92 Q185 100 180 108"/>
</g>
<!-- 尺寸标注 -->
<g stroke="#5a89bd" stroke-width="0.5" fill="#5a89bd" font-family="monospace" font-size="8">
  <line x1="20" y1="130" x2="180" y2="130"/>
  <line x1="20" y1="125" x2="20" y2="135"/>
  <line x1="180" y1="125" x2="180" y2="135"/>
  <text x="90" y="145">L = 1000mm</text>
</g>
''')
write('threaded-rod', threaded_rod)

# 23. 双头螺柱（两端螺纹）
stud_2end = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 中间杆（光杆）-->
  <rect x="60" y="92" width="80" height="16" fill="#1a2535"/>
</g>
<!-- 左端螺纹 -->
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="25" y1="92" x2="30" y2="108"/>
  <line x1="35" y1="92" x2="40" y2="108"/>
  <line x1="45" y1="92" x2="50" y2="108"/>
  <line x1="55" y1="92" x2="60" y2="108"/>
</g>
<!-- 右端螺纹 -->
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="140" y1="92" x2="145" y2="108"/>
  <line x1="150" y1="92" x2="155" y2="108"/>
  <line x1="160" y1="92" x2="165" y2="108"/>
  <line x1="170" y1="92" x2="175" y2="108"/>
</g>
<!-- 端面圆角 -->
<g stroke="#7ba7d4" stroke-width="2" fill="none">
  <path d="M20 92 Q15 100 20 108"/>
  <path d="M180 92 Q185 100 180 108"/>
</g>
<g stroke="#5a89bd" stroke-width="0.5" fill="#5a89bd" font-family="monospace" font-size="7">
  <text x="40" y="80">thread</text>
  <text x="155" y="80">thread</text>
  <text x="85" y="80">shank</text>
</g>
''')
write('stud-bolt-2end', stud_2end)

# 24. 双头螺柱（一端螺纹）
stud_1end = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <rect x="40" y="92" width="120" height="16" fill="#1a2535"/>
</g>
<!-- 右端螺纹 -->
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="120" y1="92" x2="125" y2="108"/>
  <line x1="130" y1="92" x2="135" y2="108"/>
  <line x1="140" y1="92" x2="145" y2="108"/>
  <line x1="150" y1="92" x2="155" y2="108"/>
  <line x1="160" y1="92" x2="165" y2="108"/>
  <line x1="170" y1="92" x2="175" y2="108"/>
</g>
<g stroke="#7ba7d4" stroke-width="2" fill="none">
  <path d="M40 92 Q35 100 40 108"/>
  <path d="M160 92 Q165 100 160 108"/>
</g>
<g stroke="#5a89bd" stroke-width="0.5" fill="#5a89bd" font-family="monospace" font-size="7">
  <text x="55" y="80">shank</text>
  <text x="140" y="80">thread</text>
</g>
''')
write('stud-bolt-1end', stud_1end)

# ===== 紧固件系列 =====

# 25. 平垫圈
flat_washer = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 外圆 -->
  <circle cx="100" cy="100" r="55" fill="#1a2535"/>
  <!-- 内孔 -->
  <circle cx="100" cy="100" r="22" fill="#11151d" stroke-width="2"/>
</g>
<!-- 透视厚度 -->
<g stroke="#7ba7d4" stroke-width="1" fill="none" opacity="0.5">
  <ellipse cx="100" cy="105" rx="55" ry="5"/>
  <ellipse cx="100" cy="95" rx="55" ry="5"/>
</g>
<g stroke="#5a89bd" stroke-width="0.5" fill="#5a89bd" font-family="monospace" font-size="7">
  <line x1="100" y1="45" x2="100" y2="78"/>
  <text x="105" y="62">Ød</text>
</g>
''')
write('flat-washer', flat_washer)

# 26. 弹簧垫圈
spring_washer = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 弹簧圈 -->
  <circle cx="100" cy="100" r="50" fill="#1a2535"/>
  <!-- 切口 -->
  <line x1="100" y1="50" x2="100" y2="80" stroke-width="3" stroke="#f7811a"/>
  <!-- 偏心 -->
  <path d="M100 80 Q120 100 100 150" stroke="#f7811a" stroke-width="2" fill="none"/>
  <!-- 内孔 -->
  <circle cx="100" cy="100" r="22" fill="#11151d" stroke-width="2"/>
</g>
''')
write('spring-washer', spring_washer)

# 27. 开口销
cotter_pin = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 主体 -->
  <rect x="20" y="95" width="160" height="10" rx="5" fill="#1a2535"/>
  <!-- 弯头 -->
  <path d="M20 100 Q15 90 25 80 Q35 75 30 85" stroke-width="2"/>
  <!-- 另一头分叉 -->
  <path d="M180 100 L185 90 M180 100 L185 110" stroke-width="2"/>
</g>
''')
write('cotter-pin', cotter_pin)

# 28. 弹性圆柱销
spring_pin = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 主体管 -->
  <rect x="30" y="90" width="140" height="20" rx="10" fill="#1a2535"/>
  <!-- 卷边（锥形）-->
  <path d="M30 90 Q40 95 30 100" stroke-width="2"/>
  <path d="M170 90 Q160 95 170 100" stroke-width="2"/>
  <!-- 切口 -->
  <line x1="40" y1="95" x2="160" y2="95" stroke="#f7811a" stroke-width="1.5"/>
  <line x1="40" y1="105" x2="160" y2="105" stroke="#f7811a" stroke-width="1.5"/>
</g>
''')
write('spring-pin', spring_pin)

# 29. 实心圆柱销
dowel_pin = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <rect x="20" y="92" width="160" height="16" rx="8" fill="#1a2535"/>
</g>
<!-- 端面倒角 -->
<g stroke="#7ba7d4" stroke-width="2" fill="none">
  <line x1="20" y1="92" x2="30" y2="100"/>
  <line x1="20" y1="108" x2="30" y2="100"/>
  <line x1="180" y1="92" x2="170" y2="100"/>
  <line x1="180" y1="108" x2="170" y2="100"/>
</g>
<g stroke="#5a89bd" stroke-width="0.5" fill="#5a89bd" font-family="monospace" font-size="7">
  <text x="80" y="85">Ø8 × 40</text>
</g>
''')
write('dowel-pin', dowel_pin)

# 30. 沉头铆钉
rivet_csk = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 锥头 -->
  <polygon points="80,60 120,60 100,40" fill="#1a2535"/>
  <!-- 杆部 -->
  <rect x="92" y="60" width="16" height="100" fill="#1a2535"/>
</g>
<!-- 底部铆头 -->
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <path d="M92 160 Q92 175 100 175 Q108 175 108 160" fill="#1a2535"/>
</g>
''')
write('rivet-csk', rivet_csk)

# 31. 圆头铆钉
rivet_round = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 圆头 -->
  <ellipse cx="100" cy="55" rx="22" ry="22" fill="#1a2535"/>
  <!-- 杆部 -->
  <rect x="92" y="77" width="16" height="85" fill="#1a2535"/>
</g>
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <path d="M92 162 Q92 175 100 175 Q108 175 108 162" fill="#1a2535"/>
</g>
''')
write('rivet-round', rivet_round)

# 32. 拉铆钉（盲孔铆钉）
rivet_blind = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 圆头 -->
  <ellipse cx="100" cy="50" rx="20" ry="20" fill="#1a2535"/>
  <!-- 外壳 -->
  <rect x="85" y="70" width="30" height="80" fill="#1a2535"/>
  <!-- 内拉杆 -->
  <line x1="100" y1="150" x2="100" y2="180" stroke-width="3" stroke="#f7811a"/>
  <!-- 拉杆头 -->
  <ellipse cx="100" cy="180" rx="6" ry="3" fill="#f7811a" stroke="#f7811a"/>
</g>
<!-- �接后变形（虚线）-->
<g stroke="#7ba7d4" stroke-width="1" fill="none" stroke-dasharray="2,2" opacity="0.4">
  <path d="M85 150 Q90 165 100 165 Q110 165 115 150"/>
</g>
''')
write('rivet-blind', rivet_blind)

# 33. 外卡簧挡圈
ring_ext = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- C 形环 -->
  <path d="M70 130 Q40 130 40 100 Q40 70 70 70 L130 70 Q160 70 160 100 Q160 130 130 130 L120 125" fill="#1a2535"/>
  <!-- 端部耳 -->
  <circle cx="70" cy="70" r="4" fill="#1a2535"/>
  <circle cx="130" cy="70" r="4" fill="#1a2535"/>
</g>
<g stroke="#f7811a" stroke-width="1" fill="none">
  <line x1="40" y1="100" x2="160" y2="100"/>
  <line x1="55" y1="80" x2="145" y2="120"/>
</g>
''')
write('retaining-ring-ext', ring_ext)

# 34. 内卡簧挡圈
ring_int = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- C 形环（反向）-->
  <path d="M70 70 Q40 70 40 100 Q40 130 70 130 L130 130 Q160 130 160 100 Q160 70 130 70 L120 75" fill="#1a2535"/>
  <!-- 端部耳 -->
  <circle cx="70" cy="130" r="4" fill="#1a2535"/>
  <circle cx="130" cy="130" r="4" fill="#1a2535"/>
</g>
<g stroke="#f7811a" stroke-width="1" fill="none">
  <line x1="40" y1="100" x2="160" y2="100"/>
  <line x1="55" y1="80" x2="145" y2="120"/>
</g>
''')
write('retaining-ring-int', ring_int)

# 35. 喉箍
hose_clamp = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 外环 -->
  <circle cx="100" cy="100" r="55" fill="#1a2535"/>
  <!-- 切口 -->
  <line x1="50" y1="80" x2="50" y2="120" stroke="#f7811a" stroke-width="3"/>
  <!-- 螺栓 -->
  <rect x="35" y="93" width="30" height="14" fill="#1a2535"/>
  <!-- 螺母 -->
  <circle cx="42" cy="100" r="6" fill="#1a2535" stroke-width="1.5"/>
</g>
<!-- 螺纹 -->
<g stroke="#f7811a" stroke-width="0.8" fill="none">
  <line x1="35" y1="93" x2="65" y2="93"/>
  <line x1="35" y1="107" x2="65" y2="107"/>
</g>
''')
write('hose-clamp', hose_clamp)

# 36. 组合螺丝（螺丝+垫圈）
combo_screw = svg_wrap('''
<g stroke="#7ba7d4" stroke-width="2.5" fill="none">
  <!-- 六角头 -->
  <polygon points="75,40 125,40 140,55 140,70 125,85 75,85 60,70 60,55" fill="#1a2535"/>
  <!-- 弹簧垫圈 -->
  <path d="M55 95 Q45 100 55 110 L145 110 Q155 100 145 95" fill="#1a2535"/>
  <!-- 平垫圈 -->
  <ellipse cx="100" cy="125" rx="48" ry="10" fill="#1a2535"/>
  <ellipse cx="100" cy="125" rx="48" ry="10" stroke-width="2"/>
  <!-- 中心孔 -->
  <circle cx="100" cy="125" r="20" fill="#11151d" stroke-width="2"/>
  <!-- 杆 -->
  <rect x="93" y="125" width="14" height="50" fill="#1a2535"/>
</g>
<g stroke="#f7811a" stroke-width="1.5" fill="none">
  <line x1="93" y1="135" x2="107" y2="135"/>
  <line x1="93" y1="142" x2="107" y2="142"/>
  <line x1="93" y1="149" x2="107" y2="149"/>
  <line x1="93" y1="156" x2="107" y2="156"/>
  <line x1="93" y1="163" x2="107" y2="163"/>
</g>
''')
write('combination-screw', combo_screw)

print(f'✓ 已生成 {len(os.listdir(OUT_DIR))} 个 SVG 文件')
print(f'输出目录: {OUT_DIR}')
