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
