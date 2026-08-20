// ===== 产品数据：100 个 SKU =====
// 4 大类（螺栓 / 螺母 / 螺杆 / 紧固件）+ 多系列 + 多种规格
// 用于产品中心展示，每条产品包含：编号 / 中文名 / 英文名 / 类别 / 系列 / 标准 / 规格 / 材质 / 表面

const productCategories = {
    zh: {
        bolts: '螺栓系列',
        nuts: '螺母系列',
        rods: '螺杆系列',
        misc: '紧固件系列',
        all: '全部产品'
    },
    en: {
        bolts: 'Bolts',
        nuts: 'Nuts',
        rods: 'Threaded Rods',
        misc: 'Fasteners',
        all: 'All Products'
    }
};

const products = [
    // ========== 螺栓系列 (30 个) ==========
    // 六角头螺栓 (10)
    { id: 'B001', cat: 'bolts', series: 'hex', name_zh: '六角头螺栓 (半牙)', name_en: 'Hex Bolt (Half Thread)', std: 'DIN 933 / ISO 4017', spec: 'M6 × 20 × 8.8', mat: '8.8级 合金钢', surface: '镀锌', icon: '�' },
    { id: 'B002', cat: 'bolts', series: 'hex', name_zh: '六角头螺栓 (全牙)', name_en: 'Hex Bolt (Full Thread)', std: 'DIN 933 / ISO 4017', spec: 'M8 × 30 × 8.8', mat: '8.8级 合金钢', surface: '镀锌', icon: '🔩' },
    { id: 'B003', cat: 'bolts', series: 'hex', name_zh: '六角头螺栓 (半牙)', name_en: 'Hex Bolt (Half Thread)', std: 'UNC 1/4"-20 × 1"', spec: '1/4"-20 × 1"', mat: 'Grade 5 碳钢', surface: '镀锌', icon: '🔩' },
    { id: 'B004', cat: 'bolts', series: 'hex', name_zh: '六角头螺栓 (半牙)', name_en: 'Hex Bolt (Half Thread)', std: 'UNC 3/8"-16 × 2"', spec: '3/8"-16 × 2"', mat: 'Grade 8 合金钢', surface: '达克罗', icon: '🔩' },
    { id: 'B005', cat: 'bolts', series: 'hex', name_zh: '六角头螺栓 (半牙)', name_en: 'Hex Bolt (Half Thread)', std: 'BSW 1/2" × 2"', spec: '1/2" × 2"', mat: '8.8级 碳钢', surface: '热浸镀锌', icon: '🔩' },
    { id: 'B006', cat: 'bolts', series: 'hex', name_zh: '六角头螺栓 (半牙)', name_en: 'Hex Bolt (Half Thread)', std: 'UNF 1/2"-20 × 2"', spec: '1/2"-20 × 2"', mat: 'Grade 8 合金钢', surface: '发黑', icon: '🔩' },
    { id: 'B007', cat: 'bolts', series: 'hex', name_zh: '六角头螺栓 (高强度)', name_en: 'Hex Bolt (High-Strength)', std: 'DIN 931 / ASTM A325', spec: 'M16 × 60 × 10.9', mat: '10.9级 合金钢', surface: '达克罗', icon: '🔩' },
    { id: 'B008', cat: 'bolts', series: 'hex', name_zh: '六角头螺栓 (高强度)', name_en: 'Hex Bolt (High-Strength)', std: 'ASTM A490', spec: 'M20 × 80 × 12.9', mat: '12.9级 合金钢', surface: '磷化 + 涂油', icon: '🔩' },
    { id: 'B009', cat: 'bolts', series: 'hex', name_zh: '六角头螺栓 (不锈钢)', name_en: 'Hex Bolt (Stainless)', std: 'DIN 933 / A2-70', spec: 'M10 × 40 × A2-70', mat: 'A2 不锈钢', surface: '本色', icon: '🔩' },
    { id: 'B010', cat: 'bolts', series: 'hex', name_zh: '六角头螺栓 (不锈钢)', name_en: 'Hex Bolt (Stainless)', std: 'DIN 933 / A4-80', spec: 'M12 × 50 × A4-80', mat: 'A4 不锈钢', surface: '本色', icon: '🔩' },

    // 内六角螺栓 (5)
    { id: 'B011', cat: 'bolts', series: 'socket', name_zh: '内六角圆柱头螺栓', name_en: 'Socket Cap Screw', std: 'DIN 912 / ISO 4762', spec: 'M8 × 25 × 12.9', mat: '12.9级 合金钢', surface: '发黑', icon: '🧷' },
    { id: 'B012', cat: 'bolts', series: 'socket', name_zh: '内六角圆柱头螺栓', name_en: 'Socket Cap Screw', std: 'DIN 912 / ISO 4762', spec: 'M10 × 30 × 12.9', mat: '12.9级 合金钢', surface: '发黑', icon: '🧷' },
    { id: 'B013', cat: 'bolts', series: 'socket', name_zh: '内六角沉头螺栓', name_en: 'Socket Countersunk Screw', std: 'DIN 7991 / ISO 10642', spec: 'M6 × 20 × 10.9', mat: '10.9级 合金钢', surface: '发黑', icon: '🧷' },
    { id: 'B014', cat: 'bolts', series: 'socket', name_zh: '内六角圆柱头螺栓 (不锈钢)', name_en: 'Socket Cap Screw (SS)', std: 'DIN 912 / A2-70', spec: 'M6 × 16 × A2-70', mat: 'A2 不锈钢', surface: '本色', icon: '🧷' },
    { id: 'B015', cat: 'bolts', series: 'socket', name_zh: '内六角圆柱头螺栓 (美制)', name_en: 'Socket Cap Screw (US)', std: 'UNC 1/4"-20 × 1"', spec: '1/4"-20 × 1"', mat: 'Grade 8 合金钢', surface: '发黑', icon: '🧷' },

    // 马车/方头/异形螺栓 (5)
    { id: 'B016', cat: 'bolts', series: 'special', name_zh: '马车螺栓 (美制)', name_en: 'Carriage Bolt', std: 'ASME B18.5', spec: '1/2"-13 × 4"', mat: 'Grade 5 碳钢', surface: '热浸镀锌', icon: '⚙️' },
    { id: 'B017', cat: 'bolts', series: 'special', name_zh: '马车螺栓 (公制)', name_en: 'Carriage Bolt', std: 'DIN 603 / ISO 8677', spec: 'M10 × 50 × 8.8', mat: '8.8级 碳钢', surface: '镀锌', icon: '⚙️' },
    { id: 'B018', cat: 'bolts', series: 'special', name_zh: 'T 型螺栓', name_en: 'T-Slot Bolt', std: 'DIN 261', spec: 'M8 × 30 × 8.8', mat: '8.8级 合金钢', surface: '发黑', icon: '⚙️' },
    { id: 'B019', cat: 'bolts', series: 'special', name_zh: 'U 型螺栓 (圆弧)', name_en: 'U-Bolt (Round Bend)', std: 'ASTM A307', spec: 'M12 × 80', mat: 'Grade 2 碳钢', surface: '热浸镀锌', icon: '⚙️' },
    { id: 'B020', cat: 'bolts', series: 'special', name_zh: '地脚螺栓 (弯钩)', name_en: 'Anchor Bolt (Hooked)', std: 'GB/T 799 / ASTM F1554', spec: 'M16 × 300 × 8.8', mat: '8.8级 碳钢', surface: '热浸镀锌', icon: '⚙️' },

    // 法兰/吊环/蝶形螺栓 (5)
    { id: 'B021', cat: 'bolts', series: 'flange', name_zh: '六角法兰面螺栓', name_en: 'Hex Flange Bolt', std: 'DIN 6921', spec: 'M8 × 25 × 8.8', mat: '8.8级 合金钢', surface: '镀锌', icon: '⚡' },
    { id: 'B022', cat: 'bolts', series: 'flange', name_zh: '六角法兰面螺栓 (美制)', name_en: 'Hex Flange Bolt (US)', std: 'SAE J429', spec: '5/16"-18 × 1"', mat: 'Grade 5 碳钢', surface: '镀锌', icon: '⚡' },
    { id: 'B023', cat: 'bolts', series: 'flange', name_zh: '吊环螺栓 (美制)', name_en: 'Eye Bolt (US)', std: 'ASME B18.15', spec: '3/8"-16 × 4"', mat: 'Grade 5 碳钢', surface: '镀锌', icon: '⚡' },
    { id: 'B024', cat: 'bolts', series: 'flange', name_zh: '蝶形螺栓 (镀锌)', name_en: 'Wing Bolt', std: 'DIN 316', spec: 'M10 × 50 × 4.8', mat: '4.8级 碳钢', surface: '镀锌', icon: '�' },
    { id: 'B025', cat: 'bolts', series: 'flange', name_zh: '马车螺栓 (美制圆头)', name_en: 'Round Head Carriage Bolt', std: 'ASME B18.5', spec: '3/8"-16 × 2-1/2"', mat: 'Grade 5 碳钢', surface: '镀锌', icon: '⚡' },

    // 自攻/自钻螺栓 (5)
    { id: 'B026', cat: 'bolts', series: 'self', name_zh: '十字沉头自攻螺丝', name_en: 'Cross Recessed CSK Self-Tapping Screw', std: 'DIN 7982', spec: 'ST4.2 × 16', mat: 'C1022 碳钢', surface: '镀锌', icon: '🪛' },
    { id: 'B027', cat: 'bolts', series: 'self', name_zh: '十字盘头自攻螺丝', name_en: 'Cross Recessed Pan Self-Tapping Screw', std: 'DIN 7981', spec: 'ST4.8 × 25', mat: 'C1022 碳钢', surface: '镀锌', icon: '🪛' },
    { id: 'B028', cat: 'bolts', series: 'self', name_zh: '六角华司自钻螺丝', name_en: 'Hex Washer Self-Drilling Screw', std: 'DIN 7504-K', spec: 'ST5.5 × 32', mat: 'C1022 碳钢', surface: '镀锌', icon: '🪛' },
    { id: 'B029', cat: 'bolts', series: 'self', name_zh: '十字盘头自攻螺丝 (不锈钢)', name_en: 'Pan Self-Tapping Screw (SS)', std: 'DIN 7981 / A2', spec: 'ST4.8 × 19', mat: 'A2 不锈钢', surface: '本色', icon: '🪛' },
    { id: 'B030', cat: 'bolts', series: 'self', name_zh: '六角头自钻螺丝', name_en: 'Hex Head Self-Drilling Screw', std: 'ASME B18.6.4', spec: '#10-16 × 1"', mat: 'C1022 碳钢', surface: '镀锌', icon: '🪛' },

    // ========== 螺母系列 (28 个) ==========
    // 六角螺母 (8)
    { id: 'N001', cat: 'nuts', series: 'hex', name_zh: '六角螺母 (1型)', name_en: 'Hex Nut (Type 1)', std: 'DIN 934 / ISO 4032', spec: 'M8 × 8.8 配用', mat: '8级 碳钢', surface: '镀锌', icon: '�' },
    { id: 'N002', cat: 'nuts', series: 'hex', name_zh: '六角螺母 (1型)', name_en: 'Hex Nut (Type 1)', std: 'DIN 934 / ISO 4032', spec: 'M10 × 8.8 配用', mat: '8级 碳钢', surface: '镀锌', icon: '⬢' },
    { id: 'N003', cat: 'nuts', series: 'hex', name_zh: '六角螺母 (1型)', name_en: 'Hex Nut (Type 1)', std: 'DIN 934 / ISO 4032', spec: 'M12 × 10.9 配用', mat: '10级 合金钢', surface: '发黑', icon: '⬢' },
    { id: 'N004', cat: 'nuts', series: 'hex', name_zh: '六角螺母 (美制)', name_en: 'Hex Nut (US)', std: 'ASME B18.2.2', spec: '1/4"-20 UNC', mat: 'Grade 5 碳钢', surface: '镀锌', icon: '⬢' },
    { id: 'N005', cat: 'nuts', series: 'hex', name_zh: '六角螺母 (美制)', name_en: 'Hex Nut (US)', std: 'ASME B18.2.2', spec: '3/8"-16 UNC', mat: 'Grade 5 碳钢', surface: '镀锌', icon: '⬢' },
    { id: 'N006', cat: 'nuts', series: 'hex', name_zh: '六角螺母 (英制)', name_en: 'Hex Nut (BSW)', std: 'BS 1768 / BSW', spec: '1/2" BSW', mat: '8级 碳钢', surface: '热浸镀锌', icon: '⬢' },
    { id: 'N007', cat: 'nuts', series: 'hex', name_zh: '六角螺母 (不锈钢)', name_en: 'Hex Nut (SS)', std: 'DIN 934 / A2-70', spec: 'M8 × A2-70', mat: 'A2 不锈钢', surface: '本色', icon: '⬢' },
    { id: 'N008', cat: 'nuts', series: 'hex', name_zh: '六角螺母 (不锈钢)', name_en: 'Hex Nut (SS)', std: 'DIN 934 / A4-80', spec: 'M10 × A4-80', mat: 'A4 不锈钢', surface: '本色', icon: '⬢' },

    // 自锁螺母 (5)
    { id: 'N009', cat: 'nuts', series: 'lock', name_zh: '尼龙锁紧螺母 (美制)', name_en: 'Nylon Lock Nut (US)', std: 'ASME B18.16.6', spec: '1/4"-20 UNC', mat: 'Grade 5 碳钢', surface: '镀锌', icon: '�' },
    { id: 'N010', cat: 'nuts', series: 'lock', name_zh: '尼龙锁紧螺母 (公制)', name_en: 'Nylon Lock Nut (DIN)', std: 'DIN 985 / ISO 10512', spec: 'M8 × 8级', mat: '8级 碳钢', surface: '镀锌', icon: '🔒' },
    { id: 'N011', cat: 'nuts', series: 'lock', name_zh: '全金属锁紧螺母', name_en: 'All-Metal Lock Nut', std: 'DIN 980 / ISO 7042', spec: 'M10 × 10级', mat: '10级 合金钢', surface: '发黑', icon: '🔒' },
    { id: 'N012', cat: 'nuts', series: 'lock', name_zh: '尼龙锁紧螺母 (不锈钢)', name_en: 'Nylon Lock Nut (SS)', std: 'DIN 985 / A2', spec: 'M8 × A2-70', mat: 'A2 不锈钢', surface: '本色', icon: '🔒' },
    { id: 'N013', cat: 'nuts', series: 'lock', name_zh: '法兰尼龙锁紧螺母', name_en: 'Nylon Lock Flange Nut', std: 'DIN 6926', spec: 'M10 × 8级', mat: '8级 碳钢', surface: '镀锌', icon: '🔒' },

    // 法兰螺母 (4)
    { id: 'N014', cat: 'nuts', series: 'flange', name_zh: '六角法兰螺母', name_en: 'Hex Flange Nut', std: 'DIN 6923', spec: 'M8 × 8级', mat: '8级 碳钢', surface: '镀锌', icon: '⭕' },
    { id: 'N015', cat: 'nuts', series: 'flange', name_zh: '六角法兰螺母 (美制)', name_en: 'Hex Flange Nut (US)', std: 'SAE J429', spec: '5/16"-18 UNC', mat: 'Grade 5 碳钢', surface: '镀锌', icon: '⭕' },
    { id: 'N016', cat: 'nuts', series: 'flange', name_zh: '六角法兰螺母 (不锈钢)', name_en: 'Hex Flange Nut (SS)', std: 'DIN 6923 / A2', spec: 'M10 × A2-70', mat: 'A2 不锈钢', surface: '本色', icon: '⭕' },
    { id: 'N017', cat: 'nuts', series: 'flange', name_zh: '六角锯齿法兰螺母', name_en: 'Serrated Hex Flange Nut', std: 'DIN 6923 (Serrated)', spec: 'M8 × 8级', mat: '8级 碳钢', surface: '镀锌', icon: '⭕' },

    // 盖帽螺母 (3)
    { id: 'N018', cat: 'nuts', series: 'cap', name_zh: '六角盖帽螺母', name_en: 'Hex Cap Nut', std: 'DIN 917', spec: 'M8 × 8级', mat: '8级 碳钢', surface: '镀锌', icon: '🔘' },
    { id: 'N019', cat: 'nuts', series: 'cap', name_zh: '六角盖帽螺母 (不锈钢)', name_en: 'Hex Cap Nut (SS)', std: 'DIN 917 / A2', spec: 'M10 × A2-70', mat: 'A2 不锈钢', surface: '本色', icon: '🔘' },
    { id: 'N020', cat: 'nuts', series: 'cap', name_zh: '圆头盖帽螺母 (美制)', name_en: 'Acorn Cap Nut (US)', std: 'ASME B18.2.2', spec: '3/8"-16 UNC', mat: 'Grade 5 碳钢', surface: '镀锌', icon: '🔘' },

    // 异形螺母 (8)
    { id: 'N021', cat: 'nuts', series: 'special', name_zh: '四方螺母', name_en: 'Square Nut', std: 'DIN 557', spec: 'M10 × 8级', mat: '8级 碳钢', surface: '热浸镀锌', icon: '�' },
    { id: 'N022', cat: 'nuts', series: 'special', name_zh: '蝶形螺母 (镀锌)', name_en: 'Wing Nut', std: 'DIN 315', spec: 'M10 × 4级', mat: '4级 碳钢', surface: '镀锌', icon: '⬛' },
    { id: 'N023', cat: 'nuts', series: 'special', name_zh: '蝶形螺母 (不锈钢)', name_en: 'Wing Nut (SS)', std: 'DIN 315 / A2', spec: 'M8 × A2-70', mat: 'A2 不锈钢', surface: '本色', icon: '⬛' },
    { id: 'N024', cat: 'nuts', series: 'special', name_zh: 'T 型螺母', name_en: 'T-Slot Nut', std: 'DIN 508', spec: 'M10 × 8级', mat: '8级 碳钢', surface: '发黑', icon: '⬛' },
    { id: 'N025', cat: 'nuts', series: 'special', name_zh: '圆螺母 (开槽)', name_en: 'Slotted Round Nut', std: 'DIN 1804', spec: 'M20 × 8级', mat: '8级 碳钢', surface: '发黑', icon: '⬛' },
    { id: 'N026', cat: 'nuts', series: 'special', name_zh: '焊接螺母 (四方)', name_en: 'Weld Nut (Square)', std: 'DIN 928', spec: 'M8 × 8级', mat: '8级 碳钢', surface: '本色', icon: '⬛' },
    { id: 'N027', cat: 'nuts', series: 'special', name_zh: '拉铆螺母', name_en: 'Riveting Nut', std: 'DIN 7337', spec: 'M6 × 1.0', mat: '铝合金', surface: '本色', icon: '⬛' },
    { id: 'N028', cat: 'nuts', series: 'special', name_zh: '六角螺母 (细牙)', name_en: 'Hex Nut (Fine Thread)', std: 'DIN 934 / UNF', spec: '1/2"-20 UNF', mat: 'Grade 5 碳钢', surface: '镀锌', icon: '⬛' },

    // ========== 螺杆系列 (12 个) ==========
    { id: 'R001', cat: 'rods', series: 'threaded', name_zh: '全螺纹螺杆', name_en: 'Fully Threaded Rod', std: 'DIN 976-1', spec: 'M8 × 1000mm', mat: '4.8级 碳钢', surface: '镀锌', icon: '📏' },
    { id: 'R002', cat: 'rods', series: 'threaded', name_zh: '全螺纹螺杆', name_en: 'Fully Threaded Rod', std: 'DIN 976-1', spec: 'M10 × 1000mm', mat: '8.8级 合金钢', surface: '镀锌', icon: '📏' },
    { id: 'R003', cat: 'rods', series: 'threaded', name_zh: '全螺纹螺杆', name_en: 'Fully Threaded Rod', std: 'DIN 976-1', spec: 'M12 × 1000mm', mat: '8.8级 合金钢', surface: '发黑', icon: '📏' },
    { id: 'R004', cat: 'rods', series: 'threaded', name_zh: '全螺纹螺杆 (高强)', name_en: 'Fully Threaded Rod (High-Strength)', std: 'ASTM A193 B7', spec: 'M16 × 1000mm', mat: 'B7 合金钢', surface: '发黑', icon: '📏' },
    { id: 'R005', cat: 'rods', series: 'threaded', name_zh: '全螺纹螺杆 (高强)', name_en: 'Fully Threaded Rod (High-Strength)', std: 'ASTM A193 B7', spec: 'M20 × 1000mm', mat: 'B7 合金钢', surface: '发黑', icon: '📏' },
    { id: 'R006', cat: 'rods', series: 'threaded', name_zh: '全螺纹螺杆 (美制)', name_en: 'Fully Threaded Rod (US)', std: 'ASME B18.31.3', spec: '1/2"-13 × 36"', mat: 'Grade B7 合金钢', surface: '发黑', icon: '📏' },
    { id: 'R007', cat: 'rods', series: 'threaded', name_zh: '全螺纹螺杆 (美制)', name_en: 'Fully Threaded Rod (US)', std: 'ASME B18.31.3', spec: '3/4"-10 × 36"', mat: 'Grade B7 合金钢', surface: '发黑', icon: '📏' },
    { id: 'R008', cat: 'rods', series: 'threaded', name_zh: '全螺纹螺杆 (不锈钢)', name_en: 'Fully Threaded Rod (SS)', std: 'DIN 976 / A2', spec: 'M10 × 1000mm', mat: 'A2 不锈钢', surface: '本色', icon: '📏' },
    { id: 'R009', cat: 'rods', series: 'threaded', name_zh: '全螺纹螺杆 (不锈钢)', name_en: 'Fully Threaded Rod (SS)', std: 'DIN 976 / A4', spec: 'M12 × 1000mm', mat: 'A4 不锈钢', surface: '本色', icon: '📏' },
    { id: 'R010', cat: 'rods', series: 'threaded', name_zh: '双头螺柱 (一端螺纹)', name_en: 'Stud Bolt (Thread One End)', std: 'DIN 938', spec: 'M10 × 50 × 8.8', mat: '8.8级 合金钢', surface: '发黑', icon: '📏' },
    { id: 'R011', cat: 'rods', series: 'threaded', name_zh: '双头螺柱 (两端螺纹)', name_en: 'Stud Bolt (Thread Both Ends)', std: 'DIN 939', spec: 'M12 × 60 × 8.8', mat: '8.8级 合金钢', surface: '发黑', icon: '📏' },
    { id: 'R012', cat: 'rods', series: 'threaded', name_zh: '双头螺柱 (美制高强)', name_en: 'Stud Bolt (US High-Strength)', std: 'ASTM A193 B7', spec: '3/4"-10 × 100mm', mat: 'B7 合金钢', surface: '发黑', icon: '📏' },

    // ========== 紧固件系列 (30 个) ==========
    // 平垫圈 (5)
    { id: 'F001', cat: 'misc', series: 'washer', name_zh: '平垫圈 (公制)', name_en: 'Flat Washer (DIN)', std: 'DIN 125 / ISO 7089', spec: 'M8 × 16 × 1.6', mat: '140HV 碳钢', surface: '镀锌', icon: '⊕' },
    { id: 'F002', cat: 'misc', series: 'washer', name_zh: '平垫圈 (公制)', name_en: 'Flat Washer (DIN)', std: 'DIN 125 / ISO 7089', spec: 'M10 × 20 × 2.0', mat: '140HV 碳钢', surface: '镀锌', icon: '⊕' },
    { id: 'F003', cat: 'misc', series: 'washer', name_zh: '平垫圈 (美制)', name_en: 'Flat Washer (US)', std: 'ASME B18.21.1', spec: '1/4" USS', mat: '碳钢', surface: '镀锌', icon: '⊕' },
    { id: 'F004', cat: 'misc', series: 'washer', name_zh: '平垫圈 (美制)', name_en: 'Flat Washer (US)', std: 'ASME B18.21.1', spec: '3/8" USS', mat: '碳钢', surface: '镀锌', icon: '⊕' },
    { id: 'F005', cat: 'misc', series: 'washer', name_zh: '平垫圈 (不锈钢)', name_en: 'Flat Washer (SS)', std: 'DIN 125 / A2', spec: 'M10 × A2', mat: 'A2 不锈钢', surface: '本色', icon: '⊕' },

    // 弹簧垫圈 (3)
    { id: 'F006', cat: 'misc', series: 'washer', name_zh: '弹簧垫圈 (公制)', name_en: 'Spring Lock Washer', std: 'DIN 127', spec: 'M8', mat: '碳钢', surface: '镀锌', icon: '🌀' },
    { id: 'F007', cat: 'misc', series: 'washer', name_zh: '弹簧垫圈 (美制)', name_en: 'Spring Lock Washer (US)', std: 'ASME B18.21.1', spec: '1/4"', mat: '碳钢', surface: '镀锌', icon: '�' },
    { id: 'F008', cat: 'misc', series: 'washer', name_zh: '弹簧垫圈 (不锈钢)', name_en: 'Spring Lock Washer (SS)', std: 'DIN 127 / A2', spec: 'M10 × A2', mat: 'A2 不锈钢', surface: '本色', icon: '🌀' },

    // 销轴 (5)
    { id: 'F009', cat: 'misc', series: 'pin', name_zh: '开口销', name_en: 'Cotter Pin', std: 'DIN 94 / ISO 1234', spec: 'Ø3 × 30mm', mat: '低碳钢', surface: '镀锌', icon: '📍' },
    { id: 'F010', cat: 'misc', series: 'pin', name_zh: '开口销', name_en: 'Cotter Pin', std: 'DIN 94 / ISO 1234', spec: 'Ø5 × 50mm', mat: '低碳钢', surface: '镀锌', icon: '📍' },
    { id: 'F011', cat: 'misc', series: 'pin', name_zh: '圆柱销 (弹性)', name_en: 'Spring Pin (Roll Pin)', std: 'DIN 1481 / ISO 8752', spec: 'Ø6 × 30mm', mat: '弹簧钢', surface: '发黑', icon: '📍' },
    { id: 'F012', cat: 'misc', series: 'pin', name_zh: '圆柱销 (弹性)', name_en: 'Spring Pin (Roll Pin)', std: 'DIN 1481 / ISO 8752', spec: 'Ø10 × 50mm', mat: '弹簧钢', surface: '发黑', icon: '📍' },
    { id: 'F013', cat: 'misc', series: 'pin', name_zh: '圆柱销 (硬性)', name_en: 'Solid Dowel Pin', std: 'DIN 6325 / ISO 8734', spec: 'Ø8 × 40mm', mat: '工具钢', surface: '本色', icon: '📍' },

    // 铆钉 (5)
    { id: 'F014', cat: 'misc', series: 'rivet', name_zh: '沉头铆钉 (公制)', name_en: 'Countersunk Rivet', std: 'DIN 661 / ISO 7721', spec: 'Ø4 × 12mm', mat: '低碳钢', surface: '镀锌', icon: '🔨' },
    { id: 'F015', cat: 'misc', series: 'rivet', name_zh: '沉头铆钉 (美制)', name_en: 'Countersunk Rivet (US)', std: 'ASME B18.1.1', spec: '1/8" × 1/2"', mat: '低碳钢', surface: '镀锌', icon: '🔨' },
    { id: 'F016', cat: 'misc', series: 'rivet', name_zh: '圆头铆钉 (公制)', name_en: 'Round Head Rivet', std: 'DIN 660', spec: 'Ø5 × 20mm', mat: '低碳钢', surface: '镀锌', icon: '🔨' },
    { id: 'F017', cat: 'misc', series: 'rivet', name_zh: '拉铆钉 (铝)', name_en: 'Blind Rivet (Aluminum)', std: 'DIN 7337 / ISO 15977', spec: 'Ø4.8 × 12mm', mat: '铝 + 钢钉', surface: '本色', icon: '🔨' },
    { id: 'F018', cat: 'misc', series: 'rivet', name_zh: '拉铆钉 (不锈钢)', name_en: 'Blind Rivet (SS)', std: 'DIN 7337 / A2', spec: 'Ø4.8 × 12mm', mat: 'A2 不锈钢', surface: '本色', icon: '�' },

    // 挡圈 (4)
    { id: 'F019', cat: 'misc', series: 'ring', name_zh: '外卡簧挡圈', name_en: 'External Retaining Ring', std: 'DIN 471 / ISO 464', spec: 'Ø10mm 轴用', mat: '弹簧钢', surface: '发黑', icon: '⊙' },
    { id: 'F020', cat: 'misc', series: 'ring', name_zh: '外卡簧挡圈', name_en: 'External Retaining Ring', std: 'DIN 471 / ISO 464', spec: 'Ø20mm 轴用', mat: '弹簧钢', surface: '发黑', icon: '⊙' },
    { id: 'F021', cat: 'misc', series: 'ring', name_zh: '内卡簧挡圈', name_en: 'Internal Retaining Ring', std: 'DIN 472 / ISO 464', spec: 'Ø20mm 孔用', mat: '弹簧钢', surface: '发黑', icon: '⊙' },
    { id: 'F022', cat: 'misc', series: 'ring', name_zh: '内卡簧挡圈', name_en: 'Internal Retaining Ring', std: 'DIN 472 / ISO 464', spec: 'Ø40mm 孔用', mat: '弹簧钢', surface: '发黑', icon: '⊙' },

    // 喉箍/卡箍/喉塞 (4)
    { id: 'F023', cat: 'misc', series: 'clamp', name_zh: '英式喉箍', name_en: 'British Hose Clamp', std: 'BS 5315', spec: 'Ø20-30mm', mat: '不锈钢 + 镀锌', surface: '镀锌', icon: '🎯' },
    { id: 'F024', cat: 'misc', series: 'clamp', name_zh: '德式喉箍', name_en: 'German Hose Clamp', std: 'DIN 3017', spec: 'Ø20-30mm', mat: '不锈钢 + 镀锌', surface: '镀锌', icon: '🎯' },
    { id: 'F025', cat: 'misc', series: 'clamp', name_zh: 'T 型螺栓卡箍', name_en: 'T-Bolt Hose Clamp', std: 'SAE J1508', spec: 'Ø50-70mm', mat: '不锈钢 304', surface: '本色', icon: '�' },
    { id: 'F026', cat: 'misc', series: 'clamp', name_zh: '喉箍 (美式)', name_en: 'Hose Clamp (US)', std: 'SAE J1508', spec: 'Ø1-1/2"', mat: '不锈钢 304', surface: '本色', icon: '🎯' },

    // 螺丝/螺栓补充 (4)
    { id: 'F027', cat: 'misc', series: 'bolt', name_zh: '组合螺丝 (公制)', name_en: 'Combination Screw (Bolt+Washer)', std: 'DIN 6901', spec: 'M6 × 30 + 平+弹垫', mat: '8.8级 碳钢', surface: '镀锌', icon: '🔩' },
    { id: 'F028', cat: 'misc', series: 'bolt', name_zh: '内六角螺丝 (薄头)', name_en: 'Low Head Socket Cap Screw', std: 'DIN 7984', spec: 'M6 × 16 × 8.8', mat: '8.8级 合金钢', surface: '发黑', icon: '🔩' },
    { id: 'F029', cat: 'misc', series: 'bolt', name_zh: '铰制孔螺栓', name_en: 'Fitting Bolt (Reamed)', std: 'DIN 609', spec: 'M10 × 40 × 8.8', mat: '8.8级 合金钢', surface: '发黑', icon: '🔩' },
    { id: 'F030', cat: 'misc', series: 'bolt', name_zh: '半圆头方颈螺栓', name_en: 'Cup Head Square Neck Bolt', std: 'DIN 603 / ISO 8677', spec: 'M8 × 40 × 4.8', mat: '4.8级 碳钢', surface: '热浸镀锌', icon: '🔩' },
];

// 验证数量
if (products.length !== 100) {
    console.warn(`⚠️ 产品数量异常: ${products.length}`);
}

// 按类别统计
const productStats = products.reduce((acc, p) => {
    acc[p.cat] = (acc[p.cat] || 0) + 1;
    return acc;
}, {});
