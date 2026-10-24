"""Write sitemap.xml, a sitemap index of the book and workshop sitemaps.

The list comes from the Sitemap: lines in robots.txt, so robots.txt stays the one
place to add a site. Run after editing robots.txt:

    python3 make_sitemap_index.py
"""

INDEX = "https://allendowney.github.io/sitemap.xml"

with open("robots.txt") as f:
    urls = [
        line.split(":", 1)[1].strip()
        for line in f
        if line.startswith("Sitemap:")
    ]
urls = [u for u in urls if u != INDEX]

lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    *[f"  <sitemap><loc>{u}</loc></sitemap>" for u in urls],
    "</sitemapindex>",
]
with open("sitemap.xml", "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"sitemap.xml: {len(urls)} sitemaps")
