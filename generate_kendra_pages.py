"""
JanDawa Programmatic Local SEO Generator for 777 Districts
Generates dedicated, high-ranking Kendra directory pages for every district in India,
with LocalBusiness / Pharmacy Schema.org JSON-LD, Google Maps links, search filter,
an interactive Master Directory with instant District/Pincode search, and updates sitemap.xml!
"""

import json
import os
import re
import urllib.parse
from collections import defaultdict

SCRATCH_DIR = os.path.dirname(__file__)
KENDRA_JSON_PATH = os.path.join(os.path.dirname(SCRATCH_DIR), "all_kendras.json")
OUTPUT_DIR = os.path.join(SCRATCH_DIR, "kendra")
SITEMAP_PATH = os.path.join(SCRATCH_DIR, "sitemap.xml")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

def main():
    if not os.path.exists(KENDRA_JSON_PATH):
        print(f"Kendra JSON not found at: {KENDRA_JSON_PATH}")
        return

    with open(KENDRA_JSON_PATH, "r", encoding="utf-8") as f:
        kendras = json.load(f)

    # Normalize state & district
    pin_map = {}
    for k in kendras:
        st = k['state'].strip()
        if 'Jammu' in st:
            st = 'Jammu And Kashmir'
        elif 'Dadra' in st:
            st = 'Dadra and Nagar Haveli and Daman and Diu'
        elif 'Andaman' in st:
            st = 'Andaman and Nicobar Islands'
        else:
            st = st.title()
        k['state'] = st
        dist = k['district'].strip().title()
        k['district'] = dist

        pin = k.get('pincode', '').strip()
        if re.match(r'^\d{6}$', pin):
            slug = f"{slugify(st)}-{slugify(dist)}"
            pin_map[pin] = {'d': dist, 's': st, 'u': f"/kendra/{slug}"}

    by_state_dist = defaultdict(lambda: defaultdict(list))
    for k in kendras:
        by_state_dist[k['state']][k['district']].append(k)

    print(f"Total States: {len(by_state_dist)}")
    total_districts = sum(len(d) for d in by_state_dist.values())
    print(f"Total Districts: {total_districts}")
    print(f"Total Mapped Pincodes: {len(pin_map)}")

    generated_slugs = []

    # 1. Generate individual District Pages
    for state_name, districts in sorted(by_state_dist.items()):
        state_slug = slugify(state_name)
        other_districts = sorted(districts.keys())

        for dist_name, store_list in districts.items():
            dist_slug = slugify(dist_name)
            page_slug = f"{state_slug}-{dist_slug}"
            page_url = f"https://jandawa.pages.dev/kendra/{page_slug}"
            generated_slugs.append(f"kendra/{page_slug}")

            store_count = len(store_list)

            # Build Schema.org ItemList with Pharmacy items
            schema_items = []
            for idx, s in enumerate(store_list[:25]):
                schema_items.append({
                    "@type": "Pharmacy",
                    "position": idx + 1,
                    "name": f"Pradhan Mantri Jan Aushadhi Kendra - {s['name']}",
                    "address": {
                        "@type": "PostalAddress",
                        "streetAddress": s['address'],
                        "addressLocality": dist_name,
                        "addressRegion": state_name,
                        "postalCode": s['pincode'] if s['pincode'] != 'null' else '',
                        "addressCountry": "IN"
                    },
                    "telephone": "+91-1800-180-8080"
                })

            schema_json = json.dumps({
                "@context": "https://schema.org",
                "@type": "ItemList",
                "name": f"Jan Aushadhi Kendras in {dist_name}, {state_name}",
                "description": f"Official list of {store_count} Pradhan Mantri Jan Aushadhi stores in {dist_name}, {state_name}",
                "itemListElement": schema_items
            }, ensure_ascii=False)

            # Pre-render Store Cards HTML
            store_cards_html = []
            for s in store_list:
                pin_display = f"- <strong class='text-slate-900'>{s['pincode']}</strong>" if s['pincode'] and s['pincode'] != 'null' else ''
                gmaps_query = urllib.parse.quote(f"Pradhan Mantri Jan Aushadhi Kendra {s['name']} {s['address']} {s['pincode']}")
                gmaps_link = f"https://www.google.com/maps/search/?api=1&query={gmaps_query}"
                
                card = f"""
                <div class="store-card bg-white border border-slate-200 hover:border-blue-500/50 rounded-2xl p-5 shadow-sm transition-all flex flex-col justify-between"
                     data-search="{s['name'].lower()} {s['address'].lower()} {s['pincode']} {s['code'].lower()}">
                  <div>
                    <div class="flex items-center justify-between gap-2 mb-2">
                      <span class="text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-blue-50 text-blue-700 border border-blue-200">
                        {s['code']}
                      </span>
                      <span class="text-[11px] font-semibold px-2 py-0.5 rounded bg-emerald-50 text-emerald-800">
                        सुबह 9:00 - रात 9:00 (अधिकृत)
                      </span>
                    </div>

                    <h3 class="font-bold text-sm sm:text-base text-slate-900 leading-snug">{s['name']}</h3>
                    <p class="text-xs text-slate-600 mt-1.5 leading-relaxed">
                      {s['address']} {pin_display}
                    </p>

                    <div class="mt-3 p-2.5 rounded-xl bg-slate-50 border border-slate-100 text-xs text-slate-600 space-y-0.5">
                      <div>ज़िला व राज्य: <strong class="text-slate-800">{dist_name}, {state_name}</strong></div>
                      <div class="text-slate-500">PMBJP टोल-फ्री हेल्पलाइन: <strong>1800-180-8080</strong></div>
                    </div>
                  </div>

                  <div class="mt-4 pt-3 border-t border-slate-100 flex gap-2">
                    <a href="{gmaps_link}" target="_blank" rel="noopener" class="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2.5 rounded-xl text-xs transition text-center shadow flex items-center justify-center gap-1.5">
                      <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                      </svg>
                      <span>Google Maps पर रास्ता</span>
                    </a>
                    <a href="tel:18001808080" class="px-3.5 py-2.5 border border-slate-200 hover:bg-slate-50 rounded-xl text-xs font-semibold text-slate-700 flex items-center justify-center" title="हेल्पलाइन कॉल">
                      हेल्पलाइन
                    </a>
                  </div>
                </div>
                """
                store_cards_html.append(card)

            stores_rendered = "\n".join(store_cards_html)

            # Other districts links
            other_dist_links = []
            for od in other_districts[:12]:
                if od != dist_name:
                    od_slug = f"{state_slug}-{slugify(od)}"
                    other_dist_links.append(f'<a href="/kendra/{od_slug}.html" class="px-2.5 py-1 bg-slate-100 hover:bg-blue-50 hover:text-blue-700 rounded-lg text-xs font-medium text-slate-700 transition">{od}</a>')
            other_dist_html = " ".join(other_dist_links)

            page_html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jan Aushadhi Kendra in {dist_name}, {state_name} - All {store_count} Stores, Address & Map | JanDawa</title>
  <meta name="description" content="{dist_name} ({state_name}) के सभी {store_count} प्रधानमंत्री जन औषधि केंद्र: पूरा पता, पिनकोड, ड्रग कोड और गूगल मैप्स रास्ता। 2,513 सरकारी जेनेरिक दवाएं 80% तक सस्ती प्राप्त करें।">
  <meta name="keywords" content="jan aushadhi kendra in {dist_name}, {dist_name} jan aushadhi list, {dist_name} medical store pmbjp, generic medicine {dist_name}, {state_name} jan aushadhi">
  
  <link rel="canonical" href="{page_url}">
  <meta property="og:title" content="{dist_name} में जन औषधि केंद्र - सभी {store_count} दुकानों की सूची व गूगल मैप्स">
  <meta property="og:description" content="{dist_name} ({state_name}) के सभी {store_count} अधिकृत सरकारी जन औषधि केंद्रों का पता और दिशा-निर्देश देखें।">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{page_url}">

  <!-- Tailwind CSS -->
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>

  <!-- Google Rich Snippets: ItemList / Local Pharmacy Schema -->
  <script type="application/ld+json">
  {schema_json}
  </script>
