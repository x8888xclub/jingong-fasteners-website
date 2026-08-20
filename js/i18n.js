// ===== Lumiq Hardware i18n 中英双语翻译 =====

const translations = {
    zh: {
        // Meta
        'page.title': '精工固件 Jingong - 专业英美标螺丝螺帽螺杆制造商',
        'page.desc': '精工固件 - 专业生产符合英式 BSW/BSF、美式 UNC/UNF/UNEF 规格的螺丝、螺帽、螺杆。ISO 9001 / IATF 16949 认证工厂，支持 OEM/ODM。',

        // Topbar
        'topbar.text': '📦 工厂直供 · 支持 OEM/ODM · 全球发货',
        'topbar.hotline': '销售热线:',

        // Nav
        'nav.home': '首页',
        'nav.products': '产品中心',
        'nav.specs': '规格标准',
        'nav.material': '材质工艺',
        'nav.capacity': '生产能力',
        'nav.cert': '认证资质',
        'nav.about': '关于我们',
        'nav.rfq': '立即询价',

        // Hero
        'hero.title.l1': '英美标紧固件',
        'hero.title.l2': '专业制造商',
        'hero.subtitle': 'BSW · BSF · UNC · UNF · UNEF 全规格覆盖<br>从 M2 到 M64，从 #0 到 4" — 完整公制 + 英制螺纹解决方案',
        'hero.stat.exp': '行业经验',
        'hero.stat.country': '出口国家',
        'hero.stat.sku': 'SKU 现货',
        'hero.stat.qa': '合格率',
        'hero.cta.rfq': '📋 立即询价（RFQ）→',
        'hero.cta.specs': '查看规格表',

        // Products
        'products.tag': '产品中心',
        'products.title.l1': '产品目录',
        'products.title.l2': '100 个 SKU',
        'products.desc': '从基础标准件到定制非标件，覆盖螺栓、螺母、螺杆、紧固件全系列，4 大类 · 8 子系列 · 100 SKU 现货，支持来图来样定制。',
        'line.screws.name': '六角螺栓 / Hex Bolts',
        'line.screws.desc': 'DIN 933 / ISO 4017 / UNC / UNF 全规格，强度等级 4.8-12.9',
        'line.nuts.name': '六角螺母 / Hex Nuts',
        'line.nuts.desc': 'DIN 934 / ISO 4032 / 美制 / 英制全规格，含自锁 / 法兰 / 盖帽系列',
        'line.studs.name': '双头螺杆 / Threaded Rods',
        'line.studs.desc': 'DIN 976 / ASTM A193 B7/B8 全规格，长度可定制 50mm-3000mm',
        'line.custom.name': '非标定制 / Custom Parts',
        'line.custom.desc': '来图来样定制，特殊材质 / 特殊规格 / 特殊表面处理均可定制',
        'line.custom.tag1': 'CAD / STEP',
        'line.custom.tag2': '小批量起订',
        'line.custom.tag3': '15 天交付',
        'line.custom.cta': '立即定制 →',
        'line.view': '查看规格 →',

        // Calculator
        'calc.tag': '在线计算器',
        'calc.title.l1': '输入规格',
        'calc.title.l2': '查询尺寸/体积/重量/强度',
        'calc.desc': '5 个专业计算器：螺栓、螺母、螺杆、垫圈、强度对比。基于 ISO 898-1 / DIN 933 / DIN 934 / DIN 976 真实工程数据。',
        'calc.tab.bolt': '螺栓',
        'calc.tab.nut': '螺母',
        'calc.tab.rod': '螺杆',
        'calc.tab.washer': '垫圈',
        'calc.tab.strength': '强度',
        'calc.field.size': '规格 *',
        'calc.field.length': '长度 L (mm) *',
        'calc.field.material': '材质',
        'calc.field.grade': '强度等级',
        'calc.field.type': '螺纹类型',
        'calc.btn': '🔬 开始计算',
        'calc.note': '💡 所有计算基于 ISO 898-1 / DIN 933 / DIN 934 / DIN 976 等国际标准；用于工程估算，具体设计请参考官方标准。',
        // Specs
        'specs.tag': '规格标准',
        // Catalog Filter
        'filter.cat': '产品分类',
        'filter.std': '标准体系',
        'filter.mat': '材质',
        'filter.toggle': '筛选',
        'filter.reset': '↻ 重置筛选',
        'cat.all': '全部产品',
        'cat.bolts': '螺栓系列',
        'cat.nuts': '螺母系列',
        'cat.rods': '螺杆系列',
        'cat.misc': '紧固件系列',
        'std.all': '全部标准',
        'mat.all': '全部材质',
        // Toolbar
        'toolbar.search': '搜索产品名 / 规格 / 标准...',
        'toolbar.results': '个结果',
        'toolbar.more': '加载更多',
        'toolbar.showing': '显示',
        'toolbar.of': '共',
        // Sort
        'sort.default': '默认排序',
        'sort.id': '按编号',
        'sort.name': '按名称',
        'sort.cat': '按类别',
        // Product Card
        'pc.material': '材质',
        'pc.surface': '表面',
        'pc.spec': '规格',
        'pc.inquire': '询价',
        'pc.detail': '详情',
        'specs.title.l1': '英美标',
        'specs.title.l2': '速查表',
        'specs.desc': '覆盖 BS / ANSI / ASME / ISO / DIN 全系列标准，紧固件规格一站查询。',
        'specs.tab.bs': '英式 BS 系列',
        'specs.tab.unc': '美式 UNC 粗牙',
        'specs.tab.unf': '美式 UNF 细牙',
        'specs.tab.metric': '公制 ISO/DIN',
        'specs.th.size': '规格',
        'specs.th.tpi': '牙数/TPI',
        'specs.th.major': '大径 (mm)',
        'specs.th.pitch': '螺距 (mm)',
        'specs.th.tap': '攻丝 (mm)',
        'specs.th.strength': '推荐强度',
        'specs.note': '🛡️ 所有规格均符合 GB / ISO / BS / ANSI 标准，可提供材质证明 (MTC) 与第三方检测报告',

        // Material
        'mat.tag': '材质与工艺',
        'mat.title.l1': '从原材料到表面处理',
        'mat.title.l2': '全流程自主把控',
        'mat.materials.title': '材质 / Materials',
        'mat.m.1.k': '碳钢',
        'mat.m.1.v': 'C1022 / C1045 / C1018',
        'mat.m.2.k': '合金钢',
        'mat.m.2.v': 'SCM435 / 40Cr / 35CrMo',
        'mat.m.3.k': '不锈钢',
        'mat.m.3.v': '304 (A2) / 316 (A4) / 316L',
        'mat.m.4.k': '高强度钢',
        'mat.m.4.v': '10.9 / 12.9 / ASTM A325 / A490',
        'mat.m.5.k': '有色金属',
        'mat.m.5.v': 'H62 黄铜 / 紫铜 / 铝 6061',
        'mat.surface.title': '表面处理 / Finishes',
        'mat.s.1.k': '镀锌',
        'mat.s.1.v': '蓝白锌 / 彩锌 / 黄锌 / 黑锌',
        'mat.s.2.k': '达克罗',
        'mat.s.2.v': 'Dacromet / Geomet — 盐雾 1000h+',
        'mat.s.3.k': '发黑',
        'mat.s.3.v': 'Black Oxide — 装饰 + 防锈',
        'mat.s.4.k': '磷化',
        'mat.s.4.v': 'Phosphating — 涂装前处理',
        'mat.s.5.k': '热浸镀锌',
        'mat.s.5.v': 'HDG — 户外防腐 50 年+',
        'mat.grade.title': '机械性能等级 / Strength Grades',
        'mat.g.4.t': '普通强度',
        'mat.g.8.t': '高强度',
        'mat.g.10.t': '结构连接',
        'mat.g.12.t': '超高强度',
        'mat.g.a2.t': '不锈钢',
        'mat.g.a4.t': '耐腐蚀',

        // Capacity
        'cap.tag': '生产能力',
        'cap.title.l1': '从一根线材',
        'cap.title.l2': '一颗成品',
        'cap.area.t': '厂房面积',
        'cap.area.d': '自有产权现代化厂房，含冷镦车间、热处理车间、表面处理车间。',
        'cap.machine.t': '生产设备',
        'cap.machine.d': '多工位冷�机、台湾 CNC 数控车床、全自动搓丝机、热处理炉。',
        'cap.output.t': '月产能',
        'cap.output.d': '3 条全自动生产线 + 5 条半自动产线，旺季可弹性扩展 50%。',
        'cap.lead.t': '标准交期',
        'cap.lead.d': '常规订单 7-15 天，定制订单 15-25 天，加急订单最快 5 天。',
        'cap.process.t': '生产流程 / Production Process',
        'cap.p.1': '盘条采购',
        'cap.p.2': '冷镦成型',
        'cap.p.3': '搓丝滚牙',
        'cap.p.4': '热处理',
        'cap.p.5': '表面处理',
        'cap.p.6': '全检包装',

        // Cert
        'cert.tag': '认证资质',
        'cert.title.l1': '权威认证',
        'cert.title.l2': '质量保证',
        'cert.1.d': '质量管理体系认证 — 全流程标准化作业',
        'cert.2.d': '汽车行业质量管理体系 — 主机厂供应商资质',
        'cert.3.d': '环境管理体系 — 绿色生产合规',
        'cert.4.d': '欧盟合规认证 — 出口欧洲市场通行证',
        'cert.5.d': '美标合规 — 北美市场出口资质',
        'cert.6.d': '第三方检测报告 — 每年定期送检',

        // Industry
        'ind.tag': '应用领域',
        'ind.title.l1': '服务全球',
        'ind.title.l2': '8 大行业',
        'ind.1.t': '汽车制造',
        'ind.1.d': '底盘、发动机、变速箱紧固件',
        'ind.2.t': '建筑钢结构',
        'ind.2.d': '高强螺栓、地脚螺栓、锚栓',
        'ind.3.t': '机械装备',
        'ind.3.d': '机床、工程机械、农业机械',
        'ind.4.t': '电力能源',
        'ind.4.d': '风电、光伏、输变电紧固件',
        'ind.5.t': '轨道交通',
        'ind.5.d': '高铁、地铁紧固件，符合 TB/T 标准',
        'ind.6.t': '桥梁工程',
        'ind.6.d': '10.9S / 12.9S 高强螺栓',
        'ind.7.t': '石油化工',
        'ind.7.d': '耐高温、耐腐蚀特殊紧固件',
        'ind.8.t': '家具家电',
        'ind.8.d': '内六角、自攻钉、组合螺丝',

        // About
        'about.tag': '关于我们',
        'about.title.l1': '22 年专注',
        'about.title.l2': '紧固件制造',
        'about.p1': '精工固件成立于 2003 年，位于浙江嘉兴，紧邻上海港 — 全球紧固件制造的核心区域。我们专注于英式、美式、公制全规格紧固件的研发、生产与出口。',
        'about.p2': '从一根盘条到一颗成品，我们拥有完整的冷镦、热处理、表面处理、检测能力，年产能 4 万吨以上。产品远销北美、欧洲、东南亚、中东等 45+ 国家与地区。',
        'about.f.1': '出口国家',
        'about.f.2': '企业客户',
        'about.f.3': '年出口额',
        'about.fc.loc': 'LOCATION',
        'about.fc.loc.v': '浙江 · 嘉兴',
        'about.fc.size': 'FACTORY',
        'about.fc.size.v': '12,000 ㎡',
        'about.fc.staff': 'STAFF',
        'about.fc.staff.v': '220+ 人',
        'about.fc.port': 'PORT',
        'about.fc.port.v': '上海港 90km',

        // RFQ
        'rfq.tag': '立即询价',
        'rfq.title.l1': '获取报价',
        'rfq.title.l2': '24 小时响应',
        'rfq.desc': '无论您是需要标准件现货、小批量试产、还是大批量 OEM — 我们的工程师团队都会在 24 小时内为您提供详细报价与技术支持。',
        'rfq.b.1': '免费样品（标准件）',
        'rfq.b.2': '免费材质证明 (MTC)',
        'rfq.b.3': '第三方检测报告（按需）',
        'rfq.b.4': 'DDP / FOB / CIF 多贸易条款',
        'rfq.b.5': '支持 OEM/ODM 定制包装',
        'rfq.form.t': '提交 RFQ',
        'rfq.f.name': '联系人 *',
        'rfq.f.name.ph': '您的姓名',
        'rfq.f.company': '公司名 *',
        'rfq.f.company.ph': '您的公司',
        'rfq.f.email': '邮箱 *',
        'rfq.f.email.ph': 'business@email.com',
        'rfq.f.phone': '电话 / WhatsApp *',
        'rfq.f.phone.ph': '+86 ...',
        'rfq.f.type': '需求类型',
        'rfq.f.type.std': '标准件现货',
        'rfq.f.type.oem': 'OEM 贴牌',
        'rfq.f.type.odm': 'ODM 定制',
        'rfq.f.type.sample': '样品申请',
        'rfq.f.spec': '规格标准',
        'rfq.f.spec.bsw': 'BSW (英式粗牙)',
        'rfq.f.spec.bsf': 'BSF (英式细牙)',
        'rfq.f.spec.unc': 'UNC (美式粗牙)',
        'rfq.f.spec.unf': 'UNF (美式细牙)',
        'rfq.f.spec.iso': 'ISO / DIN (公制)',
        'rfq.f.spec.other': '其它 / 定制',
        'rfq.f.desc': '需求描述 *',
        'rfq.f.desc.ph': '例如：六角螺栓 M10x40 8.8级 镀锌，每月 50000 件，FOB 上海...',
        'rfq.f.submit': '提交询价 →',
        'rfq.f.tip': '提交后 24 小时内通过邮件 / WhatsApp 与您联系',

        // Footer
        'footer.tagline': '英美标紧固件专业制造商 · 全球出口',
        'footer.col1.t': '产品',
        'footer.col1.l1': '六角螺栓',
        'footer.col1.l2': '六角螺母',
        'footer.col1.l3': '双头螺杆',
        'footer.col1.l4': '非标定制',
        'footer.col2.t': '规格',
        'footer.col2.l1': 'BSW / BSF 英式',
        'footer.col2.l2': 'UNC / UNF 美式',
        'footer.col2.l3': 'ISO / DIN 公制',
        'footer.col2.l4': '材质等级',
        'footer.col3.t': '联系',
        'footer.copyright': '© 2026 精工固件 Jingong Fasteners. All rights reserved. · 浙ICP备XXXXXXXX号',
        'pc.shown': '已显示 {shown} / {total} · {remain} 个待显示',
        'pc.empty': '没有匹配筛选条件的产品',
        'cap.unit': 'T/月',
        'cap.unit.en': 'T/Month',
        'filter.mat.carbon': '碳钢',
        'filter.mat.alloy': '合金钢',
        'filter.mat.ss': '不锈钢',
        'filter.mat.other': '其他',
        'footer.address': '📍 浙江省嘉兴市秀洲区 (待更新)',
        'footer.address.en': '📍 Jiaxing, Zhejiang, China (placeholder)',
        'calc.mat.8.8.steel': '8.8 级 合金钢',
        'calc.mat.10.9.steel': '10.9 级 合金钢',
        'calc.mat.12.9.steel': '12.9 级 合金钢',
        'calc.mat.4.8.steel': '4.8 级 碳钢',
        'calc.mat.b7': 'B7 合金钢',
        'calc.mat.a2-70': 'A2-70 不锈钢',
        'calc.mat.a4-80': 'A4-80 不锈钢',
        'calc.mat.c1022': 'C1022 碳钢',
    },

    en: {
        // Meta
        'page.title': 'Jingong Fasteners - BS/ANSI Hex Bolts, Nuts & Threaded Rods Manufacturer',
        'page.desc': 'Jingong - Professional manufacturer of BSW/BSF/UNC/UNF/UNEF standard fasteners. ISO 9001 & IATF 16949 certified factory. OEM/ODM supported.',

        // Topbar
        'topbar.text': '📦 Factory Direct · OEM/ODM Supported · Global Shipping',
        'topbar.hotline': 'Sales Hotline:',

        // Nav
        'nav.home': 'Home',
        'nav.products': 'Products',
        'nav.specs': 'Specs',
        'nav.material': 'Materials',
        'nav.capacity': 'Capacity',
        'nav.cert': 'Certifications',
        'nav.about': 'About Us',
        'nav.rfq': 'Request Quote',

        // Hero
        'hero.title.l1': 'BS / ANSI Standard',
        'hero.title.l2': 'Fastener Manufacturer',
        'hero.subtitle': 'Complete range of BSW · BSF · UNC · UNF · UNEF threads<br>From M2 to M64, from #0 to 4" — Full Metric & Imperial Threading Solutions',
        'hero.stat.exp': 'Industry Experience',
        'hero.stat.country': 'Export Countries',
        'hero.stat.sku': 'SKUs in Stock',
        'hero.stat.qa': 'Pass Rate',
        'hero.cta.rfq': '📋 Request Quote (RFQ) →',
        'hero.cta.specs': 'View Specifications',

        // Products
        'products.tag': 'PRODUCTS',
        'products.title.l1': 'Product Catalog',
        'products.title.l2': '100 SKUs',
        'products.desc': 'From standard parts to custom specials — full range of bolts, nuts, threaded rods, and fasteners. 4 categories · 8 sub-series · 100 SKUs in stock. Drawings & samples accepted.',
        'line.screws.name': 'Hex Bolts',
        'line.screws.desc': 'DIN 933 / ISO 4017 / UNC / UNF full range, strength grades 4.8 to 12.9',
        'line.nuts.name': 'Hex Nuts',
        'line.nuts.desc': 'DIN 934 / ISO 4032 / Imperial / Metric full range, including nylon lock / flange / cap series',
        'line.studs.name': 'Threaded Rods',
        'line.studs.desc': 'DIN 976 / ASTM A193 B7/B8 full range, custom lengths 50mm to 3000mm',
        'line.custom.name': 'Custom Parts',
        'line.custom.desc': 'Custom per your drawings or samples. Special materials / specs / finishes all available.',
        'line.custom.tag1': 'CAD / STEP',
        'line.custom.tag2': 'Small MOQ',
        'line.custom.tag3': '15-Day Delivery',
        'line.custom.cta': 'Customize Now →',
        'line.view': 'View Specs →',

        // Calculator
        'calc.tag': 'CALCULATORS',
        'calc.title.l1': 'Input Specs',
        'calc.title.l2': 'Query Dimensions / Volume / Weight / Strength',
        'calc.desc': '5 professional calculators: bolt, nut, rod, washer, strength comparison. Based on ISO 898-1 / DIN 933 / DIN 934 / DIN 976 engineering data.',
        'calc.tab.bolt': 'Bolt',
        'calc.tab.nut': 'Nut',
        'calc.tab.rod': 'Rod',
        'calc.tab.washer': 'Washer',
        'calc.tab.strength': 'Strength',
        'calc.field.size': 'Size *',
        'calc.field.length': 'Length L (mm) *',
        'calc.field.material': 'Material',
        'calc.field.grade': 'Strength Grade',
        'calc.field.type': 'Thread Type',
        'calc.btn': '🔬 Calculate',
        'calc.note': '💡 All calculations based on ISO 898-1 / DIN 933 / DIN 934 / DIN 976 standards; for engineering estimation. Refer to official standards for design.',
        // Specs
        'specs.tag': 'SPECIFICATIONS',
        // Catalog Filter
        'filter.cat': 'Categories',
        'filter.std': 'Standards',
        'filter.mat': 'Material',
        'filter.toggle': 'Filters',
        'filter.reset': '↻ Reset Filters',
        'cat.all': 'All Products',
        'cat.bolts': 'Bolts',
        'cat.nuts': 'Nuts',
        'cat.rods': 'Threaded Rods',
        'cat.misc': 'Fasteners',
        'std.all': 'All Standards',
        'mat.all': 'All Materials',
        // Toolbar
        'toolbar.search': 'Search by name / spec / standard...',
        'toolbar.results': ' results',
        'toolbar.more': 'Load More',
        'toolbar.showing': 'Showing',
        'toolbar.of': 'of',
        // Sort
        'sort.default': 'Default',
        'sort.id': 'By SKU',
        'sort.name': 'By Name',
        'sort.cat': 'By Category',
        // Product Card
        'pc.material': 'Material',
        'pc.surface': 'Surface',
        'pc.spec': 'Spec',
        'pc.inquire': 'Inquire',
        'pc.detail': 'Detail',
        'specs.title.l1': 'BS / ANSI',
        'specs.title.l2': 'Quick Reference',
        'specs.desc': 'Complete coverage of BS / ANSI / ASME / ISO / DIN standards — one-stop fastener specification lookup.',
        'specs.tab.bs': 'British BS Series',
        'specs.tab.unc': 'UNC (Coarse)',
        'specs.tab.unf': 'UNF (Fine)',
        'specs.tab.metric': 'Metric ISO/DIN',
        'specs.th.size': 'Size',
        'specs.th.tpi': 'TPI',
        'specs.th.major': 'Major Ø (mm)',
        'specs.th.pitch': 'Pitch (mm)',
        'specs.th.tap': 'Tap Drill (mm)',
        'specs.th.strength': 'Recommended Grade',
        'specs.note': '🛡️ All specifications comply with GB / ISO / BS / ANSI. Mill Test Certificate (MTC) & third-party inspection reports available.',

        // Material
        'mat.tag': 'MATERIAL & FINISH',
        'mat.title.l1': 'From Raw Material',
        'mat.title.l2': 'to Surface Finish',
        'mat.materials.title': 'Materials',
        'mat.m.1.k': 'Carbon Steel',
        'mat.m.1.v': 'C1022 / C1045 / C1018',
        'mat.m.2.k': 'Alloy Steel',
        'mat.m.2.v': 'SCM435 / 40Cr / 35CrMo',
        'mat.m.3.k': 'Stainless Steel',
        'mat.m.3.v': '304 (A2) / 316 (A4) / 316L',
        'mat.m.4.k': 'High-Tensile',
        'mat.m.4.v': '10.9 / 12.9 / ASTM A325 / A490',
        'mat.m.5.k': 'Non-Ferrous',
        'mat.m.5.v': 'H62 Brass / Copper / Aluminum 6061',
        'mat.surface.title': 'Surface Finishes',
        'mat.s.1.k': 'Zinc Plating',
        'mat.s.1.v': 'Clear / Yellow / Black / Color Zinc',
        'mat.s.2.k': 'Dacromet',
        'mat.s.2.v': 'Dacromet / Geomet — 1000h+ salt spray',
        'mat.s.3.k': 'Black Oxide',
        'mat.s.3.v': 'Black Oxide — decorative + anti-rust',
        'mat.s.4.k': 'Phosphating',
        'mat.s.4.v': 'Phosphating — pre-coating treatment',
        'mat.s.5.k': 'HDG',
        'mat.s.5.v': 'Hot-Dip Galvanized — 50+ years outdoor',
        'mat.grade.title': 'Mechanical Strength Grades',
        'mat.g.4.t': 'Standard',
        'mat.g.8.t': 'High-Tensile',
        'mat.g.10.t': 'Structural',
        'mat.g.12.t': 'Ultra High-Strength',
        'mat.g.a2.t': 'Stainless',
        'mat.g.a4.t': 'Corrosion-Resistant',

        // Capacity
        'cap.tag': 'CAPACITY',
        'cap.title.l1': 'From Wire Rod',
        'cap.title.l2': 'to Finished Part',
        'cap.area.t': 'Factory Area',
        'cap.area.d': 'Modern self-owned facility including cold heading, heat treatment, and surface finishing workshops.',
        'cap.machine.t': 'Equipment',
        'cap.machine.d': 'Multi-station cold headers, Taiwan CNC lathes, full-auto thread rollers, heat treatment furnaces.',
        'cap.output.t': 'Monthly Output',
        'cap.output.d': '3 fully-auto + 5 semi-auto production lines. Flexible 50% capacity expansion during peak season.',
        'cap.lead.t': 'Lead Time',
        'cap.lead.d': 'Standard orders 7-15 days, custom 15-25 days, rush orders as fast as 5 days.',
        'cap.process.t': 'Production Process',
        'cap.p.1': 'Wire Rod',
        'cap.p.2': 'Cold Heading',
        'cap.p.3': 'Thread Rolling',
        'cap.p.4': 'Heat Treatment',
        'cap.p.5': 'Surface Finish',
        'cap.p.6': 'QC & Packing',

        // Cert
        'cert.tag': 'CERTIFICATIONS',
        'cert.title.l1': 'Authoritative',
        'cert.title.l2': 'Quality Assurance',
        'cert.1.d': 'Quality Management System — fully standardized operations',
        'cert.2.d': 'Automotive Quality Management — OEM supplier qualification',
        'cert.3.d': 'Environmental Management — green production compliance',
        'cert.4.d': 'EU Compliance — pass to enter European market',
        'cert.5.d': 'US Standard Compliance — North America export qualification',
        'cert.6.d': 'Third-party Test Reports — annual inspection by SGS/BV',

        // Industry
        'ind.tag': 'APPLICATIONS',
        'ind.title.l1': 'Serving Global',
        'ind.title.l2': '8 Industries',
        'ind.1.t': 'Automotive',
        'ind.1.d': 'Chassis, engine, transmission fasteners',
        'ind.2.t': 'Steel Structures',
        'ind.2.d': 'High-strength bolts, anchor bolts',
        'ind.3.t': 'Machinery',
        'ind.3.d': 'Machine tools, construction & agricultural equipment',
        'ind.4.t': 'Power & Energy',
        'ind.4.d': 'Wind, solar, transmission fasteners',
        'ind.5.t': 'Rail Transit',
        'ind.5.d': 'High-speed rail, subway per TB/T standard',
        'ind.6.t': 'Bridge Engineering',
        'ind.6.d': '10.9S / 12.9S high-strength bolts',
        'ind.7.t': 'Oil & Chemical',
        'ind.7.d': 'High-temp & corrosion-resistant specialty fasteners',
        'ind.8.t': 'Furniture & Appliance',
        'ind.8.d': 'Socket cap, self-tapping, combination screws',

        // About
        'about.tag': 'ABOUT US',
        'about.title.l1': '22 Years Dedicated',
        'about.title.l2': 'to Fastener Manufacturing',
        'about.p1': 'Founded in 2003 in Jiaxing, Zhejiang — adjacent to Shanghai Port, the global hub of fastener manufacturing. We specialize in the R&D, production, and export of British, American, and metric standard fasteners.',
        'about.p2': 'From wire rod to finished part, we have complete cold heading, heat treatment, surface finishing, and inspection capabilities, with annual capacity over 40,000 tons. Products exported to 45+ countries across North America, Europe, Southeast Asia, and the Middle East.',
        'about.f.1': 'Export Countries',
        'about.f.2': 'Enterprise Clients',
        'about.f.3': 'Annual Export',
        'about.fc.loc': 'LOCATION',
        'about.fc.loc.v': 'Jiaxing, Zhejiang',
        'about.fc.size': 'FACTORY',
        'about.fc.size.v': '12,000 ㎡',
        'about.fc.staff': 'STAFF',
        'about.fc.staff.v': '220+ People',
        'about.fc.port': 'PORT',
        'about.fc.port.v': 'Shanghai 90km',

        // RFQ
        'rfq.tag': 'REQUEST QUOTE',
        'rfq.title.l1': 'Get Your Quote',
        'rfq.title.l2': 'within 24 Hours',
        'rfq.desc': 'Whether you need standard parts in stock, small-batch trial production, or large-volume OEM — our engineering team will provide detailed quotations and technical support within 24 hours.',
        'rfq.b.1': 'Free samples (standard parts)',
        'rfq.b.2': 'Free Mill Test Certificate (MTC)',
        'rfq.b.3': 'Third-party test reports (on demand)',
        'rfq.b.4': 'DDP / FOB / CIF trade terms',
        'rfq.b.5': 'OEM/ODM custom packaging supported',
        'rfq.form.t': 'Submit RFQ',
        'rfq.f.name': 'Contact Name *',
        'rfq.f.name.ph': 'Your name',
        'rfq.f.company': 'Company *',
        'rfq.f.company.ph': 'Your company',
        'rfq.f.email': 'Email *',
        'rfq.f.email.ph': 'business@email.com',
        'rfq.f.phone': 'Phone / WhatsApp *',
        'rfq.f.phone.ph': '+86 ...',
        'rfq.f.type': 'Inquiry Type',
        'rfq.f.type.std': 'Standard parts in stock',
        'rfq.f.type.oem': 'OEM branding',
        'rfq.f.type.odm': 'ODM custom',
        'rfq.f.type.sample': 'Sample request',
        'rfq.f.spec': 'Specification Standard',
        'rfq.f.spec.bsw': 'BSW (British Coarse)',
        'rfq.f.spec.bsf': 'BSF (British Fine)',
        'rfq.f.spec.unc': 'UNC (US Coarse)',
        'rfq.f.spec.unf': 'UNF (US Fine)',
        'rfq.f.spec.iso': 'ISO / DIN (Metric)',
        'rfq.f.spec.other': 'Other / Custom',
        'rfq.f.desc': 'Requirement Description *',
        'rfq.f.desc.ph': 'e.g., Hex bolt M10x40 grade 8.8 zinc plated, 50,000 pcs/month, FOB Shanghai...',
        'rfq.f.submit': 'Submit Quote Request →',
        'rfq.f.tip': 'We will respond within 24 hours via email / WhatsApp',

        // Footer
        'footer.tagline': 'BS / ANSI Standard Fasteners Manufacturer · Global Export',
        'footer.col1.t': 'Products',
        'footer.col1.l1': 'Hex Bolts',
        'footer.col1.l2': 'Hex Nuts',
        'footer.col1.l3': 'Threaded Rods',
        'footer.col1.l4': 'Custom Parts',
        'footer.col2.t': 'Standards',
        'footer.col2.l1': 'BSW / BSF (British)',
        'footer.col2.l2': 'UNC / UNF (American)',
        'footer.col2.l3': 'ISO / DIN (Metric)',
        'footer.col2.l4': 'Strength Grades',
        'footer.col3.t': 'Contact',
        'footer.copyright': '© 2026 Jingong Fasteners. All rights reserved.',
        'pc.shown': 'Showing {shown} / {total} · {remain} more available',
        'pc.empty': 'No products match your filters.',
        'cap.unit': 'T/Month',
        'cap.unit.en': 'T/Month',
        'filter.mat.carbon': 'Carbon Steel',
        'filter.mat.alloy': 'Alloy Steel',
        'filter.mat.ss': 'Stainless Steel',
        'filter.mat.other': 'Other',
        'footer.address': '📍 Jiaxing, Zhejiang, China (placeholder)',
        'footer.address.en': '📍 Jiaxing, Zhejiang, China (placeholder)',
        'calc.mat.8.8.steel': '8.8 Grade Alloy Steel',
        'calc.mat.10.9.steel': '10.9 Grade Alloy Steel',
        'calc.mat.12.9.steel': '12.9 Grade Alloy Steel',
        'calc.mat.4.8.steel': '4.8 Grade Carbon Steel',
        'calc.mat.b7': 'B7 Alloy Steel',
        'calc.mat.a2-70': 'A2-70 Stainless Steel',
        'calc.mat.a4-80': 'A4-80 Stainless Steel',
        'calc.mat.c1022': 'C1022 Carbon Steel',
    }
        'brand.cn': '精工固件',
        'brand.en': 'Jingong Fasteners',
};

