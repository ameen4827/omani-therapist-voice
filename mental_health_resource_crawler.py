# mental_health_resource_crawler.py

import aiohttp
import asyncio
from bs4 import BeautifulSoup

# 🌐 Mental health content sources (WHO EMRO & Oman MoH)
mental_health_urls = [
    "https://www.emro.who.int/mnh/get-connected/get-connected.html",
    "https://www.emro.who.int/mnh/publications/training-resources.html",
    "https://www.emro.who.int/mnh/videos/index.html",
    "https://www.emro.who.int/mnh/what-you-can-do/index.html",
    "https://moh.gov.om/en/health-promotion/health-awareness/?year=0&c=11683"
]

# 🧠 Label → keyword map
context_keywords = {
    "crisis_suicide": ["suicide", "crisis", "kill", "life", "prevent", "emergency"],
    "general_anxiety": ["anxiety", "worry", "panic", "stress", "calm", "overwhelm"],
    "depression": ["depression", "hopeless", "sadness", "mood"],
    "negative_self_talk": ["self-esteem", "worthless", "failure", "confidence"],
    "catastrophic_thinking": ["catastrophic", "disaster", "worst", "never improve"],
    "avoidance_withdrawal": ["isolation", "withdrawal", "avoid", "disconnect", "stay home"],
    "sleep_disorder": ["sleep", "insomnia", "restless", "nightmare"],
    "anger": ["anger", "frustration", "rage", "aggression"],
    "family_stress": ["family", "relationships", "parent", "spouse", "conflict"],
    "trauma": ["trauma", "violence", "abuse", "nightmare", "ptsd"],
    "work_stress": ["work", "job", "burnout", "career", "pressure"]
}

# ⏬ Fetch a URL's HTML
async def fetch(session, url):
    try:
        async with session.get(url, timeout=15) as resp:
            if resp.status == 200:
                return url, await resp.text()
            return url, None
    except Exception:
        return url, None

# 🔍 Extract meaningful links
def extract_links_from_html(base_url, html):
    soup = BeautifulSoup(html, "html.parser")
    links = []

    for a in soup.find_all("a", href=True):
        text = a.get_text(strip=True)
        href = a["href"]

        # Skip very short or empty text
        if not text or len(text) < 4:
            continue

        # Convert relative URL to absolute
        if href.startswith("/"):
            base = "/".join(base_url.split("/")[:3])
            href = base + href

        if href.startswith("http"):
            links.append({"text": text, "url": href})

    return links

# 🚀 Crawl all sources
async def crawl_all_resources():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in mental_health_urls]
        responses = await asyncio.gather(*tasks)

    results = {}
    for url, html in responses:
        results[url] = extract_links_from_html(url, html) if html else []
    return results

# 🏷️ Label each link with a context
def label_links_by_context(all_links):
    labeled_links = []

    for domain_links in all_links.values():
        for link in domain_links:
            combined = (link["text"] + " " + link["url"]).lower()
            matched_label = None

            for label, keywords in context_keywords.items():
                if any(kw.lower() in combined for kw in keywords):
                    matched_label = label
                    break

            labeled_links.append({
                "text": link["text"],
                "url": link["url"],
                "label": matched_label or "unclassified"
            })

    return labeled_links

#  Manual test
if __name__ == "__main__":
    import json

    loop = asyncio.get_event_loop()
    raw_links = loop.run_until_complete(crawl_all_resources())
    labeled = label_links_by_context(raw_links)

    with open("labeled_links.json", "w", encoding="utf-8") as f:
        json.dump(labeled, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Saved {len(labeled)} labeled links to labeled_links.json")
