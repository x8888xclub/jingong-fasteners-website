// ===== 紧固件规格数据 =====
// 数据来源：BS 84 / BS 1083 / ANSI B1.1 / ISO 261 / ISO 724 / DIN 13
// 真实工程数据，仅供参考。具体规格以官方标准为准。

const specsData = {
    // 英式 BSW (British Standard Whitworth) - 粗牙
    bsw: [
        { size: '1/8"', tpi: 40, major: 3.175, pitch: 0.635, tap: 2.55, strength: '4.8 / A2-70' },
        { size: '3/16"', tpi: 24, major: 4.762, pitch: 1.058, tap: 3.86, strength: '4.8 / A2-70' },
        { size: '1/4"', tpi: 20, major: 6.350, pitch: 1.270, tap: 5.10, strength: '4.8 / 8.8 / A2-70' },
        { size: '5/16"', tpi: 18, major: 7.938, pitch: 1.411, tap: 6.56, strength: '4.8 / 8.8 / A2-70' },
        { size: '3/8"', tpi: 16, major: 9.525, pitch: 1.588, tap: 7.90, strength: '8.8 / 10.9 / A2-70' },
        { size: '7/16"', tpi: 14, major: 11.112, pitch: 1.814, tap: 9.30, strength: '8.8 / 10.9' },
        { size: '1/2"', tpi: 12, major: 12.700, pitch: 2.117, tap: 10.60, strength: '8.8 / 10.9 / A4-80' },
        { size: '9/16"', tpi: 12, major: 14.288, pitch: 2.117, tap: 12.20, strength: '8.8 / 10.9' },
        { size: '5/8"', tpi: 11, major: 15.875, pitch: 2.309, tap: 13.50, strength: '8.8 / 10.9 / A4-80' },
        { size: '3/4"', tpi: 10, major: 19.050, pitch: 2.540, tap: 16.50, strength: '10.9 / 12.9 / A4-80' },
        { size: '7/8"', tpi: 9, major: 22.225, pitch: 2.822, tap: 19.50, strength: '10.9 / 12.9' },
        { size: '1"', tpi: 8, major: 25.400, pitch: 3.175, tap: 22.25, strength: '10.9 / 12.9 / A4-80' },
        { size: '1-1/8"', tpi: 7, major: 28.575, pitch: 3.629, tap: 25.00, strength: '12.9' },
        { size: '1-1/4"', tpi: 7, major: 31.750, pitch: 3.629, tap: 28.00, strength: '12.9' },
        { size: '1-1/2"', tpi: 6, major: 38.100, pitch: 4.233, tap: 33.50, strength: '12.9' },
        { size: '2"', tpi: 4.5, major: 50.800, pitch: 5.644, tap: 44.50, strength: '12.9' }
    ],

    // 美式 UNC (Unified National Coarse) - 粗牙
    unc: [
        { size: '#4-40', tpi: 40, major: 2.845, pitch: 0.635, tap: 2.30, strength: '4.8 / A2-70' },
        { size: '#6-32', tpi: 32, major: 3.505, pitch: 0.794, tap: 2.85, strength: '4.8 / A2-70' },
        { size: '#8-32', tpi: 32, major: 4.166, pitch: 0.794, tap: 3.50, strength: '4.8 / A2-70' },
        { size: '#10-24', tpi: 24, major: 4.826, pitch: 1.058, tap: 3.90, strength: '4.8 / 8.8 / A2-70' },
        { size: '1/4"-20', tpi: 20, major: 6.350, pitch: 1.270, tap: 5.11, strength: '4.8 / 8.8 / A2-70' },
        { size: '5/16"-18', tpi: 18, major: 7.938, pitch: 1.411, tap: 6.56, strength: '8.8 / 10.9 / A2-70' },
        { size: '3/8"-16', tpi: 16, major: 9.525, pitch: 1.588, tap: 7.94, strength: '8.8 / 10.9 / A4-80' },
        { size: '7/16"-14', tpi: 14, major: 11.112, pitch: 1.814, tap: 9.30, strength: '8.8 / 10.9' },
        { size: '1/2"-13', tpi: 13, major: 12.700, pitch: 1.954, tap: 10.80, strength: '8.8 / 10.9 / A4-80' },
        { size: '9/16"-12', tpi: 12, major: 14.288, pitch: 2.117, tap: 12.20, strength: '10.9 / 12.9' },
        { size: '5/8"-11', tpi: 11, major: 15.875, pitch: 2.309, tap: 13.60, strength: '10.9 / 12.9 / A4-80' },
        { size: '3/4"-10', tpi: 10, major: 19.050, pitch: 2.540, tap: 16.60, strength: '10.9 / 12.9 / A4-80' },
        { size: '7/8"-9', tpi: 9, major: 22.225, pitch: 2.822, tap: 19.50, strength: '12.9' },
        { size: '1"-8', tpi: 8, major: 25.400, pitch: 3.175, tap: 22.20, strength: '12.9 / A4-80' },
        { size: '1-1/8"-7', tpi: 7, major: 28.575, pitch: 3.629, tap: 25.00, strength: '12.9' },
        { size: '1-1/4"-7', tpi: 7, major: 31.750, pitch: 3.629, tap: 28.00, strength: '12.9' },
        { size: '1-1/2"-6', tpi: 6, major: 38.100, pitch: 4.233, tap: 33.80, strength: '12.9' },
        { size: '2"-4.5', tpi: 4.5, major: 50.800, pitch: 5.644, tap: 45.00, strength: '12.9' }
    ],

    // 美式 UNF (Unified National Fine) - 细牙
    unf: [
        { size: '#4-48', tpi: 48, major: 2.845, pitch: 0.529, tap: 2.40, strength: '4.8 / A2-70' },
        { size: '#6-40', tpi: 40, major: 3.505, pitch: 0.635, tap: 3.00, strength: '4.8 / A2-70' },
        { size: '#8-36', tpi: 36, major: 4.166, pitch: 0.706, tap: 3.60, strength: '4.8 / A2-70' },
        { size: '#10-32', tpi: 32, major: 4.826, pitch: 0.794, tap: 4.10, strength: '4.8 / A2-70' },
        { size: '1/4"-28', tpi: 28, major: 6.350, pitch: 0.907, tap: 5.50, strength: '8.8 / A2-70' },
        { size: '5/16"-24', tpi: 24, major: 7.938, pitch: 1.058, tap: 7.00, strength: '8.8 / A2-70' },
        { size: '3/8"-24', tpi: 24, major: 9.525, pitch: 1.058, tap: 8.50, strength: '8.8 / 10.9 / A4-80' },
        { size: '7/16"-20', tpi: 20, major: 11.112, pitch: 1.270, tap: 9.90, strength: '8.8 / 10.9' },
        { size: '1/2"-20', tpi: 20, major: 12.700, pitch: 1.270, tap: 11.50, strength: '8.8 / 10.9 / A4-80' },
        { size: '9/16"-18', tpi: 18, major: 14.288, pitch: 1.411, tap: 13.00, strength: '10.9 / 12.9' },
        { size: '5/8"-18', tpi: 18, major: 15.875, pitch: 1.411, tap: 14.50, strength: '10.9 / 12.9 / A4-80' },
        { size: '3/4"-16', tpi: 16, major: 19.050, pitch: 1.588, tap: 17.50, strength: '10.9 / 12.9 / A4-80' },
        { size: '7/8"-14', tpi: 14, major: 22.225, pitch: 1.814, tap: 20.50, strength: '12.9' },
        { size: '1"-12', tpi: 12, major: 25.400, pitch: 2.117, tap: 23.50, strength: '12.9 / A4-80' },
        { size: '1-1/8"-12', tpi: 12, major: 28.575, pitch: 2.117, tap: 26.50, strength: '12.9' },
        { size: '1-1/4"-12', tpi: 12, major: 31.750, pitch: 2.117, tap: 29.50, strength: '12.9' },
        { size: '1-1/2"-12', tpi: 12, major: 38.100, pitch: 2.117, tap: 36.00, strength: '12.9' }
    ],

    // 公制 ISO / DIN (Coarse + Fine)
    metric: [
        { size: 'M2', tpi: '0.4', major: 2.000, pitch: 0.40, tap: 1.60, strength: '4.8 / A2-70' },
        { size: 'M2.5', tpi: '0.45', major: 2.500, pitch: 0.45, tap: 2.05, strength: '4.8 / A2-70' },
        { size: 'M3', tpi: '0.5', major: 3.000, pitch: 0.50, tap: 2.50, strength: '4.8 / 8.8 / A2-70' },
        { size: 'M4', tpi: '0.7', major: 4.000, pitch: 0.70, tap: 3.30, strength: '4.8 / 8.8 / A2-70' },
        { size: 'M5', tpi: '0.8', major: 5.000, pitch: 0.80, tap: 4.20, strength: '8.8 / A2-70' },
        { size: 'M6', tpi: '1.0', major: 6.000, pitch: 1.00, tap: 5.00, strength: '8.8 / 10.9 / A2-70' },
        { size: 'M8', tpi: '1.25', major: 8.000, pitch: 1.25, tap: 6.80, strength: '8.8 / 10.9 / A4-80' },
        { size: 'M10', tpi: '1.5', major: 10.000, pitch: 1.50, tap: 8.50, strength: '8.8 / 10.9 / A4-80' },
        { size: 'M12', tpi: '1.75', major: 12.000, pitch: 1.75, tap: 10.20, strength: '10.9 / 12.9 / A4-80' },
        { size: 'M14', tpi: '2.0', major: 14.000, pitch: 2.00, tap: 12.00, strength: '10.9 / 12.9' },
        { size: 'M16', tpi: '2.0', major: 16.000, pitch: 2.00, tap: 14.00, strength: '10.9 / 12.9 / A4-80' },
        { size: 'M18', tpi: '2.5', major: 18.000, pitch: 2.50, tap: 15.50, strength: '12.9' },
        { size: 'M20', tpi: '2.5', major: 20.000, pitch: 2.50, tap: 17.50, strength: '12.9 / A4-80' },
        { size: 'M24', tpi: '3.0', major: 24.000, pitch: 3.00, tap: 21.00, strength: '12.9' },
        { size: 'M30', tpi: '3.5', major: 30.000, pitch: 3.50, tap: 26.50, strength: '12.9' },
        { size: 'M36', tpi: '4.0', major: 36.000, pitch: 4.00, tap: 32.00, strength: '12.9' },
        { size: 'M42', tpi: '4.5', major: 42.000, pitch: 4.50, tap: 37.50, strength: '12.9' },
        { size: 'M48', tpi: '5.0', major: 48.000, pitch: 5.00, tap: 43.00, strength: '12.9' },
        { size: 'M56', tpi: '5.5', major: 56.000, pitch: 5.50, tap: 50.50, strength: '12.9' },
        { size: 'M64', tpi: '6.0', major: 64.000, pitch: 6.00, tap: 58.00, strength: '12.9' }
    ]
};

// 表格列标题（多语言）
const specTableHeaders = {
    zh: {
        size: '规格',
        tpi: '牙数/TPI',
        major: '大径 (mm)',
        pitch: '螺距 (mm)',
        tap: '攻丝 (mm)',
        strength: 'Recommended Strength'
    },
    en: {
        size: 'Size',
        tpi: 'TPI',
        major: 'Major Dia (mm)',
        pitch: 'Pitch (mm)',
        tap: 'Tap Drill (mm)',
        strength: 'Recommended Grade'
    }
};
