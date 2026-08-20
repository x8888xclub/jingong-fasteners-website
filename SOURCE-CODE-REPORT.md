# 精工固件 Jingong Fasteners — 源码报告（v3.5）

> 给晓白的源码阅读指南 — 看完这份就知道每个文件干什么、关键函数怎么用、想改哪里改哪里。

---

## 一、项目总览

### 是什么

一个 **B2B 紧固件外贸独立站**，中英双语、100 SKU、5 个在线计算器、深色工业风、响应式（PC + 平板 + 手机）。

### 技术栈

| 项目 | 选型 | 理由 |
|------|------|------|
| 前端 | 纯静态 HTML / CSS / JS | 无需构建工具，部署简单 |
| 图片 | SVG（100 张唯一 + 36 张共享）| 矢量、可缩放、文件小 |
| 部署 | GitHub Pages | 免费、绑定域名、CDN 自动 |
| 双语 | 单 JS 文件 + data-i18n 属性 | 简单、可维护 |
| 响应式 | CSS @media 三断点 | 968 / 640 / 380 |

### 在线预览

https://x8888xclub.github.io/jingong-fasteners-website/

### 代码规模

| 维度 | 数量 |
|------|------|
| HTML | 1 个页面 / 878 行 |
| CSS | 1 个文件 / 2,499 行（含 3 个 @media 断点）|
| JS | 8 个文件 / 2,028 行 |
| SVG（共享）| 36 张 |
| SVG（唯一）| 100 张 |
| 产品 SKU | 100 个（B 螺栓 30 + N 螺母 28 + R 螺杆 12 + F 紧固件 30）|
| 翻译键 | 255 个（中英各 255）|
| 规格表 | 4 套（BSW 英制粗牙 / UNC 美制粗牙 / UNF 美制细牙 / Metric 公制）|
| 在线计算器 | 5 个（螺栓 / 螺母 / 螺杆 / 垫圈 / 强度对比）|

---

## 二、文件清单（按重要性排序）

### 🔵 核心文件（先看这三个）

| 文件 | 行数 | 作用 | 改这个会改什么 |
|------|------|------|----------------|
| `index.html` | 878 | 整站结构（11 个 section）| 改布局、加区块、改文案 |
| `css/style.css` | 2,499 | 所有样式 + 3 个移动端断点 | 改颜色、间距、移动端样式 |
| `js/products-data.js` | 172 | **100 个产品的真实数据** | **加产品、改规格、改价格、改材质** |

### 🟢 JS 文件

| 文件 | 行数 | 作用 | 关键函数 |
|------|------|------|---------|
| `js/i18n.js` | 753 | 双语翻译系统（255 keys）| `t()`、`tMat()`、`tSpec()`、`setLanguage()` |
| `js/main.js` | 460 | 产品渲染、筛选、搜索、排序 | `renderProductCard()`、`renderProducts()`、`applyFilters()` |
| `js/calculator-engine.js` | 269 | 5 个计算器的算法核心 | `CalcEngine.bolt/nut/rod/washer/strengthCompare` |
| `js/calculator-ui.js` | 290 | 计算器界面渲染 | `renderResult()`、`formatResultHTML()` |
| `js/calculator-data.js` | 112 | 材质密度表、强度表 | `MATERIAL_DENSITY`、`STRENGTH_GRADES` |
| `js/specs-data.js` | 112 | BSW/UNC/UNF/Metric 规格表 | `specsData.bsw/unc/unf/metric` |
| `js/product-images.js` | 102 | 100 SKU → SVG 路径映射 | `productImages['B001']` 等 |

### 🟡 图片资源

| 文件夹 | 数量 | 用途 |
|--------|------|------|
| `images/*.svg` | 36 张 | v3.2 拟真 SVG（备用，所有 SKU 共享）|
| `images/per-sku/*.svg` | 100 张 | **v3.3 唯一 SVG**，每张按实际规格缩放 + 内嵌规格标签 |

### ⚪ 工具脚本（不用看，只是开发时生成 SVG）

- `gen_svgs.py` — 基础 SVG 生成器（已废弃）
- `gen_photos.py` — v3.1 增强 SVG 生成器（已废弃）
- `gen_photos_v2.py` — v3.2 拟真 SVG 生成器（已废弃）
- `gen_per_sku.py` — v3.3 唯一 SVG 生成器

---

## 三、关键代码片段

### 1. 产品数据结构（`js/products-data.js`）

