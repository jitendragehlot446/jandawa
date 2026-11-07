"""
NewSalt Programmatic SEO Page Generator & Sitemap Updater
Reads medicines_master.json and generates high-ranking HTML pages for each medicine
with Google Rich Snippets (Schema.org JSON-LD), AdSense slots, Pharmacist slip,
and automatically updates sitemap.xml!
"""

import json
import os

SCRATCH_DIR = os.path.dirname(__file__)
MASTER_JSON_PATH = os.path.join(SCRATCH_DIR, "medicines_master.json")
OUTPUT_DIR = os.path.join(SCRATCH_DIR, "substitute")
SITEMAP_PATH = os.path.join(SCRATCH_DIR, "sitemap.xml")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_page(med):
    slug = med["slug"]
    brand_name = med["brand_name"]
    alt_brands = ", ".join(med["alternative_brands"])
    active_salt = med["active_salt"]
    strength = med["strength"]
    category = med["category"]
    category_hi = med["category_hi"]
    brand_mrp = f"{med['brand_mrp']:.2f}"
    unit_size = med["unit_size"]
    jan = med["jan_aushadhi"]
    jan_name = jan["generic_name"]
    jan_code = jan["drug_code"]
    jan_mrp = f"{jan['mrp']:.2f}"
    savings = med["savings"]
    saving_pct = savings["percentage"]
    saving_amt = f"{savings['amount']:.2f}"
    yearly_saving = f"{savings['yearly_saving']:.2f}"

    html_content = f"""<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{brand_name} Generic Substitute & Jan Aushadhi Price | {active_salt} - NewSalt</title>
  <meta name="description" content="{brand_name} का सस्ता जेनेरिक विकल्प: {jan_name}। जन औषधि केंद्र पर कीमत मात्र ₹{jan_mrp} (सीधी {saving_pct}% की बचत)। साल्ट कंपोजिशन, उपयोग और फार्मेसी पर्चा देखें।">
  <meta name="keywords" content="{brand_name} substitute, {brand_name} generic alternative, {active_salt} price, jan aushadhi {brand_name}, {alt_brands}">
  
  <!-- Open Graph for WhatsApp / Social Previews -->
  <meta property="og:title" content="{brand_name} की जगह जन औषधि में कौन सी दवा लें? ₹{jan_mrp} में उपलब्ध">
  <meta property="og:description" content="ब्रांडेड कीमत ₹{brand_mrp} के मुकाबले जन औषधि पर मात्र ₹{jan_mrp}। सालाना बचत ₹{yearly_saving}!">
  <meta property="og:type" content="article">

  <!-- Tailwind CSS -->
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>

  <!-- Google Rich Snippets: Drug & FAQ Schema (Schema.org JSON-LD) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Drug",
        "name": "{brand_name}",
        "activeIngredient": "{active_salt}",
        "dosageForm": "{med['dosage_form']}",
        "category": "{category}",
        "proprietaryName": "{brand_name}",
        "nonProprietaryName": "{jan_name}"
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "{brand_name} का साल्ट (Composition) क्या है?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{brand_name} में मुख्य सक्रिय साल्ट {active_salt} ({strength}) होता है।"
            }}
          }},
          {{
            "@type": "Question",
            "name": "जन औषधि केंद्र पर {brand_name} के विकल्प की कीमत क्या है?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "जन औषधि केंद्र पर यह दवा {jan_name} (ड्रग कोड: {jan_code}) के नाम से मात्र ₹{jan_mrp} प्रति {jan['unit_size']} में मिलती है, जो ब्रांडेड दवा से {saving_pct}% सस्ती है।"
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body class="bg-slate-50 text-slate-800 antialiased min-h-screen p-4 md:p-8">

  <!-- Header & Breadcrumbs -->
  <header class="max-w-4xl mx-auto mb-6">
    <nav class="text-xs text-slate-500 mb-3 flex items-center gap-1.5">
      <a href="/" class="hover:text-emerald-600 font-semibold">होम</a> <span>›</span>
      <span class="text-slate-600">{category_hi}</span> <span>›</span>
      <span class="text-slate-800 font-bold">{brand_name} Substitute</span>
    </nav>
    <div class="inline-flex items-center gap-1.5 bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full text-xs font-bold mb-2">
      <span>●</span> 100% सटीक साल्ट मैच (Same Active Salt)
    </div>
    <h1 class="text-2xl md:text-4xl font-extrabold text-slate-900 leading-tight">
      {brand_name} का जेनेरिक विकल्प एवं जन औषधि दर
    </h1>
    <p class="text-slate-600 text-sm md:text-base mt-1">
      सक्रिय साल्ट: <span class="font-bold text-slate-800">{active_salt} ({strength})</span> | श्रेणी: {category_hi}
    </p>
  </header>

  <!-- Top Ad Slot -->
  <div class="max-w-4xl mx-auto mb-6 p-3 bg-white border border-dashed border-slate-300 rounded-xl text-center text-xs text-slate-400">
    [ Google AdSense Responsive Display Ad Slot (728x90 / 320x50) ]
  </div>

  <!-- Comparison Card -->
  <main class="max-w-4xl mx-auto space-y-6">
    <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
        <!-- Branded Side -->
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <div class="text-xs font-semibold text-slate-500 uppercase">ब्रांडेड दवा (Market Brand)</div>
          <h2 class="text-xl font-bold text-slate-800 mt-1">{brand_name}</h2>
          <p class="text-xs text-slate-500">निर्माता: {med['manufacturer']}</p>
          <div class="mt-4 flex items-baseline gap-2">
            <span class="text-2xl font-bold text-red-600 line-through">₹{brand_mrp}</span>
            <span class="text-xs text-slate-500">({unit_size})</span>
          </div>
          <p class="text-xs text-slate-500 mt-1">अन्य समान ब्रांड: {alt_brands}</p>
        </div>

        <!-- Jan Aushadhi Side -->
        <div class="p-5 rounded-xl bg-emerald-50 border border-emerald-300 relative">
          <div class="absolute -top-3 right-4 bg-emerald-600 text-white text-xs font-bold px-3 py-0.5 rounded-full shadow">
            {saving_pct}% सीधी बचत
          </div>
          <div class="text-xs font-bold text-emerald-800 uppercase">प्रधानमंत्री जन औषधि केंद्र विकल्प</div>
          <h2 class="text-lg md:text-xl font-extrabold text-emerald-950 mt-1">{jan_name}</h2>
          <div class="text-xs text-emerald-700 mt-1">
            ड्रग कोड: <code class="bg-white px-1.5 py-0.5 rounded border border-emerald-300 font-bold">{jan_code}</code>
          </div>
          <div class="mt-4 flex items-baseline gap-2">
            <span class="text-3xl font-black text-emerald-700">₹{jan_mrp}</span>
            <span class="text-xs text-emerald-800 font-semibold">({jan['unit_size']})</span>
          </div>
          <p class="text-xs font-semibold text-emerald-800 mt-1">
            प्रति पैक बचत: ₹{saving_amt} | <strong>सालाना बचत: ₹{yearly_saving}</strong>
          </p>
        </div>
      </div>

      <!-- Action Button -->
      <div class="mt-6 pt-4 border-t border-slate-100 flex flex-col sm:flex-row gap-3">
        <button onclick="window.print()" class="flex-1 bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3 rounded-xl text-sm transition shadow flex items-center justify-center gap-2">
          <span>📋</span> जन औषधि केंद्र के लिए पर्चा प्रिंट करें
        </button>
        <a href="https://janaushadhi.gov.in" target="_blank" class="px-5 py-3 border border-slate-300 hover:bg-slate-50 rounded-xl text-sm font-semibold text-slate-700 text-center">
          📍 नजदीकी केंद्र खोजें
        </a>
      </div>
    </div>

    <!-- In-Article Ad Slot -->
    <div class="p-4 bg-white border border-dashed border-slate-300 rounded-xl text-center text-xs text-slate-400">
      [ Google AdSense In-Article Native Ad Slot ]
    </div>

    <!-- Medicine FAQs Section -->
    <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm space-y-4">
      <h3 class="text-lg font-bold text-slate-900 border-b border-slate-100 pb-2">
        {brand_name} के बारे में अक्सर पूछे जाने वाले सवाल (FAQs)
      </h3>
      <div>
        <h4 class="font-bold text-sm text-slate-800">1. क्या {brand_name} और जन औषधि की दवा में कोई अंतर है?</h4>
        <p class="text-xs md:text-sm text-slate-600 mt-1">
          नहीं, दोनों में सक्रिय साल्ट <strong>{active_salt} ({strength})</strong> बिल्कुल समान है। भारत सरकार द्वारा प्रमाणित NABL लैब्स में जांच के बाद ही इसे उपलब्ध कराया जाता है।
        </p>
      </div>
      <div>
        <h4 class="font-bold text-sm text-slate-800">2. जन औषधि केंद्र पर मैं यह दवा कैसे मांगूं?</h4>
        <p class="text-xs md:text-sm text-slate-600 mt-1">
          स्टोर संचालक को बताएं कि आपको <strong>{active_salt} {strength}</strong> (ड्रग कोड: <code>{jan_code}</code>) चाहिए।
        </p>
      </div>
    </div>

    <!-- Disclaimer -->
    <footer class="p-4 bg-amber-50 border border-amber-200 rounded-xl text-xs text-amber-900">
      <strong>⚠️ मेडिकल अस्वीकरण:</strong> यह जानकारी केवल जन-जागरूकता के लिए है। किसी भी दवा को बदलने से पहले अपने डॉक्टर से सलाह अवश्य लें।
    </footer>
  </main>
</body>
</html>
"""
    file_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    return slug