let currentLang = localStorage.getItem('jingong-lang') || 'zh';


/* ===== 材质/表面翻译映射 ===== */
const matEnMap = {
    '10.9级 合金钢': '10.9 Grade Alloy Steel',
    '10级 合金钢': '10 Grade Alloy Steel',
    '12.9级 合金钢': '12.9 Grade Alloy Steel',
    '140HV 碳钢': '140HV Carbon Steel',
    '4.8级 碳钢': '4.8 Grade Carbon Steel',
    '4级 碳钢': '4 Grade Carbon Steel',
    '8.8级 合金钢': '8.8 Grade Alloy Steel',
    '8.8级 碳钢': '8.8 Grade Carbon Steel',
    '8级 碳钢': '8 Grade Carbon Steel',
    'A2 不锈钢': 'A2 Stainless Steel',
    'A4 不锈钢': 'A4 Stainless Steel',
    'B7 合金钢': 'B7 Alloy Steel',
    'C1022 碳钢': 'C1022 Carbon Steel',
    'Grade 2 碳钢': 'Grade 2 Carbon Steel',
    'Grade 5 碳钢': 'Grade 5 Carbon Steel',
    'Grade 8 合金钢': 'Grade 8 Alloy Steel',
    'Grade B7 合金钢': 'Grade B7 Alloy Steel',
    '不锈钢 + 镀锌': 'Stainless + Zinc Plated',
    '不锈钢 304': '304 Stainless Steel',
    '低碳钢': 'Low Carbon Steel',
    '工具钢': 'Tool Steel',
    '弹簧钢': 'Spring Steel',
    '碳钢': 'Carbon Steel',
    '铝 + 钢钉': 'Aluminum + Steel Mandrel',
    '铝合金': 'Aluminum Alloy'
};
const surfaceEnMap = {
    '发黑': 'Black Oxide',
    '本色': 'Plain (Mill Finish)',
    '热浸镀锌': 'Hot-Dip Galvanized',
    '磷化 + 涂油': 'Phosphated + Oiled',
    '达克罗': 'Dacromet',
    '镀锌': 'Zinc Plated'
};
const matFilterEnMap = {
    '碳钢': 'Carbon Steel',
    '合金钢': 'Alloy Steel',
    '不锈钢': 'Stainless Steel',
    '其他': 'Other'
};