</head>
<body class="bg-slate-50 text-slate-800 antialiased min-h-screen flex flex-col font-sans">

  <!-- Header -->
  <header class="bg-white border-b border-slate-200 sticky top-0 z-30">
    <div class="max-w-6xl mx-auto px-4 py-3.5 flex items-center justify-between">
      <a href="/" class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-emerald-600 flex items-center justify-center text-white font-bold text-base">
          +
        </div>
        <div>
          <span class="font-extrabold text-xl text-slate-900 tracking-tight">Jan<span class="text-emerald-700">Dawa</span></span>
          <span class="hidden sm:inline-block ml-1.5 px-2 py-0.5 rounded text-[10px] font-semibold bg-emerald-50 text-emerald-800 border border-emerald-200">जन औषधि</span>
        </div>
      </a>
      <div class="flex items-center gap-2">
        <a href="/" class="text-xs font-semibold px-3 py-2 rounded-xl text-slate-700 hover:bg-slate-100 transition">दवा खोजक (2,513 दवाएं)</a>
        <a href="/kendra/" class="text-xs font-semibold px-3.5 py-2 rounded-xl bg-blue-50 text-blue-700 border border-blue-200 transition">सभी 777 ज़िले</a>
      </div>
    </div>
  </header>

  <!-- Hero Banner -->
  <div class="bg-gradient-to-b from-white to-slate-50 border-b border-slate-200/80 py-8 px-4">
    <div class="max-w-4xl mx-auto space-y-3">
      <!-- Breadcrumbs -->
      <nav class="text-xs text-slate-500 flex items-center gap-1.5 flex-wrap">
        <a href="/" class="hover:text-emerald-700 font-semibold">होम (Home)</a> <span>›</span>
        <a href="/kendra/" class="hover:text-emerald-700 font-semibold">केंद्र डायरेक्टरी</a> <span>›</span>
        <span class="text-slate-600">{state_name}</span> <span>›</span>
        <span class="text-slate-900 font-bold">{dist_name}</span>
      </nav>

      <div class="inline-flex items-center gap-1.5 bg-blue-50 text-blue-700 px-3 py-1 rounded-full text-xs font-bold">
        <span>📍</span> {state_name} ➔ {dist_name} ज़िला
      </div>

      <h1 class="text-2xl sm:text-3xl md:text-4xl font-extrabold text-slate-900 tracking-tight leading-tight">
        {dist_name} के सभी {store_count} जन औषधि केंद्र
      </h1>
      <p class="text-xs sm:text-sm text-slate-600 max-w-2xl leading-relaxed">
        {dist_name} ({state_name}) में भारत सरकार की प्रधानमंत्री भारतीय जन औषधि परियोजना (PMBJP) के तहत संचालित सभी अधिकृत दुकानों का सत्यापित पता, पिनकोड, ड्रग कोड और गूगल मैप्स रास्ता देखें।
      </p>

      <!-- Instant Filter Bar -->
      <div class="pt-2 max-w-xl">
        <div class="relative">
          <input 
            id="districtFilterInput" 
            type="text" 
            placeholder="{dist_name} में पिनकोड, इलाका या दुकान का नाम खोजें (उदा: 342001)..." 
            class="w-full bg-white border border-slate-300 rounded-2xl px-4 py-3 text-xs sm:text-sm text-slate-900 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm"
          />
        </div>
      </div>
    </div>
  </div>

  <!-- Content Section -->
  <main class="max-w-6xl mx-auto px-4 py-8 flex-1 w-full space-y-6">

    <!-- Store Count Meta -->
    <div class="flex items-center justify-between text-xs text-slate-500 border-b border-slate-200 pb-3">
      <div>
        कुल केंद्र: <strong id="visibleCount" class="text-slate-900 font-bold">{store_count}</strong> (100% सरकारी अधिकृत)
      </div>
      <a href="/" class="text-emerald-700 font-semibold hover:underline">
        दवाओं के सरकारी विकल्प देखें ➔
      </a>
    </div>

    <!-- Stores Grid -->
    <div id="storesGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
      {stores_rendered}
    </div>

    <!-- No Match State -->
    <div id="noMatchMsg" class="hidden bg-white border border-slate-200 rounded-2xl p-8 text-center space-y-2">
      <h3 class="font-bold text-base text-slate-800">इस सर्च के लिए कोई केंद्र नहीं मिला</h3>
      <p class="text-xs text-slate-500">कृपया केवल पिनकोड के 6 अंक या इलाके का नाम लिखकर देखें।</p>
    </div>

    <!-- Other Districts in this State -->
    <div class="bg-white border border-slate-200 rounded-2xl p-5 sm:p-6 space-y-3 mt-8">
      <h3 class="text-sm font-bold text-slate-900">{state_name} के अन्य ज़िले देखें:</h3>
      <div class="flex flex-wrap gap-1.5">
        {other_dist_html}
      </div>
    </div>

  </main>

  <!-- Footer -->
  <footer class="bg-white border-t border-slate-200 py-8 px-4 text-xs text-slate-500 text-center leading-relaxed space-y-2 mt-auto">
    <div>© 2026 <strong>JanDawa (जन दवा)</strong>. भारत सरकार PMBJP डेटा पर आधारित जनहित में 100% निशुल्क सेवा।</div>
    <div class="flex items-center justify-center gap-4 text-slate-600 font-medium">
      <a href="/" class="hover:text-emerald-700">होम</a>
      <a href="/kendra/" class="hover:text-emerald-700">सभी केंद्र</a>
      <a href="/sitemap.xml" class="hover:text-emerald-700">Sitemap</a>
      <a href="/disclaimer.html" class="hover:text-emerald-700">Disclaimer</a>
    </div>
  </footer>

  <!-- Instant Search Script -->
  <script>
    const filterInput = document.getElementById('districtFilterInput');
    const storeCards = document.querySelectorAll('.store-card');
    const visibleCountEl = document.getElementById('visibleCount');
    const noMatchMsg = document.getElementById('noMatchMsg');

    filterInput?.addEventListener('input', (e) => {{
      const q = e.target.value.trim().toLowerCase();
      let matched = 0;

      storeCards.forEach(card => {{
        const searchData = card.getAttribute('data-search') || '';
        if (!q || searchData.includes(q)) {{
          card.classList.remove('hidden');
          matched++;
        }} else {{
          card.classList.add('hidden');
        }}
      }});

      if (visibleCountEl) visibleCountEl.innerText = matched;
      if (noMatchMsg) {{
        if (matched === 0) noMatchMsg.classList.remove('hidden');
        else noMatchMsg.classList.add('hidden');
      }}
    }});
  </script>
