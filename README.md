# allendowney.github.io

Root site for https://allendowney.github.io/. The book sites are separate GitHub Pages project sites at `/<RepoName>/`.

This repo holds only:
- `index.html`: a page linking to the book sites
- `robots.txt`: lists each book's sitemap (only the domain root can have a robots.txt)
- `sitemap.xml`: a sitemap index of those sitemaps, generated from `robots.txt` by `make_sitemap_index.py` (run it after adding a `Sitemap:` line)
- search engine verification files (Google Search Console, Bing Webmaster Tools)

Do not set a custom domain on this repo; that would redirect every project site to the custom domain.