function t(key, params) {
    let v = (translations[currentLang] || {})[key] || key;
    if (params && typeof v === 'string') {
        for (const k in params) {
            v = v.split('{' + k + '}').join(params[k]);
        }
    }
    return v;
}


/* ===== Select 选项翻译映射 ===== */
const i18nOptionMap = {
    'calc.materials': {
        '8.8': { zh: '8.8 级 合金钢', en: '8.8 Grade Alloy Steel' },
        '10.9': { zh: '10.9 级 合金钢', en: '10.9 Grade Alloy Steel' },
        '12.9': { zh: '12.9 级 合金钢', en: '12.9 Grade Alloy Steel' },
        '4.8': { zh: '4.8 级 碳钢', en: '4.8 Grade Carbon Steel' },
        'b7': { zh: 'B7 合金钢', en: 'B7 Alloy Steel' },
        'a2-70': { zh: 'A2-70 不锈钢', en: 'A2-70 Stainless Steel' },
        'a4-80': { zh: 'A4-80 不锈钢', en: 'A4-80 Stainless Steel' },
        'c1022': { zh: 'C1022 碳钢', en: 'C1022 Carbon Steel' },
        '8': { zh: '8 级 碳钢', en: '8 Grade Carbon Steel' },
        '10': { zh: '10 级 合金钢', en: '10 Grade Alloy Steel' },
        'a2': { zh: 'A2 不锈钢', en: 'A2 Stainless Steel' },
        '140hv': { zh: '140HV 碳钢', en: '140HV Carbon Steel' }
    },
    'filter.materials': {
        'carbon': { zh: '碳钢', en: 'Carbon Steel' },
        'alloy': { zh: '合金钢', en: 'Alloy Steel' },
        'ss': { zh: '不锈钢', en: 'Stainless Steel' },
        'other': { zh: '其他', en: 'Other' }
    }
};
function tMat(zh) { return (currentLang === 'en' && matEnMap[zh]) || zh; }
function tSurface(zh) { return (currentLang === 'en' && surfaceEnMap[zh]) || zh; }
function tMatFilter(zh) { return (currentLang === 'en' && matFilterEnMap[zh]) || zh; }