```javascript
// 100 个 SKU，每条记录 9 个字段
{ id: 'B001',                  // SKU 编号（决定排序）
  cat: 'bolts',                // 分类（bolts / nuts / rods / misc）
  series: 'hex',               // 系列（hex / socket / flange 等）
  name_zh: '六角头螺栓 (半牙)', // 中文名
  name_en: 'Hex Bolt (Half Thread)', // 英文名
  std: 'DIN 933 / ISO 4017',   // 执行标准
  spec: 'M6 × 20 × 8.8',      // 规格（直径×长度×强度）
  mat: '8.8级 合金钢',         // 材质（tMat 翻译）
  surface: '镀锌',             // 表面处理（tSurface 翻译）
  icon: '🔩'                   // 备用 emoji
}
```

**4 个分类的分布**：

| cat | 数量 | ID 范围 |
|-----|------|---------|
| bolts | 30 | B001-B030 |
| nuts | 28 | N001-N028 |
| rods | 12 | R001-R012 |
| misc | 30 | F001-F030 |

**修改建议**：
- 加新产品 → 复制一条改 id/name/std/spec/mat/surface
- 改翻译 → 改 name_zh / name_en
- 改分类分布 → 改 cat 字段

---

### 2. 翻译系统（`js/i18n.js`）

#### 2.1 主翻译对象

```javascript
const translations = {
    zh: { 'nav.home': '首页', 'nav.products': '产品', ... },  // 255 keys
    en: { 'nav.home': 'Home', 'nav.products': 'Products', ... }  // 255 keys
};
```

#### 2.2 核心 t() 函数

```javascript
function t(key, params) {
    let v = (translations[currentLang] || {})[key] || key;
    if (params && typeof v === 'string') {
        // 支持参数替换：t('pc.shown', {shown: 24, total: 100, remain: 76})
        for (const k in params) {
            v = v.split('{' + k + '}').join(params[k]);
        }
    }
    return v;
}
```

#### 2.3 4 个翻译辅助函数

```javascript
// 材质：'8.8级 合金钢' → '8.8 Grade Alloy Steel'
function tMat(zh) { return (currentLang === 'en' && matEnMap[zh]) || zh; }

// 表面：'镀锌' → 'Zinc Plated'
function tSurface(zh) { return (currentLang === 'en' && surfaceEnMap[zh]) || zh; }

// 筛选器：'碳钢' → 'Carbon Steel'
function tMatFilter(zh) { return (currentLang === 'en' && matFilterEnMap[zh]) || zh; }

// 规格：'M8 × 8.8 配用' → 'M8 × 8.8 Match'
// 规格：'M8 × 8级' → 'M8 × Grade 8'
// 规格：'Ø10mm 轴用' → 'Ø10mm Shaft'
function tSpec(zh) { /* 见源文件 666-685 行 */ }
```

#### 2.4 setLanguage() 切换流程

```javascript
function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('jingong-lang', lang);  // 记住用户选择
    
    // 1. 替换所有 data-i18n 元素
    document.querySelectorAll('[data-i18n]').forEach(el => {
        el.textContent = t(el.dataset.i18n);
    });
    
    // 2. 替换所有 data-i18n-placeholder 输入框
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        el.placeholder = t(el.dataset.i18nPlaceholder);
    });
    
    // 3. 翻译 select 选项（data-i18n-options）
    document.querySelectorAll('[data-i18n-options]').forEach(select => {
        const mapKey = select.dataset.i18nOptions;
        Array.from(select.options).forEach(opt => {
            const map = i18nOptionMap[mapKey]?.[opt.value];
            if (map) opt.textContent = map[lang];
        });
    });
    
    // 4. 重新渲染产品卡（动态内容需要重画）
    if (typeof renderProducts === 'function') renderProducts(true);
    
    // 5. 更新 <html lang="...">
    document.documentElement.lang = lang;
}
```

**修改建议**：
- 加新文案 → 在 zh 和 en 里都加一行 `'key': 'value'`
- HTML 里加 `data-i18n="key"` 自动翻译
- 翻译键统一前缀：`nav.*` / `hero.*` / `pc.*` / `calc.*` / `filter.*` / `footer.*`

---

### 3. 产品渲染（`js/main.js`）

#### 3.1 筛选逻辑（`applyFilters`，316-345 行）