def update_sitemap(slugs):
    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        '  <url>',
        '    <loc>https://jandawa.pages.dev/</loc>',
        '    <lastmod>2026-11-08</lastmod>',
        '    <changefreq>daily</changefreq>',
        '    <priority>1.0</priority>',
        '  </url>',
        '  <url>',
        '    <loc>https://jandawa.pages.dev/about.html</loc>',
        '    <lastmod>2026-11-08</lastmod>',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.5</priority>',
        '  </url>',
        '  <url>',
        '    <loc>https://jandawa.pages.dev/disclaimer.html</loc>',
        '    <lastmod>2026-11-08</lastmod>',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.5</priority>',
        '  </url>',
        '  <url>',
        '    <loc>https://jandawa.pages.dev/privacy-policy.html</loc>',
        '    <lastmod>2026-11-08</lastmod>',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.5</priority>',
        '  </url>'
    ]

    for slug in slugs:
        sitemap_lines.extend([
            '  <url>',
            f'    <loc>https://jandawa.pages.dev/substitute/{slug}.html</loc>',
            '    <lastmod>2026-11-08</lastmod>',
            '    <changefreq>weekly</changefreq>',
            '    <priority>0.9</priority>',
            '  </url>'
        ])

    sitemap_lines.append('</urlset>')

    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_lines))

def main():
    if not os.path.exists(MASTER_JSON_PATH):
        print(f"File not found: {MASTER_JSON_PATH}")
        return

    with open(MASTER_JSON_PATH, "r", encoding="utf-8") as f:
        medicines = json.load(f)

    generated = []
    for med in medicines:
        slug = generate_page(med)
        generated.append(slug)

    update_sitemap(generated)
    print(f"Successfully generated {len(generated)} programmatic SEO pages and updated sitemap.xml!")

if __name__ == "__main__":
    main()
