"""
JanDawa Programmatic SEO Page Generator & Sitemap Updater
Reads medicines_master.json and generates high-ranking HTML pages for top medicines
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
    slug = med.get("slug", "med-" + str(med.get("id", 1)))
    brand_name = med.get("brandName") or med.get("brand_name", "Generic Medicine")
    alt_brands = brand_name
    active_salt = med.get("activeSalt") or med.get("active_salt", brand_name)
    strength = med.get("strength", "10s")
    category = med.get("category", "General")
    category_hi = med.get("category_hi", "सामान्य")
    manufacturer = med.get("manufacturer", "भारतीय फार्मास्युटिकल मानक")
    dosage_form = "Tablets / Capsules"
    
    b_mrp = float(med.get("brandPrice") or med.get("brand_mrp", 50))
    brand_mrp = f"{b_mrp:.2f}"
    unit_size = med.get("unitSize") or med.get("unit_size", "10s")
    
    jan_name = med.get("genericName") or med.get("saltName", brand_name)
    jan_code = med.get("drugCode") or "PMBJP00001"
    j_mrp = float(med.get("janAushadhiPrice") or 10.0)
    jan_mrp = f"{j_mrp:.2f}"
    
    saving_pct = med.get("savingPercent", 80)
    s_amt = b_mrp - j_mrp
    saving_amt = f"{s_amt:.2f}"
    yearly_saving_num = s_amt * 12
    yearly_saving = f"{yearly_saving_num:.2f}"

    html_content = f"""<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{brand_name} Generic Substitute & Jan Aushadhi Price | {active_salt} - JanDawa</title>
  <meta name="description" content="{brand_name} का सस्ता जेनेरिक विकल्प: {jan_name}। जन औषधि केंद्र पर कीमत मात्र ₹{jan_mrp} (सीधी {saving_pct}% की बचत)। साल्ट कंपोजिशन, उपयोग और फार्मेसी पर्चा देखें।">
  <meta name="keywords" content="{brand_name} substitute, {brand_name} generic alternative, {active_salt} price, jan aushadhi {brand_name}">
  
  <!-- Open Graph for WhatsApp / Social Previews -->
  <meta property="og:title" content="{brand_name} की जगह जन औषधि की यह दवा लें, बचेंगे ₹{saving_amt}">
  <meta property="og:description" content="{brand_name} (₹{brand_mrp}) के बदले जन औषधि केंद्र पर {jan_name} मात्र ₹{jan_mrp} में उपलब्ध है।">
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
        "dosageForm": "{dosage_form}",
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
              "text": "जन औषधि केंद्र पर यह दवा {jan_name} (ड्रग कोड: {jan_code}) के नाम से मात्र ₹{jan_mrp} प्रति {unit_size} में मिलती है, जो ब्रांडेड दवा से {saving_pct}% सस्ती है।"
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
          <p class="text-xs text-slate-500">निर्माता: {manufacturer}</p>
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
            <span class="text-xs text-emerald-800 font-semibold">({unit_size})</span>
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
        <a href="https://jandawa.pages.dev" class="px-5 py-3 border border-slate-300 hover:bg-slate-50 rounded-xl text-sm font-semibold text-slate-700 text-center">
          अन्य दवाएं खोजें
        </a>
      </div>
    </div>

    <!-- FAQ Section for SEO -->
    <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm space-y-4">
      <h3 class="text-lg font-bold text-slate-900">अक्सर पूछे जाने वाले सवाल (FAQs)</h3>
      
      <div class="space-y-3 text-sm">
        <div class="p-3 bg-slate-50 rounded-xl border border-slate-100">
          <p class="font-bold text-slate-800">क्या जन औषधि की {jan_name} ब्रांडेड {brand_name} जितनी ही असरदार है?</p>
          <p class="text-slate-600 mt-1">हाँ! दोनों दवाओं में एक ही सक्रिय रासायनिक साल्ट ({active_salt}) और क्षमता ({strength}) होती है। भारत सरकार की NABL मान्यता प्राप्त लैब में जांच के बाद ही जन औषधि केंद्र पर दवाएं आती हैं।</p>
        </div>

        <div class="p-3 bg-slate-50 rounded-xl border border-slate-100">
          <p class="font-bold text-slate-800">यह दवा जन औषधि केंद्र पर कैसे मांगें?</p>
          <p class="text-slate-600 mt-1">दुकानदार को ब्रांड का नाम न बोलकर साल्ट का नाम <strong>"{jan_name}"</strong> या ड्रग कोड <strong>"{jan_code}"</strong> बताएं।</p>
        </div>
      </div>
    </div>
  </main>

  <!-- Footer -->
  <footer class="max-w-4xl mx-auto mt-12 pt-6 border-t border-slate-200 text-center text-xs text-slate-400 space-y-2">
    <div>© 2026 JanDawa. 100% नि:शुल्क जनहित स्वास्थ्य सेवा।</div>
    <div>डेटा स्रोत: BPPI (Pharmaceuticals & Medical Devices Bureau of India)</div>
  </footer>

</body>
</html>"""

    file_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    return slug

def update_sitemap(slugs):
    base_url = "https://jandawa.pages.dev"
    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        f'  <url><loc>{base_url}/</loc><priority>1.0</priority><changefreq>daily</changefreq></url>',
        f'  <url><loc>{base_url}/about.html</loc><priority>0.5</priority></url>',
        f'  <url><loc>{base_url}/privacy-policy.html</loc><priority>0.5</priority></url>',
        f'  <url><loc>{base_url}/disclaimer.html</loc><priority>0.5</priority></url>'
    ]

    for slug in slugs:
        sitemap_lines.append(f'  <url><loc>{base_url}/substitute/{slug}.html</loc><priority>0.8</priority></url>')

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
    # Generate top 100 high volume medicines for SEO
    for med in medicines[:100]:
        slug = generate_page(med)
        generated.append(slug)

    update_sitemap(generated)
    print(f"Successfully generated {len(generated)} programmatic SEO pages and updated sitemap.xml!")

if __name__ == "__main__":
    main()