```javascript
function applyFilters() {
    filteredProducts = products.filter(p => {
        // 4 维筛选：分类 + 标准 + 材质 + 搜索
        if (filterState.cat !== 'all' && p.cat !== filterState.cat) return false;
        if (filterState.std !== 'all' && getStdType(p.std) !== filterState.std) return false;
        if (filterState.mat !== 'all' && getMaterialType(p.mat) !== filterState.mat) return false;
        if (filterState.search) {
            const q = filterState.search.toLowerCase();
            const hay = `${p.name_zh} ${p.name_en} ${p.spec} ${p.std} ${p.mat} ${p.id}`.toLowerCase();
            if (!hay.includes(q)) return false;
        }
        return true;
    });

    // 3 种排序：ID / 名称 / 分类
    if (filterState.sort === 'id-asc') {
        filteredProducts.sort((a, b) => a.id.localeCompare(b.id));
    } else if (filterState.sort === 'name-asc') {
        // ...
    } else if (filterState.sort === 'cat-asc') {
        filteredProducts.sort((a, b) => a.cat.localeCompare(b.cat) || a.id.localeCompare(b.id));
    }

    renderProducts(true);  // 重渲染（reset = true）
}
```

#### 3.2 产品卡渲染（`renderProductCard`，226 行）

```javascript
function renderProductCard(p) {
    const name = currentLang === 'en' ? p.name_en : p.name_zh;
    const imgPath = (typeof productImages !== 'undefined' && productImages[p.id]) || null;
    const imgHtml = imgPath
        ? `<img src="${imgPath}" alt="${name}" class="pc-img" loading="lazy" 
                onerror="this.outerHTML='<span class=\\'pc-icon\\'>${p.icon || '🔩'}</span>'">`
        : `<span class="pc-icon">${p.icon || '🔩'}</span>`;
    return `
        <article class="product-card" data-id="${p.id}">
            <div class="pc-image">${imgHtml}</div>
            <div class="pc-head">
                <span class="pc-sku">${p.id}</span>
                <span class="pc-std">${p.std}</span>
            </div>
            <h3 class="pc-name">${name}</h3>
            <ul class="pc-info">
                <li><strong>${pcSpecLabel()}</strong><span>${tSpec(p.spec)}</span></li>
                <li><strong>${pcMaterialLabel()}</strong><span>${tMat(p.mat)}</span></li>
                <li><strong>${pcSurfaceLabel()}</strong><span>${tSurface(p.surface)}</span></li>
            </ul>
            <div class="pc-action">
                <a href="#rfq" class="pc-btn pc-btn-outline" data-sku="${p.id}">${t('pc.detail')}</a>
                <a href="#rfq" class="pc-btn pc-btn-primary" data-sku="${p.id}">${t('pc.inquire')}</a>
            </div>
        </article>
    `;
}
```

#### 3.3 分页（`renderProducts`，254 行）

```javascript
const ITEMS_PER_PAGE = 24;  // 每页 24 个

function renderProducts(reset = false) {
    const grid = document.getElementById('productGrid');
    const loadBtn = document.getElementById('loadMoreBtn');
    const hint = document.getElementById('moreHint');

    if (reset) { grid.innerHTML = ''; displayedCount = 0; }

    const next = filteredProducts.slice(displayedCount, displayedCount + ITEMS_PER_PAGE);
    
    // ... 空状态处理 ...
    
    const html = next.map(renderProductCard).join('');
    if (reset) { grid.innerHTML = html; } else { grid.insertAdjacentHTML('beforeend', html); }
    
    displayedCount += next.length;
    
    // 更新加载按钮
    if (displayedCount >= filteredProducts.length) {
        loadBtn.style.display = 'none';
        hint.textContent = t('pc.shown', {shown: displayedCount, total: filteredProducts.length, remain: 0});
    } else {
        hint.textContent = t('pc.shown', {shown: displayedCount, total: filteredProducts.length, remain: filteredProducts.length - displayedCount});
    }
}
```

---

### 4. 计算引擎（`js/calculator-engine.js`）

5 个计算器共享同一套核心算法：

```javascript
const CalcEngine = {
    // 螺栓：d=直径, L=长度, mat=材质, grade=强度等级
    bolt(d, L, mat, grade) { /* 体积、重量、强度 */ },
    
    // 螺母：d=螺纹直径, m=高度, mat=材质
    nut(d, m, mat) { /* 体积、重量 */ },
    
    // 螺杆：d=直径, L=长度, mat=材质
    rod(d, L, mat) { /* 体积、重量 */ },
    
    // 垫圈：d1=内径, d2=外径, h=厚度, mat=材质
    washer(d1, d2, h, mat) { /* 体积、重量 */ },
    
    // 强度对比：bolt vs nut 在同一规格下哪个先失效
    strengthCompare(d, grade, mat) { /* 比较两者强度极限 */ }
};
```

