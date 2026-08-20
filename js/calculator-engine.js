// ===== 紧固件计算引擎 =====
// 基于 ISO 898-1 / DIN 933 / ISO 4017 工程公式

const CalcEngine = {
    // ===== 通用：螺栓杆部抗拉截面面积 =====
    // As = (π/4) × (d - 0.9382p)²  (ISO 898-1 应力截面积公式)
    tensileArea(d, p) {
        return (Math.PI / 4) * Math.pow(d - 0.9382 * p, 2);
    },

    // ===== 螺栓计算 =====
    bolt({ d, p, k, s, dk, length, material, grade }) {
        const mat = MATERIAL_DENSITY[material];
        const grd = STRENGTH_GRADES[grade];
        if (!mat) throw new Error('Material not found: ' + material);
        if (!grd) throw new Error('Grade not found: ' + grade);

        // 体积（mm³）= 头部体积 + 杆部体积
        // 头部（近似圆柱体）= π × (dk/2)² × k
        const headVol = Math.PI * Math.pow(dk / 2, 2) * k;
        // 杆部（螺纹段，简化为光杆）= π × (d/2)² × length
        const bodyVol = Math.PI * Math.pow(d / 2, 2) * length;
        const totalVol = headVol + bodyVol;

        // 重量（克）= 体积(cm³) × 密度(g/cm³)
        // 1 mm³ = 0.001 cm³
        const volCm3 = totalVol * 0.001;
        const weight = volCm3 * mat.density;

        // 抗拉截面积 (mm²)
        const As = this.tensileArea(d, p);

        // 抗拉强度 (N) = As × Rm
        const Fm = As * grd.rm;
        // 屈服强度 (N) = As × Rp
        const Fp = As * grd.rp;
        // 推荐拧紧力矩 (N·m)，K=0.2 拧紧系数
        const torque = 0.2 * Fp * d * 0.001;

        return {
            type: 'bolt',
            input: { d, p, k, s, dk, length, material, grade },
            spec: {
                '大径 d': `${d.toFixed(3)} mm`,
                '螺距 p': `${p.toFixed(3)} mm`,
                '头高 k': `${k.toFixed(2)} mm`,
                '对边 s': `${s.toFixed(2)} mm`,
                '头径 dk': `${dk.toFixed(2)} mm`,
                '长度 L': `${length} mm`
            },
            dimensions: {
                totalLength: length + k,
                headHeight: k,
                shankLength: length,
                shankDiameter: d,
                acrossFlats: s,
                acrossCorners: s * 1.155  // 六角对角 = 对边 × 2/√3
            },
            volume: {
                headCm3: (headVol * 0.001).toFixed(4),
                bodyCm3: (bodyVol * 0.001).toFixed(4),
                totalCm3: volCm3.toFixed(4),
                totalMm3: Math.round(totalVol)
            },
            weight: {
                grams: weight.toFixed(2),
                kg: (weight / 1000).toFixed(4),
                lbs: (weight / 453.592).toFixed(4)
            },
            strength: {
                material: mat,
                grade: grd,
                tensileArea: As.toFixed(3),
                tensileLoadKN: (Fm / 1000).toFixed(2),
                yieldLoadKN: (Fp / 1000).toFixed(2),
                torqueNm: torque.toFixed(2),
                shearLoadKN: ((0.6 * Fm) / 1000).toFixed(2)  // 剪切承载约 60% 抗拉
            }
        };
    },

    // ===== 螺母计算 =====
    nut({ d, m, s, material }) {
        const mat = MATERIAL_DENSITY[material];
        if (!mat) throw new Error('Material not found: ' + material);

        // 体积 = 六角棱柱体积 - 中心孔体积
        // 六角棱柱：s² × m × (√3/2) × 3 / 2 = s² × m × 3√3/4 ≈ 1.299 × s² × m
        const hexVol = 1.299 * s * s * m;
        // 中心孔：π × (d/2)² × m（简化）
        const holeVol = Math.PI * Math.pow(d / 2, 2) * m;
        const netVol = hexVol - holeVol;
        const volCm3 = netVol * 0.001;
        const weight = volCm3 * mat.density;

        return {
            type: 'nut',
            input: { d, m, s, material },
            spec: {
                '螺纹大径 d': `${d.toFixed(2)} mm`,
                '螺母厚度 m': `${m.toFixed(2)} mm`,
                '对边 s': `${s.toFixed(2)} mm`,
                '对角 e': `${(s * 1.155).toFixed(2)} mm`
            },
            dimensions: {
                thickness: m,
                acrossFlats: s,
                acrossCorners: s * 1.155,
                innerDiameter: d
            },
            volume: {
                hexCm3: (hexVol * 0.001).toFixed(4),
                holeCm3: (holeVol * 0.001).toFixed(4),
                netCm3: volCm3.toFixed(4),
                totalMm3: Math.round(netVol)
            },
            weight: {
                grams: weight.toFixed(2),
                kg: (weight / 1000).toFixed(4),
                lbs: (weight / 453.592).toFixed(4)
            },
            material: mat
        };
    },

    // ===== 螺杆计算（按长度）=====
    rod({ d, length, material }) {
        const mat = MATERIAL_DENSITY[material];
        if (!mat) throw new Error('Material not found: ' + material);

        // 体积（光杆简化）= π × (d/2)² × length
        const vol = Math.PI * Math.pow(d / 2, 2) * length;
        const volCm3 = vol * 0.001;
        const weight = volCm3 * mat.density;

        // 单位重量（每米）
        const perMeter = (Math.PI * Math.pow(d / 2, 2) * 1000) * 0.001 * mat.density;

        return {
            type: 'rod',
            input: { d, length, material },
            spec: {
                '直径 d': `${d.toFixed(2)} mm`,
                '长度 L': `${length} mm`,
                '每米重量': `${perMeter.toFixed(3)} g/m`
            },
            dimensions: {
                diameter: d,
                length: length,
                aspectRatio: (length / d).toFixed(2)
            },
            volume: {
                cm3: volCm3.toFixed(4),
                mm3: Math.round(vol),
                m3: (vol * 1e-9).toFixed(6)
            },
            weight: {
                grams: weight.toFixed(2),
                kg: (weight / 1000).toFixed(4),
                lbs: (weight / 453.592).toFixed(4),
                perMeter: perMeter.toFixed(3)
            },
            material: mat
        };
    },

    // ===== 垫圈计算 =====
    washer({ d, material }) {
        const mat = MATERIAL_DENSITY[material];
        if (!mat) throw new Error('Material not found: ' + material);

        const spec = WASHER_METRIC.find(w => w.d === d);
        if (!spec) throw new Error('Washer size not found: M' + d);

        // 体积 = π × ((d2/2)² - (d1/2)²) × h
        const vol = Math.PI * (Math.pow(spec.d2 / 2, 2) - Math.pow(spec.d1 / 2, 2)) * spec.h;
        const volCm3 = vol * 0.001;
        const weight = volCm3 * mat.density;

        // 承压面积（外径 - 内径的环形面积）
        const loadArea = Math.PI * (Math.pow(spec.d2 / 2, 2) - Math.pow(spec.d1 / 2, 2));

        return {
            type: 'washer',
            input: { d, material },
            spec: {
                '适用螺栓': `M${d}`,
                '内径 d1': `${spec.d1.toFixed(2)} mm`,
                '外径 d2': `${spec.d2.toFixed(2)} mm`,
                '厚度 h': `${spec.h.toFixed(2)} mm`
            },
            dimensions: spec,
            volume: {
                cm3: volCm3.toFixed(4),
                mm3: Math.round(vol)
            },
            weight: {
                grams: weight.toFixed(3),
                kg: (weight / 1000).toFixed(5),
                lbs: (weight / 453.592).toFixed(4)
            },
            load: {
                bearingArea: loadArea.toFixed(2),
                unit: 'mm²'
            },
            material: mat
        };
    },

    // ===== 强度对比（给定规格 + 等级）=====
    strengthCompare({ d, grade, type = 'metric' }) {
        const grd = STRENGTH_GRADES[grade];
        if (!grd) throw new Error('Grade not found: ' + grade);

        let p = 0;
        if (type === 'metric') {
            const bolt = BOLT_METRIC.find(b => b.d === d);
            if (!bolt) throw new Error('Bolt size not found: M' + d);
            p = bolt.p;
        } else {
            // 美制：查表
            const bolt = BOLT_IMPERIAL.find(b => b.d === d);
            if (bolt) p = bolt.p;
        }

        const As = p > 0 ? this.tensileArea(d, p) : (Math.PI / 4) * Math.pow(d, 2);

        const Fm = As * grd.rm;
        const Fp = As * grd.rp;
        const torque = 0.2 * Fp * d * 0.001;

        return {
            type: 'strength',
            input: { d, grade, threadType: type, pitch: p },
            spec: {
                '螺纹大径 d': `${d.toFixed(2)} mm`,
                '螺距 p': p ? `${p.toFixed(3)} mm` : 'N/A',
                '强度等级': grd.name_zh + ' / ' + grd.name_en,
                '抗拉强度 Rm': `${grd.rm} MPa`,
                '屈服强度 Rp0.2': `${grd.rp} MPa`
            },
            dimensions: {
                tensileArea: `${As.toFixed(3)} mm²`
            },
            strength: {
                tensileArea: As.toFixed(3),
                tensileLoadKN: (Fm / 1000).toFixed(2),
                yieldLoadKN: (Fp / 1000).toFixed(2),
                torqueNm: torque.toFixed(2),
                shearLoadKN: ((0.6 * Fm) / 1000).toFixed(2),
                safeLoadKN: ((0.5 * Fp) / 1000).toFixed(2)  // 50% 屈服安全系数
            },
            grade: grd
        };
    },

    // ===== 查找最近规格（公制螺栓）=====
    findNearestBolt(d) {
        return BOLT_METRIC.find(b => b.d === d) || BOLT_METRIC.reduce((prev, curr) => {
            return Math.abs(curr.d - d) < Math.abs(prev.d - d) ? curr : prev;
        });
    },

    findNearestNut(d) {
        return NUT_METRIC.find(n => n.d === d) || NUT_METRIC.reduce((prev, curr) => {
            return Math.abs(curr.d - d) < Math.abs(prev.d - d) ? curr : prev;
        });
    }
};
