// JanDawa Bilingual (Hindi / English) Internationalization (i18n) Engine
(function() {
  const I18N = {
    hi: {
      // Header & Navigation
      nav_brand_sub: "जन औषधि",
      nav_medicines: "दवा खोजक",
      nav_skincare: "स्किनकेयर व ब्यूटी (25 उत्पाद)",
      nav_kendras: "केंद्र डायरेक्टरी (777 ज़िले)",
      nav_savings: "बचत कैलकुलेटर",
      nav_kendra_btn: "21,745 केंद्र खोजें",
      nav_med_btn: "2,513 दवाएं खोजें",

      // Mobile Bottom App Bar
      bar_medicines: "दवाएं",
      bar_skincare: "स्किनकेयर",
      bar_kendras: "777 ज़िले",
      bar_savings: "बचत",

      // Home Hero Section
      hero_badge: "प्रधानमंत्री भारतीय जन औषधि परियोजना (PMBJP) डेटाबेस",
      hero_title: 'ब्रांडेड दवाओं का <span class="text-brand-700">सटीक सरकारी विकल्प</span> खोजें',
      hero_sub: "वही सक्रिय रासायनिक साल्ट (Active Formulation), NABL लैब प्रमाणित गुणवत्ता और 80% तक की सीधी बचत। बस अपनी दवा का नाम टाइप करें:",
      search_placeholder: "ब्रांडेड दवा या साल्ट लिखें (उदा: Telma 40, Pan-D, Dolo 650, Augmentin)...",
      btn_scan_rx: "पर्चा स्कैन करें",
      trending_label: "अक्सर खोजी गई:",
      verified_badge: "100% प्रामाणिक PMBJP सरकारी दर",

      // Stats
      stat_kendras_num: "21,745+",
      stat_kendras_label: "सक्रिय जन औषधि केंद्र",
      stat_meds_num: "2,513+",
      stat_meds_label: "सस्ती जेनेरिक दवाएं",
      stat_districts_num: "777",
      stat_districts_label: "ज़िलों में देशव्यापी नेटवर्क",
      stat_savings_num: "50-90%",
      stat_savings_label: "अधिकतम सीधी बचत",

      // Medicine Filter Categories
      cat_all: "सभी दवाएं (2,513)",
      cat_cardio: "बीपी व दिल (Cardio)",
      cat_diabetes: "मधुमेह (Diabetes)",
      cat_gastro: "गैस व एसिडिटी (Gastro)",
      cat_antibiotic: "एंटीबायोटिक (Antibiotic)",
      cat_pain: "दर्द व बुखार (Pain Relief)",
      cat_respiratory: "सांस व दमा (Asthma)",
      cat_vitamins: "विटामिन्स (Vitamins)",

      // Medicine Card Strings
      card_saving_tag: "बचत",
      card_equiv_brand: "समान ब्रांड:",
      card_active_salt: "सक्रिय फॉर्मूलेशन (Active Salt):",
      card_drug_code: "ड्रग कोड:",
      card_unit: "यूनिट:",
      card_market_mrp: "ब्रांडेड MRP",
      card_jan_price: "जन औषधि दर",
      card_direct_saving: "सीधी बचत:",
      card_per_pack: "प्रति पैक",
      card_rx_slip: "डिजिटल पर्चा",
      card_find_kendra: "नजदीकी केंद्र",
      card_details_btn: "विस्तार ➔",
      card_share: "शेयर करें",
      showing_label: "कुल 2,513 में से दवाएं दिख रही हैं:",
      load_more: "और दवाएं देखें (Load More)",
      no_results_title: "कोई दवा नहीं मिली",
      no_results_sub: "कृपया स्पेलिंग जांचें या केवल जेनेरिक साल्ट का नाम लिखकर खोजें।",
      no_results_btn: "सभी दवाएं देखें",

      // Savings Calculator
      calc_badge: "बचत कैलकुलेटर",
      calc_title: "जन औषधि से आप हर साल कितना बचा सकते हैं?",
      calc_sub: "अपने परिवार का मासिक दवा खर्च दर्ज करें और देखें कि जन औषधि पर आप कितनी बचत कर सकते हैं।",
      calc_input_label: "आपका मासिक दवा खर्च (रुपये में):",
      calc_monthly_savings: "मासिक बचत",
      calc_yearly_savings: "वार्षिक बचत (12 महीने)",
      calc_note: "*औसत 70% बचत दर के आधार पर अनुमानित। विभिन्न दवाओं में बचत 50% से 90% तक होती है।",

      // Trust Badges
      trust_badge: "गुणवत्ता व प्रामाणिकता",
      trust_title: "सरकारी मानकों पर 100% खरी दवाएं",
      trust_sub: "जन औषधि की सभी दवाएं उच्चतम अंतरराष्ट्रीय और राष्ट्रीय स्वास्थ्य मानकों पर परखी जाती हैं।",
      trust_nabl_title: "सरकारी NABL लैब्स में परीक्षण",
      trust_nabl_sub: "हर बैच की गुणवत्ता और शुद्धता NABL से मान्यता प्राप्त लैब्स द्वारा प्रमाणित की जाती है।",
      trust_gmp_title: "WHO-GMP प्रमाणित विनिर्माण",
      trust_gmp_sub: "दवाओं का निर्माण विश्व स्वास्थ्य संगठन (WHO) के गुड मैन्युफैक्चरिंग प्रैक्टिसेज मानकों के तहत होता है।",
      trust_inn_title: "वही सक्रिय रासायनिक तत्व (INN)",
      trust_inn_sub: "ब्रांडेड दवाओं जैसा ही रासायनिक फॉर्मूला (Salt & Strength), जिससे असर में कोई अंतर नहीं होता।",

      // FAQs
      faq_badge: "सामान्य प्रश्न",
      faq_title: "अक्सर पूछे जाने वाले सवाल",

      // Skincare Specific
      skin_avail_badge: "Available at Nearest Kendra",
      skin_title: 'Affordable Govt Alternatives to <span class="text-rose-600">Expensive Skincare Brands</span>',
      skin_sub: "Identical active dermatological ingredients (Salicylic, Glycolic, Ketoconazole, Adapalene) used in ₹400-₹800 premium cosmetics — available at Jan Aushadhi Kendras for just <strong>₹25 to ₹85</strong>.",
      skin_search_placeholder: "Search products (e.g. Face Wash, Minoxidil, Suvidha)...",
      skin_search_btn: "Search",
      skin_cat_all: "All Products (25)",
      skin_cat_face: "Face Wash & Acne (6)",
      skin_cat_hair: "Hair & Anti-Dandruff (4)",
      skin_cat_moisturizer: "Moisturizer & Body (4)",
      skin_cat_hygiene: "Suvidha Sanitary Pads (3)",
      skin_cat_baby: "Baby Care (3)",
      skin_cat_oral: "Dental & Oral Care (3)",
      skin_avg_saving: "Average 80% Savings",
      skin_avail_badge: "नजदीकी केंद्र पर उपलब्ध",
      skin_title: 'महंगे स्किनकेयर ब्रांड्स का <span class="text-rose-600">किफायती सरकारी विकल्प</span>',
      skin_sub: "वही रासायनिक साल्ट (सैलिसिलिक, ग्लाइकोलिक, कीटोकोनाज़ोल, अडैपलीन) जो ₹400-₹800 के कॉस्मेटिक ब्रांड्स में होते हैं — जन औषधि केंद्र पर मात्र <strong>₹25 से ₹85</strong> में उपलब्ध।",
      skin_search_placeholder: "प्रोडक्ट खोजें (उदा: फेस वॉश, मिनोक्सिडिल, सुविधा)...",
      skin_search_btn: "खोजें",
      skin_cat_all: "सभी उत्पाद (25)",
      skin_cat_face: "फेस वॉश व मुहांसे (6)",
      skin_cat_hair: "बाल व डैंड्रफ (4)",
      skin_cat_moisturizer: "मॉइस्चराइज़र व लोशन (4)",
      skin_cat_hygiene: "सुविधा सैनिटरी पैड्स (3)",
      skin_cat_baby: "शिशु देखभाल (3)",
      skin_cat_oral: "दांत व ओरल केयर (3)",
      skin_avg_saving: "औसत 80% बचत",
      skin_badge: "जन औषधि ब्यूटी, डर्मा व पर्सनल केयर",
      skin_title_1: "महंगे स्किनकेयर ब्रांड्स का",
      skin_title_accent: "किफायती सरकारी विकल्प",
      skin_sub: "वही रासायनिक साल्ट (सैलिसिलिक, ग्लाइकोलिक, कीटोकोनाज़ोल, अडैपलीन) जो ₹400-₹800 के कॉस्मेटिक ब्रांड्स में होते हैं — जन औषधि केंद्र पर मात्र ₹25 से ₹85 में उपलब्ध।",
      skin_search_placeholder: "प्रोडक्ट खोजें (उदा: फेस वॉश, मिनोक्सिडिल, कीटोकोनाज़ोल, सुविधा)...",
      skin_cat_all: "सभी उत्पाद (25)",
      skin_cat_face: "फेस वॉश व मुहांसे",
      skin_cat_hair: "बाल व डैंड्रफ",
      skin_cat_body: "त्वचा व एंटी-फंगल",
      skin_cat_hygiene: "सुविधा सैनिटरी पैड्स",
      skin_cat_baby: "शिशु देखभाल (Baby)",
      skin_cat_oral: "ओरल व डेंटल केयर",
      skin_count_prefix: "कुल",
      skin_count_suffix: "उत्पाद उपलब्ध",
      skin_card_benefit: "मुख्य लाभ:",
      skin_card_usage: "उपयोग:",
      skin_card_market: "बाजार ब्रांड",
      skin_card_jan: "जन औषधि दर",

      // Kendra Specific
      kendra_badge: "पूरे भारत में 21,745+ केंद्र",
      kendra_hero_title: "अपने ज़िले में नजदीकी जन औषधि केंद्र खोजें",
      kendra_hero_sub: "देश के सभी 36 राज्यों और 777 ज़िलों में फैले आधिकारिक जन औषधि केंद्रों की पूरी सूची व पता।",
      kendra_search_placeholder: "अपने राज्य या ज़िले का नाम लिखें (उदा. Jaipur, Patna, Lucknow)...",
      kendra_states_heading: "भारत के सभी 36 राज्य एवं केंद्र शासित प्रदेश",
      kendra_state_count_suffix: "ज़िले",
      kendra_view_districts: "ज़िले देखें",

      // Footer
      footer_disclaimer: "जन दवा (JanDawa) एक स्वतंत्र जन-जागरूकता पहल है। यह भारत सरकार के PMBJP पोर्टल से सार्वजनिक रूप से उपलब्ध आधिकारिक डेटा पर आधारित है। दवा लेने से पहले डॉक्टर की सलाह अवश्य लें।",
      footer_about: "हमारे बारे में",
      footer_disclaimer_link: "डिस्क्लेमर",
      footer_privacy: "प्राइवेसी पॉलिसी",
      footer_copyright: "जन दवा — सभी भारतीयों के लिए सस्ती व सुलभ स्वास्थ्य सेवा।"
    },

    en: {
      // Header & Navigation
      nav_brand_sub: "Jan Aushadhi",
      nav_medicines: "Medicine Finder",
      nav_skincare: "Skincare & Beauty (25 Items)",
      nav_kendras: "Kendra Directory (777 Districts)",
      nav_savings: "Savings Calculator",
      nav_kendra_btn: "Find 21,745 Kendras",
      nav_med_btn: "Search 2,513 Medicines",

      // Mobile Bottom App Bar
      bar_medicines: "Medicines",
      bar_skincare: "Skincare",
      bar_kendras: "777 Districts",
      bar_savings: "Savings",

      // Home Hero Section
      hero_badge: "Official PMBJP Database & 2,513+ Generic Medicines",
      hero_title: 'Find Affordable <span class="text-brand-700">Govt Generic Alternatives</span> to Branded Medicines',
      hero_sub: "Identical active chemical formulation, certified NABL lab quality, and up to 80% direct savings. Simply type your medicine name:",
      search_placeholder: "Type branded medicine or salt (e.g. Telma 40, Pan-D, Dolo 650, Augmentin)...",
      btn_scan_rx: "Scan Rx Slip",
      trending_label: "Trending Searches:",
      verified_badge: "100% Authentic PMBJP Govt Rates",

      // Stats
      stat_kendras_num: "21,745+",
      stat_kendras_label: "Active Jan Aushadhi Kendras",
      stat_meds_num: "2,513+",
      stat_meds_label: "Affordable Generic Medicines",
      stat_districts_num: "777",
      stat_districts_label: "Districts Covered Nationwide",
      stat_savings_num: "50-90%",
      stat_savings_label: "Direct Patient Savings",

      // Medicine Filter Categories
      cat_all: "All Medicines (2,513)",
      cat_cardio: "BP & Heart (Cardio)",
      cat_diabetes: "Diabetes & Sugar",
      cat_gastro: "Acidity & Gas (Gastro)",
      cat_antibiotic: "Antibiotics",
      cat_pain: "Pain & Fever Relief",
      cat_respiratory: "Asthma & Respiratory",
      cat_vitamins: "Vitamins & Supplements",

      // Medicine Card Strings
      card_saving_tag: "Savings",
      card_equiv_brand: "Equivalent Brand:",
      card_active_salt: "Active Formulation (Salt):",
      card_drug_code: "Drug Code:",
      card_unit: "Unit:",
      card_market_mrp: "Branded MRP",
      card_jan_price: "Jan Aushadhi Price",
      card_direct_saving: "Direct Savings:",
      card_per_pack: "per pack",
      card_rx_slip: "Digital Rx Slip",
      card_find_kendra: "Nearest Kendra",
      card_details_btn: "Details ➔",
      card_share: "Share",
      showing_label: "Showing medicines out of 2,513:",
      load_more: "Load More Medicines",
      no_results_title: "No Medicines Found",
      no_results_sub: "Please verify spelling or search directly by generic salt formulation.",
      no_results_btn: "View All Medicines",

      // Savings Calculator
      calc_badge: "Savings Calculator",
      calc_title: "How Much Can You Save Every Year with Jan Aushadhi?",
      calc_sub: "Enter your family's monthly medicine expense to see your direct annual savings.",
      calc_input_label: "Your Monthly Medicine Expense (in ₹):",
      calc_monthly_savings: "Monthly Savings",
      calc_yearly_savings: "Annual Savings (12 Months)",
      calc_note: "*Estimated based on an average 70% savings rate. Savings vary from 50% to 90% across different formulations.",

      // Trust Badges
      trust_badge: "Quality & Authenticity",
      trust_title: "100% Certified to Government Standards",
      trust_sub: "All Jan Aushadhi medicines are tested and certified against rigorous national and WHO healthcare quality benchmarks.",
      trust_nabl_title: "Tested in Govt NABL Labs",
      trust_nabl_sub: "Every single production batch is verified for purity and safety by NABL-accredited analytical laboratories.",
      trust_gmp_title: "WHO-GMP Certified Facilities",
      trust_gmp_sub: "Manufactured strictly following World Health Organization Good Manufacturing Practices (WHO-GMP).",
      trust_inn_title: "Identical Active Ingredients (INN)",
      trust_inn_sub: "Exact chemical equivalence (Salt & Strength) matching premium commercial pharmaceutical brands.",

      // FAQs
      faq_badge: "Frequently Asked Questions",
      faq_title: "Frequently Asked Questions",

      // Skincare Specific
      skin_avail_badge: "Available at Nearest Kendra",
      skin_title: 'Affordable Govt Alternatives to <span class="text-rose-600">Expensive Skincare Brands</span>',
      skin_sub: "Identical active dermatological ingredients (Salicylic, Glycolic, Ketoconazole, Adapalene) used in ₹400-₹800 premium cosmetics — available at Jan Aushadhi Kendras for just <strong>₹25 to ₹85</strong>.",
      skin_search_placeholder: "Search products (e.g. Face Wash, Minoxidil, Suvidha)...",
      skin_search_btn: "Search",
      skin_cat_all: "All Products (25)",
      skin_cat_face: "Face Wash & Acne (6)",
      skin_cat_hair: "Hair & Anti-Dandruff (4)",
      skin_cat_moisturizer: "Moisturizer & Body (4)",
      skin_cat_hygiene: "Suvidha Sanitary Pads (3)",
      skin_cat_baby: "Baby Care (3)",
      skin_cat_oral: "Dental & Oral Care (3)",
      skin_avg_saving: "Average 80% Savings",
      skin_badge: "Jan Aushadhi Beauty, Derma & Personal Care",
      skin_title_1: "Affordable Government Alternatives to",
      skin_title_accent: "Expensive Skincare Brands",
      skin_sub: "The exact active chemical salts (Salicylic Acid, Glycolic Acid, Ketoconazole, Adapalene) found in ₹400-₹800 premium cosmetics — available at Jan Aushadhi Kendras for just ₹25 to ₹85.",
      skin_search_placeholder: "Search products (e.g. Face Wash, Minoxidil, Ketoconazole, Suvidha)...",
      skin_cat_all: "All Products (25)",
      skin_cat_face: "Face Wash & Acne",
      skin_cat_hair: "Hair & Anti-Dandruff",
      skin_cat_body: "Skin & Anti-Fungal",
      skin_cat_hygiene: "Suvidha Sanitary Pads",
      skin_cat_baby: "Baby Care",
      skin_cat_oral: "Oral & Dental Care",
      skin_count_prefix: "Total",
      skin_count_suffix: "Products Available",
      skin_card_benefit: "Key Benefits:",
      skin_card_usage: "Usage:",
      skin_card_market: "Market Brand",
      skin_card_jan: "Jan Aushadhi Price",

      // Kendra Specific
      kendra_badge: "21,745+ Kendras Across India",
      kendra_hero_title: "Find Nearest Jan Aushadhi Kendra in Your District",
      kendra_hero_sub: "Comprehensive directory with verified addresses and contacts across all 36 States and 777 Districts in India.",
      kendra_search_placeholder: "Type State or District name (e.g. Jaipur, Patna, Lucknow, Mumbai)...",
      kendra_states_heading: "All 36 States & Union Territories of India",
      kendra_state_count_suffix: "Districts",
      kendra_view_districts: "View Districts",

      // Footer
      footer_disclaimer: "JanDawa is an independent public awareness healthcare platform based on official publicly available data from the PMBJP portal. Please consult a qualified doctor before taking any medicine.",
      footer_about: "About Us",
      footer_disclaimer_link: "Disclaimer",
      footer_privacy: "Privacy Policy",
      footer_copyright: "JanDawa — Affordable, accessible, certified healthcare for all citizens."
    }
  };

  // Get current language from localStorage or default to 'hi'
  let currentLang = localStorage.getItem('jandawa_lang') || 'hi';

  function t(key, fallback = '') {
    const dict = I18N[currentLang] || I18N['hi'];
    return dict[key] !== undefined ? dict[key] : (I18N['hi'][key] || fallback || key);
  }

  function setLanguage(lang) {
    if (lang !== 'hi' && lang !== 'en') lang = 'hi';
    currentLang = lang;
    localStorage.setItem('jandawa_lang', lang);
    document.documentElement.lang = lang;

    // Apply translations to all DOM elements with data-i18n
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      const val = t(key);
      if (val) {
        el.innerHTML = val;
      }
    });

    // Apply placeholders
    document.querySelectorAll('[data-i18n-ph]').forEach(el => {
      const key = el.getAttribute('data-i18n-ph');
      const val = t(key);
      if (val) {
        el.setAttribute('placeholder', val);
      }
    });

    // Update Language Toggle Buttons in UI
    updateLanguageButtons();

    // Trigger page-specific re-renders
    if (typeof window.renderMedicines === 'function') {
      window.renderMedicines();
    }
    if (typeof window.renderSkincare === 'function') {
      window.renderSkincare();
    }
    if (typeof window.updateSavingsCalc === 'function') {
      window.updateSavingsCalc();
    }
    if (typeof window.renderKendraDirectory === 'function') {
      window.renderKendraDirectory();
    }

    // Dispatch event so any other components can listen
    window.dispatchEvent(new CustomEvent('jandawa_language_changed', { detail: { lang: currentLang } }));
  }

  function updateLanguageButtons() {
    document.querySelectorAll('.lang-btn-hi').forEach(btn => {
      if (currentLang === 'hi') {
        btn.className = 'lang-btn-hi px-2.5 py-1 rounded-full font-bold text-xs bg-white text-slate-900 shadow-xs transition-all';
      } else {
        btn.className = 'lang-btn-hi px-2.5 py-1 rounded-full font-medium text-xs text-slate-500 hover:text-slate-900 transition-all';
      }
    });

    document.querySelectorAll('.lang-btn-en').forEach(btn => {
      if (currentLang === 'en') {
        btn.className = 'lang-btn-en px-2.5 py-1 rounded-full font-bold text-xs bg-white text-slate-900 shadow-xs transition-all';
      } else {
        btn.className = 'lang-btn-en px-2.5 py-1 rounded-full font-medium text-xs text-slate-500 hover:text-slate-900 transition-all';
      }
    });
  }

  // Initialize on load
  document.addEventListener('DOMContentLoaded', () => {
    setLanguage(currentLang);
  });

  // Export to window
  window.I18N = I18N;
  window.t = t;
  window.setLanguage = setLanguage;
  window.getLanguage = () => currentLang;
})();