**公式**（基于 ISO 898-1）：

```javascript
// 螺栓抗拉强度 (N)
σ_b = 800 MPa (8.8 级) × A_s

// A_s = 应力截面积 (mm²)
A_s = (π/4) × ((d/2 + d/2×0.9382)²)   // 简化

// 重量 (g)
weight = volume_mm³ × density_g/cm³ / 1000

// 密度表 (g/cm³)
const MATERIAL_DENSITY = {
    '8.8级 合金钢': 7.85,
    '10.9级 合金钢': 7.85,
    'A2-70 不锈钢': 7.93,
    'A4-80 不锈钢': 7.93,
    'C1022 碳钢': 7.85,
    'H62 黄铜': 8.43
};
```

---

### 5. CSS 设计系统（`css/style.css`）

#### 5.1 配色变量（`:root`，13 行起）

```css
:root {
    --bg-deep: #0a0d14;          /* 最深背景 */
    --bg-dark: #11151d;          /* 次背景 */
    --bg-card: #1a1f2b;          /* 卡片背景 */
    --bg-card-hover: #232938;    /* 悬停态 */
    --bg-elevated: #2a3140;      /* 凸起元素 */
    --text-primary: #e8ecf3;     /* 主文字 */
    --text-secondary: #a8b0c0;   /* 次文字 */
    --text-muted: #6b7385;       /* 弱化文字 */
    --accent-orange: #f7811a;    /* 主品牌色（按钮/重点）*/
    --accent-amber: #ff8c42;     /* 渐变次色 */
    --accent-blue: #4d92e8;      /* 信息/链接 */
    --accent-green: #3fb950;     /* 成功 */
    --accent-red: #f85149;       /* 错误 */
}
```

**深色工业风**配色思路：钢蓝 + 橙金，强调工程感。

#### 5.2 响应式断点（3 处 @media）

| 断点 | 行号 | 触发场景 |
|------|------|---------|
| `@media (max-width: 968px)` | 1055, 2278 | 平板竖屏：导航变汉堡、Hero 单列 |
| `@media (max-width: 640px)` | 1091, 2414 | 手机：产品卡单列、统计 2×2、计算器横滚 |
| `@media (max-width: 380px)` | 2493 | iPhone SE：字体缩小、隐藏 logo-en |

#### 5.3 产品卡（`.product-card`）

```css
.product-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px;
    transition: all 0.3s;
}
.product-card:hover {
    border-color: var(--accent-orange);
    transform: translateY(-2px);
}
.pc-img {
    width: 100%;
    height: 140px;          /* 移动端 */
    object-fit: contain;
}
```

---

## 四、HTML 结构（`index.html`）

11 个 `<section>`，按文档顺序：

```html
<body>
  <nav>             <!-- 顶部导航 + 语言切换 -->
  <header>          <!-- Hero 区：标题 + CTA + 大螺栓 SVG -->
  <section id="stats">       <!-- 4 个数字统计 -->
  <section id="products">    <!-- 产品目录（100 SKU）-->
  <section id="specs">       <!-- 规格表（4 套标准）-->
  <section id="materials">   <!-- 材质说明 -->
  <section id="capacity">    <!-- 产能 / 月产 / 出口国家 -->
  <section id="certifications"> <!-- 认证：ISO 9001 / CE / RoHS 等 -->
  <section id="calculator">  <!-- 5 个在线计算器 -->
  <section id="about">       <!-- 关于我们 / 公司介绍 -->
  <section id="rfq">         <!-- 询价表单 -->
  <footer>          <!-- 4 列：产品 / 标准 / 联系 / 订阅 -->
</body>
```

**修改建议**：
- 改 Hero 文案 → `<header>` 里的 `<h1>` / `<p>`（记得加 data-i18n）
- 加新 section → 复制一段 `<section>` 改 id 和内容
- 改导航 → `<nav>` 里的 `<a class="nav-link" data-i18n="nav.xxx">`

---

## 五、如何修改常见内容

### 🛠 加 1 个新产品