function setLanguage(lang) {
    if (!translations[lang]) return;
    currentLang = lang;
    localStorage.setItem('jingong-lang', lang);

    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.dataset.i18n;
        if (translations[lang][key]) {
            el.textContent = translations[lang][key];
        }
    });

    document.querySelectorAll('[data-i18n-html]').forEach(el => {
        const key = el.dataset.i18nHtml;
        if (translations[lang][key]) {
            el.innerHTML = translations[lang][key];
        }
    });

    // 翻译 select option 文本
    document.querySelectorAll('select[data-i18n-options]').forEach(sel => {
        const key = sel.dataset.i18nOptions;
        const map = i18nOptionMap[key] || {};
        Array.from(sel.options).forEach(opt => {
            const lookup = opt.getAttribute('data-i18n-opt') || opt.value;
            if (map[lookup]) {
                const v = map[lookup][lang] || map[lookup].zh;
                opt.textContent = v;
            }
        });
    });

    // 触发产品卡重渲染（mat/surface 等动态字段）
    if (typeof renderProducts === 'function') {
        renderProducts(true);
    }

    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.dataset.i18nPlaceholder;
        if (translations[lang][key]) {
            el.placeholder = translations[lang][key];
        }
    });

    document.querySelectorAll('[data-i18n-option]').forEach(el => {
        const key = el.dataset.i18nOption;
        if (translations[lang][key]) {
            el.textContent = translations[lang][key];
        }
    });

    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';

    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === lang);
    });

    // 重新渲染规格表（含多语言表头）
    if (typeof renderSpecTable === 'function') {
        renderSpecTable(currentSpecTab);
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => setLanguage(currentLang));
} else {
    setLanguage(currentLang);
}
