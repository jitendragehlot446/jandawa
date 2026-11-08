"""
JanDawa Programmatic Local SEO Generator for 777 Districts
Generates dedicated, high-ranking Kendra directory pages for every district in India,
with LocalBusiness / Pharmacy Schema.org JSON-LD, Google Maps links, search filter,
and updates sitemap.xml!
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
        k['district'] = k['district'].strip().title()

    by_state_dist = defaultdict(lambda: defaultdict(list))
    for k in kendras:
        by_state_dist[k['state']][k['district']].append(k)

    print(f"Total States: {len(by_state_dist)}")
    total_districts = sum(len(d) for d in by_state_dist.values())
    print(f"Total Districts: {total_districts}")

    generated_slugs = []

    # 1. Generate individual District Pages
    for state_name, districts in sorted(by_state_dist.items()):
        state_slug = slugify(state_name)
        other_districts = sorted(districts.keys())

        for dist_name, store_list in districts.items():
            dist_slug = slugify(dist_name)
            page_slug = f"{state_slug}-{dist_slug}"
            page_url = f"https://jandawa.pages.dev/kendra/{page_slug}.html"
            generated_slugs.append(f"kendra/{page_slug}.html")

            store_count = len(store_list)

            # Build Schema.org ItemList with Pharmacy items (top 20 for JSON-LD)
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
        <a href="/kendra/" class="text-xs font-semibold px-3.5 py-2 rounded-xl bg-blue-50 text-blue-700 border border-blue-200 transition">सभी ज़िले</a>
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

    # 2. Generate Master Kendra Directory Index Page (kendra/index.html)
    directory_html_sections = []
    for state_name, districts in sorted(by_state_dist.items()):
        state_slug = slugify(state_name)
        total_state_stores = sum(len(sl) for sl in districts.values())
        dist_links = []
        for dist_name in sorted(districts.keys()):
            dist_slug = slugify(dist_name)
            count = len(districts[dist_name])
            dist_links.append(f'<a href="/kendra/{state_slug}-{dist_slug}.html" class="px-2.5 py-1.5 rounded-xl bg-slate-50 hover:bg-blue-50 hover:text-blue-700 border border-slate-200 text-xs font-semibold text-slate-800 transition flex items-center justify-between gap-2"><span>{dist_name}</span> <span class="text-[10px] bg-white px-1.5 py-0.5 rounded border border-slate-200 text-slate-500 font-mono">{count}</span></a>')
        
        links_block = "\n".join(dist_links)
        directory_html_sections.append(f"""
        <div class="bg-white border border-slate-200 rounded-2xl p-5 sm:p-6 space-y-4">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h2 class="text-base sm:text-lg font-bold text-slate-900">{state_name}</h2>
            <span class="text-xs font-extrabold text-blue-700 bg-blue-50 border border-blue-200 px-3 py-1 rounded-full">{total_state_stores.toLocaleString('en-IN') if hasattr(total_state_stores, 'toLocaleString') else total_state_stores} केंद्र</span>
          </div>
          <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2">
            {links_block}
          </div>
        </div>
        """)

    all_sections_rendered = "\n".join(directory_html_sections)

    index_page_html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>All India Jan Aushadhi Kendra Directory - 21,745 Stores in 777 Districts | JanDawa</title>
  <meta name="description" content="पूरे भारत के 36 राज्यों और 777 ज़िलों के सभी 21,745 प्रधानमंत्री जन औषधि केंद्रों की आधिकारिक डायरेक्टरी। अपने ज़िले का चुनाव करें और केंद्र का पता व गूगल मैप्स देखें।">
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

  <div class="bg-gradient-to-b from-white to-slate-50 border-b border-slate-200/80 py-8 px-4 text-center space-y-3">
    <div class="inline-flex items-center gap-1.5 bg-blue-50 text-blue-700 px-3 py-1 rounded-full text-xs font-bold">
      <span>🇮🇳</span> अखिल भारतीय जन औषधि केंद्र डायरेक्टरी
    </div>
    <h1 class="text-2xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
      देशभर के 21,745 केंद्र (777 ज़िले)
    </h1>
    <p class="text-xs sm:text-sm text-slate-600 max-w-xl mx-auto">
      नीचे अपने राज्य और ज़िले का चुनाव करें और अपने नजदीकी अधिकृत केंद्र का पता, पिनकोड और दिशा-निर्देश देखें:
    </p>
  </div>

  <main class="max-w-6xl mx-auto px-4 py-8 flex-1 w-full space-y-6">
    {all_sections_rendered}
  </main>

  <footer class="bg-white border-t border-slate-200 py-8 px-4 text-xs text-slate-500 text-center space-y-2 mt-auto">
    <div>© 2026 <strong>JanDawa (जन दवा)</strong>. 100% निशुल्क सरकारी जन औषधि खोज मंच।</div>
    <div class="flex items-center justify-center gap-4 text-slate-600 font-medium">
      <a href="/" class="hover:text-emerald-700">होम</a>
      <a href="/sitemap.xml" class="hover:text-emerald-700">Sitemap</a>
      <a href="/disclaimer.html" class="hover:text-emerald-700">Disclaimer</a>
    </div>
  </footer>
</body>
</html>
"""
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page_html)

    print("Generated Master Directory at kendra/index.html")

    # 3. Update Sitemap with All 777 Kendra Pages + Directory
    # Read existing sitemap lines or rebuild
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

    # Add substitute pages
    sub_dir = os.path.join(SCRATCH_DIR, "substitute")
    if os.path.exists(sub_dir):
        for fname in sorted(os.listdir(sub_dir)):
            if fname.endswith(".html"):
                sitemap_lines.append(f'  <url><loc>{base_url}/substitute/{fname}</loc><priority>0.8</priority></url>')

    # Add all 777 Kendra district pages
    for kslug in sorted(generated_slugs):
        sitemap_lines.append(f'  <url><loc>{base_url}/{kslug}</loc><priority>0.85</priority></url>')

    sitemap_lines.append('</urlset>')

    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_lines))

    print(f"Updated {SITEMAP_PATH} with {len(sitemap_lines) - 3} URLs!")

if __name__ == '__main__':
    main()
