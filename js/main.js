// ===== 导航栏滚动效果 =====
const navbar = document.getElementById('navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 30) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// ===== 移动端菜单 =====
const menuToggle = document.getElementById('menuToggle');
const navMenu = document.getElementById('navMenu');

menuToggle.addEventListener('click', () => {
    navMenu.classList.toggle('open');
});

document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('open');
    });
});

// ===== 当前导航高亮 =====
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');

function highlightNav() {
    const scrollPos = window.pageYOffset + 120;
    sections.forEach(section => {
        const top = section.offsetTop;
        const height = section.offsetHeight;
        const id = section.getAttribute('id');
        if (scrollPos >= top && scrollPos < top + height) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${id}`) {
                    link.classList.add('active');
                }
            });
        }
    });
}

window.addEventListener('scroll', highlightNav);

// ===== 语言切换器 =====
document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const targetLang = btn.dataset.lang;
        if (targetLang === currentLang) return;
        btn.classList.add('lang-switching');
        setTimeout(() => btn.classList.remove('lang-switching'), 250);
        setLanguage(targetLang);
    });
});

// ===== 规格表渲染 =====
let currentSpecTab = 'bsw';

function renderSpecTable(tab) {
    currentSpecTab = tab;
    const tbody = document.getElementById('specTableBody');
    const thead = document.querySelector('.spec-table thead tr');
    if (!tbody) return;

    // 表头（多语言）
    const headers = specTableHeaders[currentLang] || specTableHeaders.zh;
    thead.innerHTML = `
        <th>${headers.size}</th>
        <th>${headers.tpi}</th>
        <th>${headers.major}</th>
        <th>${headers.pitch}</th>
        <th>${headers.tap}</th>
        <th>${headers.strength}</th>
    `;

    // 表体
    const data = specsData[tab];
    if (!data || !data.length) {
        tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;padding:40px;">数据加载中...</td></tr>';
        return;
    }

    tbody.innerHTML = data.map(row => `
        <tr>
            <td class="size-cell">${row.size}</td>
            <td>${row.tpi}</td>
            <td>${row.major.toFixed(3)}</td>
            <td>${row.pitch.toFixed(3)}</td>
            <td>${row.tap.toFixed(2)}</td>
            <td>${row.strength}</td>
        </tr>
    `).join('');
}

// 规格标签切换
document.querySelectorAll('.spec-tab').forEach(tab => {
    tab.addEventListener('click', () => {
        document.querySelectorAll('.spec-tab').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        renderSpecTable(tab.dataset.tab);
    });
});

// 初始渲染
renderSpecTable('bsw');

// ===== RFQ 表单提交 =====
const rfqForm = document.getElementById('rfqForm');

if (rfqForm) {
    rfqForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const btn = rfqForm.querySelector('button[type="submit"]');
        const tip = rfqForm.querySelector('.form-tip');
        const originalText = btn.textContent;
        const originalTip = tip.textContent;

        const successMsg = currentLang === 'zh'
            ? '✓ 询价已提交！我们将在 24 小时内与您联系'
            : '✓ Quote request submitted! We will contact you within 24 hours';
        const pendingMsg = currentLang === 'zh'
            ? '正在提交...'
            : 'Submitting...';

        btn.textContent = pendingMsg;
        btn.disabled = true;

        setTimeout(() => {
            btn.textContent = successMsg;
            btn.style.background = 'linear-gradient(135deg, #3fb950 0%, #2ea043 100%)';
            tip.style.color = 'var(--accent-green)';

            setTimeout(() => {
                rfqForm.reset();
                btn.textContent = originalText;
                btn.style.background = '';
                btn.disabled = false;
                tip.style.color = '';
                tip.textContent = originalTip;
            }, 4000);
        }, 800);
    });
}

// ===== 滚动揭示动画 =====
const revealElements = document.querySelectorAll(
    '.line-card, .mat-card, .cap-card, .cert-card, .ind-card, .spec-table-wrap, .about-features, .factory-card, .rfq-card'
);
revealElements.forEach(el => el.classList.add('reveal'));

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            setTimeout(() => entry.target.classList.add('visible'), index * 50);
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

revealElements.forEach(el => revealObserver.observe(el));

// ===== 平滑滚动 =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#' || href.length < 2) return;
        const target = document.querySelector(href);
        if (target) {
            e.preventDefault();
            const offset = 80;
            const top = target.offsetTop - offset;
            window.scrollTo({ top: top, behavior: 'smooth' });
            navMenu.classList.remove('open');
        }
    });
});

// ===== 控制台彩蛋 =====
console.log(
    '%c✦ 精工固件 Jingong Fasteners · Bilingual Edition',
    'font-family: Inter; font-size: 22px; font-weight: 900; color: #f7811a; padding: 12px 0;'
);
console.log(
    '%c英美标紧固件专业制造商 · BS / ANSI Standard Fastener Manufacturer',
    'color: #f7811a; font-size: 13px;'
);


// ===== 产品目录渲染 =====

const ITEMS_PER_PAGE = 24;
let filteredProducts = [...products];
let displayedCount = 0;

// 判断产品材质类型
function getMaterialType(mat) {
    const m = mat.toLowerCase();
    if (m.includes('a2') || m.includes('a4') || m.includes('304') || m.includes('316') || m.includes('不锈钢')) return 'stainless';
    if (m.includes('c10') || m.includes('c1045') || m.includes('低碳') || m.includes('140hv') || m.includes('碳钢')) return 'carbon';
    if (m.includes('合金') || m.includes('8.8') || m.includes('10.9') || m.includes('12.9') || m.includes('b7') || m.includes('scm') || m.includes('40cr') || m.includes('grade 5') || m.includes('grade 8') || m.includes('弹簧') || m.includes('工具')) return 'alloy';
    return 'other';
}

// 判断产品标准类型
function getStdType(std) {
    const s = std.toUpperCase();
    if (s.includes('DIN') || s.includes('ISO')) return 'DIN';
    if (s.includes('ANSI') || s.includes('ASME') || s.includes('SAE')) return 'ANSI';
    if (s.includes('BS') || s.includes('BSW') || s.includes('BSF')) return 'BS';
    if (s.includes('GB') || s.includes('ASTM')) return 'GB';
    return 'DIN';
}

// 获取翻译 key
const pcMaterialLabel = () => translations[currentLang]['pc.material'] || '材质';
const pcSurfaceLabel = () => translations[currentLang]['pc.surface'] || '表面';
const pcSpecLabel = () => translations[currentLang]['pc.spec'] || '规格';
const pcInquireLabel = () => translations[currentLang]['pc.inquire'] || '询价';

// 渲染产品卡片（含 SVG 图片）
function renderProductCard(p) {
    const name = currentLang === 'en' ? p.name_en : p.name_zh;
    const imgPath = (typeof productImages !== 'undefined' && productImages[p.id]) || null;
    const imgHtml = imgPath
        ? `<img src="${imgPath}" alt="${name}" class="pc-img" loading="lazy" onerror="this.outerHTML='<span class=\'pc-icon\'>${p.icon || '\u{1F529}'}</span>'">`
        : `<span class="pc-icon">${p.icon || '\u{1F529}'}</span>`;
    return `
        <article class="product-card" data-id="${p.id}">
            <div class="pc-image">${imgHtml}</div>
            <div class="pc-head">
                <span class="pc-sku">${p.id}</span>
                <span class="pc-std">${p.std}</span>
            </div>
            <h3 class="pc-name">${name}</h3>
            <ul class="pc-info">
                <li><strong>${pcSpecLabel()}</strong><span>${p.spec}</span></li>
                <li><strong>${pcMaterialLabel()}</strong><span>${p.mat}</span></li>
                <li><strong>${pcSurfaceLabel()}</strong><span>${p.surface}</span></li>
            </ul>
            <div class="pc-action">
                <a href="#rfq" class="pc-btn pc-btn-outline" data-sku="${p.id}">${currentLang === 'en' ? 'Detail' : '详情'}</a>
                <a href="#rfq" class="pc-btn pc-btn-primary" data-sku="${p.id}">${currentLang === 'en' ? 'Inquire' : '询价'}</a>
            </div>
        </article>
    `;
}

// 渲染产品列表（分页）
function renderProducts(reset = false) {
    const grid = document.getElementById('productGrid');
    const loadBtn = document.getElementById('loadMoreBtn');
    const hint = document.getElementById('moreHint');

    if (reset) {
        grid.innerHTML = '';
        displayedCount = 0;
    }

    const next = filteredProducts.slice(displayedCount, displayedCount + ITEMS_PER_PAGE);

    if (displayedCount === 0 && next.length === 0) {
        const emptyIcon = currentLang === 'en' ? '🔍' : '🔍';
        const emptyText = currentLang === 'en' ? 'No products match your filters.' : '没有匹配筛选条件的产品';
        grid.innerHTML = `
            <div class="product-empty">
                <div class="product-empty-icon">${emptyIcon}</div>
                <p>${emptyText}</p>
            </div>
        `;
        loadBtn.style.display = 'none';
        hint.textContent = '';
        return;
    }

    const html = next.map(renderProductCard).join('');
    if (reset) {
        grid.innerHTML = html;
    } else {
        grid.insertAdjacentHTML('beforeend', html);
    }

    displayedCount += next.length;

    // 更新计数
    document.getElementById('resultCount').textContent = filteredProducts.length;

    // 加载更多按钮
    if (displayedCount >= filteredProducts.length) {
        loadBtn.style.display = 'none';
        const total = filteredProducts.length;
        hint.textContent = currentLang === 'en'
            ? `Showing all ${total} products`
            : `已显示全部 ${total} 个产品`;
    } else {
        loadBtn.style.display = '';
        const remaining = filteredProducts.length - displayedCount;
        const showing = currentLang === 'en' ? 'Showing' : '已显示';
        const total = filteredProducts.length;
        const remainText = currentLang === 'en' ? 'remaining' : '个待显示';
        hint.textContent = `${showing} ${displayedCount} / ${total} · ${remaining} ${remainText}`;
    }
}

// 筛选状态
const filterState = {
    cat: 'all',
    std: 'all',
    mat: 'all',
    search: '',
    sort: 'default'
};

// 应用筛选
function applyFilters() {
    filteredProducts = products.filter(p => {
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

    // 排序
    if (filterState.sort === 'id-asc') {
        filteredProducts.sort((a, b) => a.id.localeCompare(b.id));
    } else if (filterState.sort === 'name-asc') {
        filteredProducts.sort((a, b) => {
            const an = currentLang === 'en' ? a.name_en : a.name_zh;
            const bn = currentLang === 'en' ? b.name_en : b.name_zh;
            return an.localeCompare(bn, currentLang === 'zh' ? 'zh' : 'en');
        });
    } else if (filterState.sort === 'cat-asc') {
        filteredProducts.sort((a, b) => a.cat.localeCompare(b.cat) || a.id.localeCompare(b.id));
    }

    renderProducts(true);
    const fc = document.getElementById("filterCount");
    if (fc) fc.textContent = filteredProducts.length;
}

// 筛选按钮
document.querySelectorAll('#filterCat .filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('#filterCat .filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        filterState.cat = btn.dataset.cat;
        applyFilters();
    });
});

document.querySelectorAll('#filterStd .filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('#filterStd .filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        filterState.std = btn.dataset.std;
        applyFilters();
    });
});

document.querySelectorAll('#filterMat .filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('#filterMat .filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        filterState.mat = btn.dataset.mat;
        applyFilters();
    });
});

// 重置
document.getElementById('filterReset').addEventListener('click', () => {
    filterState.cat = 'all';
    filterState.std = 'all';
    filterState.mat = 'all';
    filterState.search = '';
    filterState.sort = 'default';
    document.getElementById('productSearch').value = '';
    document.getElementById('productSort').value = 'default';
    document.querySelectorAll('.filter-btn').forEach(b => {
        b.classList.remove('active');
        const parent = b.closest('.filter-list');
        if (parent.id === 'filterCat' && b.dataset.cat === 'all') b.classList.add('active');
        if (parent.id === 'filterStd' && b.dataset.std === 'all') b.classList.add('active');
        if (parent.id === 'filterMat' && b.dataset.mat === 'all') b.classList.add('active');
    });
    applyFilters();
});

// 搜索（防抖）
let searchTimer;
document.getElementById('productSearch').addEventListener('input', (e) => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {
        filterState.search = e.target.value.trim();
        applyFilters();
    }, 200);
});

// 排序
document.getElementById('productSort').addEventListener('change', (e) => {
    filterState.sort = e.target.value;
    applyFilters();
});

// 加载更多
document.getElementById('loadMoreBtn').addEventListener('click', () => {
    renderProducts(false);
});

// 产品卡片点击 → 询价表单自动填充 SKU
document.getElementById('productGrid').addEventListener('click', (e) => {
    const btn = e.target.closest('[data-sku]');
    if (btn) {
        const sku = btn.dataset.sku;
        setTimeout(() => {
            const descField = document.querySelector('#rfqForm textarea');
            if (descField) {
                const skuPrefix = currentLang === 'en' ? 'Product' : '产品';
                descField.value = `${skuPrefix}: ${sku}\n` + descField.value;
                descField.focus();
            }
        }, 600);
    }
});

// 初始渲染
applyFilters();


// ===== 移动端筛选切换 =====
const filterToggle = document.getElementById('filterToggle');
const catalogFilter = document.querySelector('.catalog-filter');
if (filterToggle && catalogFilter) {
    filterToggle.addEventListener('click', () => {
        catalogFilter.classList.toggle('open');
        filterToggle.classList.toggle('active');
    });
}

// 关闭筛选（点产品卡片或筛选按钮时）
document.querySelectorAll('.catalog-filter .filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        if (window.innerWidth <= 968) {
            // 移动端选择后不关闭，方便连续选
        }
    });
});

// 监听 filter count 实时更新
const filterCountEl = document.getElementById('filterCount');
const updateFilterCount = () => {
    if (filterCountEl) filterCountEl.textContent = filteredProducts.length;
};
const origApplyFilters = applyFilters;
// 包装原函数以更新 count（简单做法：再调一次 updateFilterCount）
