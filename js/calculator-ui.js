// ===== 紧固件计算器 UI 交互 =====

// 标签页切换
document.querySelectorAll('.calc-tab').forEach(tab => {
    tab.addEventListener('click', () => {
        document.querySelectorAll('.calc-tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.calc-panel').forEach(p => p.classList.remove('active'));
        tab.classList.add('active');
        document.getElementById('calc-panel-' + tab.dataset.calc).classList.add('active');
    });
});

// ===== 渲染结果卡片 =====
function renderResult(targetEl, result, type) {
    const html = formatResultHTML(result, type);
    targetEl.innerHTML = html;
    targetEl.classList.add('visible');
    targetEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function formatResultHTML(r, type) {
    const lang = currentLang;
    const L = (zh, en) => lang === 'en' ? en : zh;

    let html = '<div class="result-header">';
    html += `<div class="result-title">${L('� 计算结果', '📊 Results')}</div>`;
    html += `<div class="result-subtitle">${typeLabel(type, lang)}</div>`;
    html += '</div>';

    // 规格参数区
    html += '<div class="result-section">';
    html += `<div class="result-section-title">${L('📐 规格参数', '📐 Specifications')}</div>`;
    html += '<div class="result-grid">';
    Object.entries(r.spec).forEach(([k, v]) => {
        const labelZh = k;
        const labelEn = translateKey(k, lang);
        html += `
            <div class="result-item">
                <div class="result-label">${lang === 'en' ? labelEn : labelZh}</div>
                <div class="result-value">${v}</div>
            </div>
        `;
    });
    html += '</div></div>';

    // 尺寸 / 体积 / 重量（合并）
    if (r.volume || r.weight || r.dimensions) {
        html += '<div class="result-section">';
        html += `<div class="result-section-title">${L('📏 尺寸 · 体积 · 重量', '📏 Dimensions · Volume · Weight')}</div>`;
        html += '<div class="result-grid">';

        if (r.dimensions) {
            Object.entries(r.dimensions).forEach(([k, v]) => {
                const display = formatValue(v);
                html += `
                    <div class="result-item">
                        <div class="result-label">${translateKey('dim.' + k, lang) || k}</div>
                        <div class="result-value">${display}</div>
                    </div>
                `;
            });
        }
        if (r.volume) {
            Object.entries(r.volume).forEach(([k, v]) => {
                html += `
                    <div class="result-item">
                        <div class="result-label">${translateKey('vol.' + k, lang) || k}</div>
                        <div class="result-value">${v}</div>
                    </div>
                `;
            });
        }
        if (r.weight) {
            Object.entries(r.weight).forEach(([k, v]) => {
                html += `
                    <div class="result-item">
                        <div class="result-label">${translateKey('weight.' + k, lang) || k}</div>
                        <div class="result-value">${v}</div>
                    </div>
                `;
            });
        }
        html += '</div></div>';
    }

    // 强度（仅螺栓/强度对比）
    if (r.strength) {
        html += '<div class="result-section result-strength">';
        html += `<div class="result-section-title">${L('💪 力学性能', '💪 Mechanical Strength')}</div>`;
        html += '<div class="result-grid">';
        Object.entries(r.strength).forEach(([k, v]) => {
            if (['material', 'grade'].includes(k)) return;
            html += `
                <div class="result-item">
                    <div class="result-label">${translateKey('str.' + k, lang) || k}</div>
                    <div class="result-value">${typeof v === 'number' ? v.toFixed(2) : v}</div>
                </div>
            `;
        });
        html += '</div></div>';

        if (r.strength.material) {
            const mat = r.strength.material;
            html += `<div class="result-meta">${L('材质：', 'Material:')} ${lang === 'en' ? mat.name_en : mat.name_zh} (${mat.density} g/cm³)</div>`;
        }
    }

    if (r.material && type === 'nut') {
        const mat = r.material;
        html += `<div class="result-meta">${L('材质：', 'Material:')} ${lang === 'en' ? mat.name_en : mat.name_zh} | ${L('密度', 'Density')}: ${mat.density} g/cm³</div>`;
    }
    // 显示材料密度（通用，bolt/rod/washer 都有）
    if (r.strength && r.strength.material) {
        // 已在 strength 区显示过了，避免重复
    } else if (r.material) {
        const mat = r.material;
        const metaDiv = `<div class="result-meta">${L('材质：', 'Material:')} ${lang === 'en' ? mat.name_en : mat.name_zh} | ${L('密度', 'Density')}: ${mat.density} g/cm³</div>`;
        // 找到 result-note 之前插入
        html = html.replace('<div class="result-note">', metaDiv + '<div class="result-note">');
    }

    // 提示
    html += `<div class="result-note">${L('⚠️ 计算基于 ISO 898-1 / DIN 标准，实际请以工程实测为准。', '⚠️ Based on ISO 898-1 / DIN standards. For engineering use, please refer to actual measurements.')}</div>`;

    return html;
}

function formatValue(v) {
    if (typeof v === 'number') {
        if (v < 100) return v.toFixed(2);
        return Math.round(v).toString();
    }
    return v;
}

function typeLabel(type, lang) {
    const labels = {
        bolt: ['六角螺栓 (DIN 933)', 'Hex Bolt (DIN 933)'],
        nut: ['六角螺母 (DIN 934)', 'Hex Nut (DIN 934)'],
        rod: ['全螺纹螺杆 (DIN 976)', 'Threaded Rod (DIN 976)'],
        washer: ['平垫圈 (DIN 125)', 'Flat Washer (DIN 125)'],
        strength: ['力学性能对比', 'Strength Comparison']
    };
    return lang === 'en' ? labels[type][1] : labels[type][0];
}

function translateKey(key, lang) {
    const dict = {
        'dim.totalLength': ['总长 (mm)', 'Total Length (mm)'],
        'dim.headHeight': ['头高 (mm)', 'Head Height (mm)'],
        'dim.shankLength': ['杆长 (mm)', 'Shank Length (mm)'],
        'dim.shankDiameter': ['杆径 (mm)', 'Shank Diameter (mm)'],
        'dim.acrossFlats': ['对边 (mm)', 'Across Flats (mm)'],
        'dim.acrossCorners': ['对角 (mm)', 'Across Corners (mm)'],
        'dim.thickness': ['厚度 (mm)', 'Thickness (mm)'],
        'dim.innerDiameter': ['内径 (mm)', 'Inner Diameter (mm)'],
        'dim.diameter': ['直径 (mm)', 'Diameter (mm)'],
        'dim.length': ['长度 (mm)', 'Length (mm)'],
        'dim.aspectRatio': ['长径比', 'Aspect Ratio'],
        'dim.tensileArea': ['抗拉截面积 (mm²)', 'Tensile Area (mm²)'],
        'vol.headCm3': ['头部体积 (cm³)', 'Head Volume (cm³)'],
        'vol.bodyCm3': ['杆部体积 (cm³)', 'Body Volume (cm³)'],
        'vol.totalCm3': ['总体积 (cm³)', 'Total Volume (cm³)'],
        'vol.totalMm3': ['总体积 (mm³)', 'Total Volume (mm³)'],
        'vol.cm3': ['体积 (cm³)', 'Volume (cm³)'],
        'vol.mm3': ['体积 (mm³)', 'Volume (mm³)'],
        'vol.m3': ['体积 (m³)', 'Volume (m³)'],
        'vol.hexCm3': ['六角体积 (cm³)', 'Hex Volume (cm³)'],
        'vol.holeCm3': ['内孔体积 (cm³)', 'Hole Volume (cm³)'],
        'vol.netCm3': ['净体积 (cm³)', 'Net Volume (cm³)'],
        'weight.grams': ['重量 (g)', 'Weight (g)'],
        'weight.kg': ['重量 (kg)', 'Weight (kg)'],
        'weight.lbs': ['重量 (lbs)', 'Weight (lbs)'],
        'weight.perMeter': ['每米重量 (g/m)', 'Weight per meter (g/m)'],
        'str.tensileArea': ['抗拉截面积 (mm²)', 'Tensile Area (mm²)'],
        'str.tensileLoadKN': ['抗拉承载 (kN)', 'Tensile Load (kN)'],
        'str.yieldLoadKN': ['屈服承载 (kN)', 'Yield Load (kN)'],
        'str.shearLoadKN': ['剪切承载 (kN)', 'Shear Load (kN)'],
        'str.safeLoadKN': ['安全载荷 (kN)', 'Safe Load (kN)'],
        'str.torqueNm': ['推荐力矩 (N·m)', 'Tightening Torque (N·m)']
    };
    if (!dict[key]) return null;
    return lang === 'en' ? dict[key][1] : dict[key][0];
}

// ===== 1. 螺栓计算 =====
const calcBoltBtn = document.getElementById('calcBoltBtn');
if (calcBoltBtn) {
    calcBoltBtn.addEventListener('click', () => {
        const d = parseFloat(document.getElementById('boltD').value);
        const length = parseFloat(document.getElementById('boltL').value);
        const material = document.getElementById('boltMat').value;
        const grade = document.getElementById('boltGrade').value;
        const resultEl = document.getElementById('boltResult');

        try {
            const spec = CalcEngine.findNearestBolt(d);
            const result = CalcEngine.bolt({
                d: spec.d, p: spec.p, k: spec.k, s: spec.s, dk: spec.dk,
                length, material, grade
            });
            renderResult(resultEl, result, 'bolt');
        } catch (e) {
            resultEl.innerHTML = `<div class="result-error">❌ ${e.message}</div>`;
        }
    });
}

// ===== 2. 螺母计算 =====
const calcNutBtn = document.getElementById('calcNutBtn');
if (calcNutBtn) {
    calcNutBtn.addEventListener('click', () => {
        const d = parseFloat(document.getElementById('nutD').value);
        const material = document.getElementById('nutMat').value;
        const resultEl = document.getElementById('nutResult');

        try {
            const spec = CalcEngine.findNearestNut(d);
            const result = CalcEngine.nut({
                d: spec.d, m: spec.m, s: spec.s, material
            });
            renderResult(resultEl, result, 'nut');
        } catch (e) {
            resultEl.innerHTML = `<div class="result-error">❌ ${e.message}</div>`;
        }
    });
}

// ===== 3. 螺杆计算 =====
const calcRodBtn = document.getElementById('calcRodBtn');
if (calcRodBtn) {
    calcRodBtn.addEventListener('click', () => {
        const d = parseFloat(document.getElementById('rodD').value);
        const length = parseFloat(document.getElementById('rodL').value);
        const material = document.getElementById('rodMat').value;
        const resultEl = document.getElementById('rodResult');

        try {
            const result = CalcEngine.rod({ d, length, material });
            renderResult(resultEl, result, 'rod');
        } catch (e) {
            resultEl.innerHTML = `<div class="result-error">❌ ${e.message}</div>`;
        }
    });
}

// ===== 4. 垫圈计算 =====
const calcWasherBtn = document.getElementById('calcWasherBtn');
if (calcWasherBtn) {
    calcWasherBtn.addEventListener('click', () => {
        const d = parseFloat(document.getElementById('washerD').value);
        const material = document.getElementById('washerMat').value;
        const resultEl = document.getElementById('washerResult');

        try {
            const result = CalcEngine.washer({ d, material });
            renderResult(resultEl, result, 'washer');
        } catch (e) {
            resultEl.innerHTML = `<div class="result-error">❌ ${e.message}</div>`;
        }
    });
}

// ===== 5. 强度对比 =====
const calcStrBtn = document.getElementById('calcStrBtn');
if (calcStrBtn) {
    calcStrBtn.addEventListener('click', () => {
        const d = parseFloat(document.getElementById('strD').value);
        const grade = document.getElementById('strGrade').value;
        const type = document.getElementById('strType').value;
        const resultEl = document.getElementById('strResult');

        try {
            const result = CalcEngine.strengthCompare({ d, grade, type });
            renderResult(resultEl, result, 'strength');
        } catch (e) {
            resultEl.innerHTML = `<div class="result-error">❌ ${e.message}</div>`;
        }
    });
}

// ===== 联动：自动设置螺距 =====
document.getElementById('boltD')?.addEventListener('change', (e) => {
    const d = parseFloat(e.target.value);
    if (!isNaN(d)) {
        const spec = CalcEngine.findNearestBolt(d);
        const pitchDisplay = document.getElementById('boltPDisplay');
        if (pitchDisplay) pitchDisplay.textContent = spec.p.toFixed(3) + ' mm';
    }
});