```javascript
// 编辑 js/products-data.js，在 PRODUCTS 数组末尾加一条：
{
    id: 'B031',                                 // 新 SKU
    cat: 'bolts',
    series: 'hex',
    name_zh: '六角头螺栓 (加长型)',
    name_en: 'Hex Bolt (Extra Long)',
    std: 'DIN 933 / ISO 4017',
    spec: 'M12 × 100 × 8.8',
    mat: '8.8级 合金钢',
    surface: '镀锌',
    icon: '🔩'
}
```

然后：
1. 在 `js/product-images.js` 加一行：`'B031': 'images/per-sku/B031.svg',`
2. 把对应 SVG 放到 `images/per-sku/B031.svg`（或先用共享 SVG）
3. 在 `js/products-data.js` 顶部数组 `const PRODUCTS = [...]` 的注释里更新计数

### 🛠 改产品文案

直接编辑 `js/products-data.js` 里的 `name_zh` / `name_en` / `spec` / `std` 字段即可。无需重启服务，刷新页面就生效。

### 🛠 改网站文字（中英双语）

1. 找到对应元素（HTML 里搜索 `data-i18n="..."`）
2. 在 `js/i18n.js` 的 `zh: {...}` 和 `en: {...}` 两个对象里都加 `'new.key': 'value'`

例如加一个 "Quality Guaranteed"：
```javascript
// 在 zh 块加：
'about.quality': '品质保证',
// 在 en 块加：
'about.quality': 'Quality Guaranteed',
// 在 HTML 加：
<p data-i18n="about.quality"></p>
```

### 🛠 改配色

编辑 `css/style.css` 的 `:root` 变量（前 25 行）。改一个变量全站生效：
```css
--accent-orange: #f7811a;   /* 改成你喜欢的颜色 */
```

### 🛠 加新计算器

1. 在 `js/calculator-engine.js` 的 `CalcEngine` 对象加新方法（如 `flange()`）
2. 在 `js/calculator-data.js` 加新数据表
3. 在 `js/calculator-ui.js` 加渲染函数
4. 在 `index.html` 的 `#calculator` section 加一个新 tab

### 🛠 改产品图

**临时方案**：在 `js/product-images.js` 改路径：
```javascript
'B001': 'images/your-photo.jpg',   // 改成你自己的图
```

**永久方案**：把图放到 `images/per-sku/B001.jpg`，文件名跟 SKU 对应，路径用绝对路径。

---

## 六、部署指南

### 方式 A：GitHub Pages（推荐）

仓库：`x8888xclub/jingong-fasteners-website`

```bash
# 1. 拉取最新代码
git clone https://github.com/x8888xclub/jingong-fasteners-website.git
cd jingong-fasteners-website

# 2. 本地预览
python3 -m http.server 8000
# 打开 http://localhost:8000

# 3. 修改后提交
git add .
git commit -m "改了点东西"
git push origin main
# 几分钟后 https://x8888xclub.github.io/jingong-fasteners-website/ 自动更新
```

### 方式 B：本地 HTML 直接打开

```bash
# 直接双击 index.html 也能看（部分功能需要服务器，但展示没问题）
open index.html
```

### 方式 C：部署到自有服务器

```bash
# 上传整个项目文件夹到服务器
scp -r ./* user@server:/var/www/jingong/
# Nginx 配一个 server block 指向该目录
```

---

## 七、版本历史

| 版本 | 日期 | 关键改动 |
|------|------|---------|
| v1.0 | 2026-08-18 | 完整 HTML/CSS/JS 双语站，11 区块 |
| v2.0 | 2026-08-19 | 100 SKU 产品目录 + 筛选/搜索/排序/分页 |
| v2.1 | 2026-08-19 | 36 张 SVG 技术示意图 |
| v3.0 | 2026-08-19 | 5 个在线计算器（螺栓/螺母/螺杆/垫圈/强度）|
| v3.1 | 2026-08-19 | 增强版 36 SVG（3D 透视 + 金属渐变）|
| v3.2 | 2026-08-19 | 拟真 SVG（HSL 渐变 + 颗粒 + 景深模糊）|
| v3.3 | 2026-08-20 | **100 唯一 SVG + 规格标签**（每 SKU 一张图）|
| v3.4 | 2026-08-20 | 移动端优化（汉堡菜单 + 单列卡 + Hero 压缩）|
| **v3.5** | **2026-08-20** | **英文翻译全面修复（247→9 处，96% 修复）**|

### v3.5 关键 bug 修复