</body>
</html>
"""
            out_file = os.path.join(OUTPUT_DIR, f"{page_slug}.html")
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(page_html)

    print(f"Generated {len(generated_slugs)} district pages in {OUTPUT_DIR}")

    # 2. Generate Master Kendra Directory Index Page with Interactive Search (kendra/index.html)
    directory_html_sections = []
    for state_name, districts in sorted(by_state_dist.items()):
        state_slug = slugify(state_name)
        total_state_stores = sum(len(sl) for sl in districts.values())
        dist_links = []
        for dist_name in sorted(districts.keys()):
            dist_slug = slugify(dist_name)
            count = len(districts[dist_name])
            dist_links.append(f'<a href="/kendra/{state_slug}-{dist_slug}.html" class="dist-link px-2.5 py-1.5 rounded-xl bg-slate-50 hover:bg-blue-50 hover:text-blue-700 border border-slate-200 text-xs font-semibold text-slate-800 transition flex items-center justify-between gap-2" data-name="{dist_name.lower()}" data-state="{state_name.lower()}" data-slug="/kendra/{state_slug}-{dist_slug}.html"><span>{dist_name}</span> <span class="text-[10px] bg-white px-1.5 py-0.5 rounded border border-slate-200 text-slate-500 font-mono">{count}</span></a>')
        
        links_block = "\n".join(dist_links)
        directory_html_sections.append(f"""
        <div class="state-block bg-white border border-slate-200 rounded-2xl p-5 sm:p-6 space-y-4" data-state="{state_name.lower()}">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h2 class="text-base sm:text-lg font-bold text-slate-900">{state_name}</h2>
            <span class="text-xs font-extrabold text-blue-700 bg-blue-50 border border-blue-200 px-3 py-1 rounded-full">{total_state_stores:,} केंद्र</span>
          </div>
          <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2">
            {links_block}
          </div>
        </div>
        """)

    all_sections_rendered = "\n".join(directory_html_sections)
    pin_map_json = json.dumps(pin_map, ensure_ascii=False)

    index_page_html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>All India Jan Aushadhi Kendra Directory - 21,745 Stores in 777 Districts | JanDawa</title>
  <meta name="description" content="पूरे भारत के 36 राज्यों और 777 ज़िलों के सभी 21,745 प्रधानमंत्री जन औषधि केंद्रों की आधिकारिक डायरेक्टरी। ज़िला, शहर या पिनकोड डालकर तुरंत केंद्र का पता व गूगल मैप्स रास्ता देखें।">
  <link rel="canonical" href="https://jandawa.pages.dev/kendra/">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
</head>
<body class="bg-slate-50 text-slate-800 antialiased min-h-screen flex flex-col font-sans">
  <header class="bg-white border-b border-slate-200 sticky top-0 z-30">
    <div class="max-w-6xl mx-auto px-4 py-3.5 flex items-center justify-between">
      <a href="/" class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-emerald-600 flex items-center justify-center text-white font-bold text-base">+</div>
        <div>
          <span class="font-extrabold text-xl text-slate-900 tracking-tight">Jan<span class="text-emerald-700">Dawa</span></span>
          <span class="hidden sm:inline-block ml-1.5 px-2 py-0.5 rounded text-[10px] font-semibold bg-emerald-50 text-emerald-800 border border-emerald-200">जन औषधि</span>
        </div>
      </a>
      <a href="/" class="text-xs font-semibold px-4 py-2 rounded-xl bg-emerald-700 text-white shadow hover:bg-emerald-800 transition">
        2,513 दवाओं के विकल्प ➔
      </a>
    </div>
  </header>

  <!-- Hero with Master Search Bar -->
  <div class="bg-gradient-to-b from-white to-slate-50 border-b border-slate-200/80 py-8 px-4 text-center space-y-4">
    <div class="inline-flex items-center gap-1.5 bg-blue-50 text-blue-700 px-3 py-1 rounded-full text-xs font-bold">
      <span>🇮🇳</span> अखिल भारतीय जन औषधि केंद्र डायरेक्टरी
    </div>
    <h1 class="text-2xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
      देशभर के 21,745 केंद्र (777 ज़िले)
    </h1>
    <p class="text-xs sm:text-sm text-slate-600 max-w-xl mx-auto">
      अपना ज़िला, शहर या 6-अंकीय पिनकोड डालें और सीधे अपने नजदीकी केंद्रों का पता और गूगल मैप्स रास्ता देखें:
    </p>

    <!-- Master Search Bar with Search Button -->
    <div class="max-w-2xl mx-auto pt-2">
      <div class="bg-white rounded-2xl shadow-md border-2 border-slate-300 focus-within:border-blue-600 p-2 flex gap-2 transition-all">
        <div class="relative flex-1 flex items-center">
          <svg class="w-5 h-5 absolute left-3 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          <input 
            id="kendraMasterSearch" 
            type="text" 
            autocomplete="off"
            placeholder="ज़िले का नाम (उदा: Jodhpur), शहर, राज्य या 6-अंकीय पिनकोड..." 
            class="w-full pl-10 pr-3 py-3 text-sm sm:text-base text-slate-900 placeholder-slate-400 focus:outline-none bg-transparent"
          />
        </div>
        <button id="searchDirectoryBtn" onclick="runMasterDirectorySearch()" class="bg-blue-600 hover:bg-blue-700 text-white font-bold px-6 py-3 rounded-xl text-xs sm:text-sm transition flex items-center justify-center gap-1.5 shadow">
          <span>खोजें</span>
        </button>
      </div>

      <!-- Live Pincode / Direct Match Result Banner -->
      <div id="pincodeMatchBanner" class="hidden mt-3 p-4 bg-emerald-50 border border-emerald-200 rounded-2xl text-left flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 shadow-sm">
        <div>
          <div class="text-[11px] font-bold text-emerald-800 uppercase tracking-wider">🎯 सटीक पिनकोड मैच</div>
          <div id="pincodeMatchText" class="text-sm font-extrabold text-emerald-950 mt-0.5"></div>
          <div class="text-xs text-emerald-700 mt-0.5">इस ज़िले के सभी अधिकृत केंद्र, पता और गूगल मैप्स देखें</div>
        </div>
        <a id="pincodeMatchLink" href="#" class="shrink-0 bg-emerald-700 hover:bg-emerald-800 text-white font-bold px-5 py-2.5 rounded-xl text-xs transition shadow flex items-center gap-1">
          <span>केंद्र सूची खोलें ➔</span>
        </a>
      </div>

      <!-- Quick Popular City Chips -->
      <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs text-slate-500 mt-3">
        <span class="font-medium text-slate-400">अक्सर खोजे जाने वाले:</span>
        <button onclick="setDirectorySearch('Jodhpur')" class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 hover:border-blue-500 hover:text-blue-700 font-semibold transition">जोधपुर</button>
        <button onclick="setDirectorySearch('Jaipur')" class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 hover:border-blue-500 hover:text-blue-700 font-semibold transition">जयपुर</button>
        <button onclick="setDirectorySearch('Lucknow')" class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 hover:border-blue-500 hover:text-blue-700 font-semibold transition">लखनऊ</button>
        <button onclick="setDirectorySearch('Patna')" class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 hover:border-blue-500 hover:text-blue-700 font-semibold transition">पटना</button>
        <button onclick="setDirectorySearch('Indore')" class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 hover:border-blue-500 hover:text-blue-700 font-semibold transition">इंदौर</button>
        <button onclick="setDirectorySearch('Bhopal')" class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 hover:border-blue-500 hover:text-blue-700 font-semibold transition">भोपाल</button>
        <button onclick="setDirectorySearch('Delhi')" class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 hover:border-blue-500 hover:text-blue-700 font-semibold transition">दिल्ली</button>
        <button onclick="setDirectorySearch('Mumbai')" class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 hover:border-blue-500 hover:text-blue-700 font-semibold transition">मुंबई</button>
      </div>
    </div>
  </div>

  <main class="max-w-6xl mx-auto px-4 py-8 flex-1 w-full space-y-6">
    <div id="noMatchBox" class="hidden bg-white border border-slate-200 rounded-2xl p-8 text-center space-y-3">
      <h3 class="font-bold text-base text-slate-800">कोई ज़िला या केंद्र नहीं मिला</h3>
      <p class="text-xs text-slate-500">कृपया ज़िले की स्पेलिंग जांचें या 6-अंकीय पिनकोड डालकर देखें।</p>
      <button onclick="setDirectorySearch('')" class="text-xs font-bold text-blue-700 bg-blue-50 px-4 py-2 rounded-xl border border-blue-200 hover:bg-blue-100 transition">
        सभी ज़िले दोबारा दिखाएं
      </button>
    </div>

    <div id="directoryContainer" class="space-y-6">
      {all_sections_rendered}
    </div>
  </main>

  <footer class="bg-white border-t border-slate-200 py-8 px-4 text-xs text-slate-500 text-center space-y-2 mt-auto">
    <div>© 2026 <strong>JanDawa (जन दवा)</strong>. 100% निशुल्क सरकारी जन औषधि खोज मंच।</div>
    <div class="flex items-center justify-center gap-4 text-slate-600 font-medium">
      <a href="/" class="hover:text-emerald-700">होम</a>
      <a href="/sitemap.xml" class="hover:text-emerald-700">Sitemap</a>
      <a href="/disclaimer.html" class="hover:text-emerald-700">Disclaimer</a>
    </div>
  </footer>

  <!-- Search & Pincode Filter Script -->
  <script>
    const pinMap = {pin_map_json};
    const searchInput = document.getElementById('kendraMasterSearch');
    const stateBlocks = document.querySelectorAll('.state-block');
    const distLinks = document.querySelectorAll('.dist-link');
    const pincodeBanner = document.getElementById('pincodeMatchBanner');
    const pincodeText = document.getElementById('pincodeMatchText');
    const pincodeLink = document.getElementById('pincodeMatchLink');
    const noMatchBox = document.getElementById('noMatchBox');

    function filterDirectory(q) {{
      q = q.trim().toLowerCase();

      // Check if 6-digit pincode
      if (/^\\d{{6}}$/.test(q)) {{
        if (pinMap[q]) {{
          const item = pinMap[q];
          pincodeText.innerText = 'पिनकोड ' + q + ' ➔ ' + item.d + ' (' + item.s + ')';
          pincodeLink.href = item.u;
          pincodeBanner.classList.remove('hidden');
          // Filter to that district
          q = item.d.toLowerCase();
        }} else {{
          pincodeBanner.classList.add('hidden');
        }}
      }} else {{
        pincodeBanner.classList.add('hidden');
      }}

      let visibleStates = 0;
      let matchedDistricts = 0;

      stateBlocks.forEach(sb => {{
        const stateName = sb.getAttribute('data-state') || '';
        const stateMatches = stateName.includes(q);
        const links = sb.querySelectorAll('.dist-link');
        let visibleLinksInState = 0;

        links.forEach(l => {{
          const dName = l.getAttribute('data-name') || '';
          if (!q || stateMatches || dName.includes(q)) {{
            l.classList.remove('hidden');
            visibleLinksInState++;
            matchedDistricts++;
          }} else {{
            l.classList.add('hidden');
          }}
        }});

        if (!q || visibleLinksInState > 0) {{
          sb.classList.remove('hidden');
          visibleStates++;
        }} else {{
          sb.classList.add('hidden');
        }}
      }});

      if (noMatchBox) {{
        if (visibleStates === 0 && matchedDistricts === 0) {{
          noMatchBox.classList.remove('hidden');
        }} else {{
          noMatchBox.classList.add('hidden');
        }}
      }}
    }}

    function runMasterDirectorySearch() {{
      const q = searchInput.value.trim().toLowerCase();
      if (!q) return;

      // If 6-digit pin matches, directly navigate
      if (/^\\d{{6}}$/.test(q) && pinMap[q]) {{
        window.location.href = pinMap[q].u;
        return;
      }}

      // Check if exact 1 district matches
      const visibleLinks = document.querySelectorAll('.dist-link:not(.hidden)');
      if (visibleLinks.length === 1) {{
        window.location.href = visibleLinks[0].href;
        return;
      }}

      // Otherwise scroll down to results
      const firstVisible = document.querySelector('.state-block:not(.hidden)');
      if (firstVisible) {{
        firstVisible.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}
    }}

    function setDirectorySearch(val) {{
      if (searchInput) {{
        searchInput.value = val;
        filterDirectory(val);
        if (val) {{
          const firstVisible = document.querySelector('.state-block:not(.hidden)');
          if (firstVisible) {{
            firstVisible.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
          }}
        }}
      }}
    }}

    searchInput?.addEventListener('input', (e) => {{
      filterDirectory(e.target.value);
    }});

    searchInput?.addEventListener('keydown', (e) => {{
      if (e.key === 'Enter') {{
        runMasterDirectorySearch();
      }}
    }});
  </script>
</body>
</html>
"""
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page_html)

    print("Generated Master Directory with Search at kendra/index.html")

    # 3. Update Sitemap
    base_url = "https://jandawa.pages.dev"
    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        f'  <url><loc>{base_url}/</loc><priority>1.0</priority></url>',
        f'  <url><loc>{base_url}/about.html</loc><priority>0.5</priority></url>',
        f'  <url><loc>{base_url}/privacy-policy.html</loc><priority>0.5</priority></url>',
        f'  <url><loc>{base_url}/disclaimer.html</loc><priority>0.5</priority></url>',
        f'  <url><loc>{base_url}/kendra/</loc><priority>0.9</priority></url>'
    ]

    sub_dir = os.path.join(SCRATCH_DIR, "substitute")
    if os.path.exists(sub_dir):
        for fname in sorted(os.listdir(sub_dir)):
            if fname.endswith(".html"):
                sitemap_lines.append(f'  <url><loc>{base_url}/substitute/{fname}</loc><priority>0.8</priority></url>')

    for kslug in sorted(generated_slugs):
        sitemap_lines.append(f'  <url><loc>{base_url}/{kslug}</loc><priority>0.85</priority></url>')

    sitemap_lines.append('</urlset>')

    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_lines))

    print(f"Updated {SITEMAP_PATH} with {len(sitemap_lines) - 3} URLs!")

if __name__ == '__main__':
    main()
