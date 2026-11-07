# JanDawa (जन दवा) - Affordable Generic Medicine Finder

> **Mission**: Empowering Indian families to reduce chronic healthcare costs by 70–90% through direct brand-to-PMBJP generic mapping, AI prescription scanning, and hyperlocal Jan Aushadhi Kendra discovery.

---

## 🚀 Live Website
- **URL**: [https://jandawa.pages.dev](https://jandawa.pages.dev)
- **Hosted on**: Cloudflare Pages (Global Edge Network, Unlimited Free Bandwidth)

---

## 🌟 Key Features
1. **Instant Brand-to-Salt Search**: Search 15+ top chronic care brands (Telma, Glycomet, Pan 40, Dolo, Montair, Shelcal) and view bioequivalent PMBJP generic salts, drug codes, and government MRPs.
2. **📸 AI Prescription & Blister Foil Scanner**: Upload photo of doctor prescription or medicine strip to extract active salts and calculate monthly basket savings.
3. **📍 Pincode & GPS Kendra Locator**: Enter any 6-digit Indian PIN code or city name to find nearest Jan Aushadhi Kendras with turn-by-turn Google Maps directions.
4. **📋 1-Click Pharmacist Slip**: Generate a formatted digital slip to show the store operator.
5. **📱 PWA & Offline Support**: Progressive Web App installable on mobile devices with offline service worker caching.
6. **💰 Google AdSense & Affiliate Ready**: Optimized ad slots and health checkup affiliate card compliant with YMYL medical policies.

---

## 📁 Repository Structure
```
├── index.html              # Main application UI & client-side search
├── sw.js                   # Offline PWA service worker
├── manifest.json           # Web app manifest
├── sitemap.xml             # Search Console sitemap
├── robots.txt              # Crawler instructions
├── about.html              # About mission & PMBI data attribution
├── disclaimer.html         # Medical & Legal disclaimer
├── privacy-policy.html     # Privacy policy for AdSense compliance
├── medicines_master.json   # Seed master dataset of Indian medicines
├── generate_seo_pages.py   # Programmatic SEO generator
├── PDA.md                  # Comprehensive Project Design & Architecture document
└── substitute/             # Programmatic SEO pages with Schema.org JSON-LD
    ├── telma-40.html
    ├── glycomet-500.html
    ├── dolo-650.html
    ├── pan-40.html
    └── ...
```

---

## 📄 License & Attribution
- Medicine pricing and composition data sourced from the **Pharmaceuticals & Medical Devices Bureau of India (PMBI)** (`janaushadhi.gov.in`).
- Licensed under MIT License.