**问题**：i18n.js 的 `brand.cn` 键错位（放在 zh 和 en 块之间），导致整个 JS 文件解析失败 → 所有 `translations` 都未加载 → 切英文完全无效。

**修复**：
- 移除错位的 `brand.cn`，正确放进 zh 和 en 块
- 增强 `t()` 函数支持 `{key}` 参数替换
- 添加 `tMat/tSurface/tMatFilter/tSpec` 4 个翻译辅助函数
- 4 个材质 filter + 4 个计算器 select 加 `data-i18n-options`
- specs-data.js 残留中文：`'A4-80 不锈钢'` → `'A4-80 Stainless Steel'`

---

## 八、已知问题与待办

### 🟡 当前已知问题（不严重，可接受）

1. **SVG 是矢量图，不是真实照片** — 等待晓白提供 5-10 张手机实拍图后可替换
2. **公司名是占位符** — "精工固件 Jingong Fasteners" 等晓白确认
3. **联系信息是占位符** — 地址/电话/邮箱待晓白提供
4. **询价表单无后端** — 现在点了没反应，需要后端收邮件 / 微信通知

### 🔵 后续可加的功能

| 功能 | 工作量 | 优先级 |
|------|--------|--------|
| 真实产品图替换 SVG | 1 小时（晓白拍照后）| ⭐⭐⭐⭐⭐ |
| 真实公司信息 | 5 分钟 | ⭐⭐⭐⭐⭐ |
| PDF 导出计算结果 | 2 小时 | ⭐⭐⭐ |
| 计算历史（localStorage）| 1 小时 | ⭐⭐ |
| 询价邮件发送 | 2 小时 + 后端 | ⭐⭐⭐ |
| 产品详情页 | 3 小时 | ⭐⭐ |
| 对比模式 | 2 小时 | ⭐⭐ |

---

## 九、关键技术细节

### 9.1 100 张 SVG 的生成逻辑（`gen_per_sku.py`）

```python
# 36 种基础渲染类型
TYPES = ['hex_bolt', 'socket_cap', 'carriage', 't_bolt', 'anchor', 
        'hex_nut', 'lock_nut', 'flange_nut', 'wing_nut', 
        'threaded_rod', 'stud_1end', 'stud_2end',
        'flat_washer', 'spring_washer', 'cotter_pin', ...]

# 按实际规格缩放
def d_to_px(d, scale=3.6):
    return max(20, min(72, d * scale))  # 头宽 20-72 px

def L_to_px(L):
    return max(40, min(360, L * 2.2))   # 长度 40-360 px

# 每张 SVG 嵌入规格标签
def spec_overlay(sku_id, spec, std_short, grade_short):
    # 左上：橙色 SKU 徽章
    # 右上：白色规格标签
```

### 9.2 移动端汉堡菜单 CSS

```css
.menu-toggle {
    display: none;
}
@media (max-width: 968px) {
    .menu-toggle {
        display: flex;       /* 显示汉堡按钮 */
    }
    .nav-menu {
        position: fixed;
        top: 60px;
        right: -100%;         /* 默认隐藏 */
        width: 280px;
        height: calc(100vh - 60px);
        background: var(--bg-dark);
        transition: right 0.3s;
    }
    .nav-menu.open {
        right: 0;             /* 打开状态 */
    }
}
```

### 9.3 双 CDN 镜像（中国访问）

```bash
# 国内访问 GitHub Pages 不稳定，可以用 ghproxy 镜像
https://ghproxy.com/https://github.com/x8888xclub/jingong-fasteners-website/releases/download/{tag}/{file}
```

---

## 十、自检清单（部署前过一遍）

- [ ] 在 PC 端（1440px）查看：导航、Hero、产品卡、计算器、询价表单是否正常
- [ ] 在手机（375px）查看：汉堡菜单、产品卡单列、Hero 压缩、计算器横滚
- [ ] 切英文（右上角 🌐）：所有中文文案是否翻译
- [ ] 试算计算器：5 个 tab 是否都能算出结果
- [ ] 试筛选：4 维筛选 + 搜索 + 排序 + 加载更多
- [ ] 查 console（F12）：无 JS 报错、无 404
- [ ] 移动端断网测试：手机信号弱时也能正常浏览（纯静态）

---

**报告完成。**

如果你想看某个文件的完整源码，告诉我，我直接贴出来。
如果你想改某个东西，也告诉我具体需求，我帮你改。

🐭