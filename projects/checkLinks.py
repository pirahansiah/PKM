import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def check_links(base_url, check_external=False):
    try:
        response = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)

        print(f"Scanning {base_url}... Found {len(links)} links.")
        broken = []
        ok = []

        for link in links:
            url = link['href']
            text = link.get_text(strip=True)[:50]

            # Skip anchors and empty
            if url.startswith('#') or not url:
                continue

            full_url = urljoin(base_url, url)
            parsed = urlparse(full_url)

            # Check internal links
            if parsed.netloc == urlparse(base_url).netloc:
                try:
                    res = requests.head(full_url, allow_redirects=True, timeout=5)
                    if res.status_code >= 400:
                        broken.append((res.status_code, full_url, text))
                        print(f"[BROKEN] {res.status_code}: {full_url} ({text})")
                    else:
                        ok.append(full_url)
                except Exception as e:
                    broken.append((0, full_url, text))
                    print(f"[ERROR] {full_url}: {e}")

            # Optionally check external links
            elif check_external:
                try:
                    res = requests.head(full_url, allow_redirects=True, timeout=5)
                    if res.status_code >= 400:
                        broken.append((res.status_code, full_url, text))
                        print(f"[BROKEN-EXT] {res.status_code}: {full_url} ({text})")
                except:
                    pass

        print(f"\nSummary: {len(ok)} OK, {len(broken)} broken")
        return broken
    except Exception as e:
        print(f"Failed to crawl {base_url}: {e}")
        return []

# Check multiple pages
pages = [
    "https://www.pirahansiah.com/",
    "https://www.pirahansiah.com/contents/public/Resources/",
    "https://www.pirahansiah.com/contents/public/coaching/",
    "https://www.pirahansiah.com/contents/public/links/",
]

all_broken = []
for page in pages:
    all_broken.extend(check_links(page))

print(f"\n=== TOTAL: {len(all_broken)} broken links across {len(pages)} pages ===")
