import os
import ads
from datetime import datetime

ads.config.token = os.environ["ADS_API_KEY"]

query = ads.SearchQuery(
    q='author:("Villanueva, N")',  # refine with ORCID if you have one
    fl=["bibcode", "author", "title", "pub", "pubdate", "year",
        "volume", "page", "doi", "doctype", "identifier"],
    sort="pubdate desc",
    max_pages=100,
)
papers = list(query)

def to_bibtex(p):
    authors = " and ".join(p.author) if p.author else ""
    title = p.title[0] if p.title else ""
    year = p.year or ""
    journal = p.pub or ""
    volume = p.volume or ""
    page = p.page[0] if p.page else ""
    doi = p.doi[0] if p.doi else ""
    bibcode = p.bibcode or ""
    doctype = p.doctype or "article"

    entry = f"@{doctype}{{{bibcode},\n"
    entry += f"  author = {{{authors}}},\n"
    entry += f"  title = {{{title}}},\n"
    entry += f"  journal = {{{journal}}},\n"
    entry += f"  year = {{{year}}},\n"
    if volume: entry += f"  volume = {{{volume}}},\n"
    if page:   entry += f"  pages = {{{page}}},\n"
    if doi:    entry += f"  doi = {{{doi}}},\n"
    entry += f"  adsurl = {{https://ui.adsabs.harvard.edu/abs/{bibcode}}},\n"
    entry += "}\n"
    return entry

bibtex = "\n".join(to_bibtex(p) for p in papers)

with open("_bibliography/papers.bib", "w") as f:
    f.write(bibtex)

print(f"Written {len(papers)} papers to _bibliography/papers.bib")
