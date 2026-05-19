import os
import ads
from datetime import datetime

ads.config.token = os.environ["ADS_API_KEY"]

# Adjust query to your name/ORCID — ORCID is most reliable
query = ads.SearchQuery(
    q='orcid:0000-0000-0000-0000',  # or: author:("Song, N.")
    fl=["bibcode", "author", "title", "pub", "pubdate", "year",
        "volume", "page", "doi", "doctype", "citation_count"],
    sort="pubdate desc",
    max_pages=100,
)
papers = list(query)

# Separate first-author vs. co-author
first_author, coauthor = [], []
MY_LAST = "Song"  # adjust
for p in papers:
    if p.author and MY_LAST.lower() in p.author[0].lower():
        first_author.append(p)
    else:
        coauthor.append(p)

def format_paper(p):
    authors = ", ".join(p.author[:6]) if p.author else "—"
    if len(p.author) > 6:
        authors += " et al."
    title = p.title[0] if p.title else "Untitled"
    journal = p.pub or ""
    year = p.year or ""
    doi_link = f" [DOI](https://doi.org/{p.doi[0]})" if p.doi else ""
    ads_link = f" [ADS](https://ui.adsabs.harvard.edu/abs/{p.bibcode})"
    citations = f" ({p.citation_count} citations)" if p.citation_count else ""
    return f"- **{title}**  \n  {authors}  \n  *{journal}* ({year}){citations}{doi_link}{ads_link}\n"

lines = [
    f"# Publications\n",
    f"*Auto-updated {datetime.utcnow().strftime('%Y-%m-%d')} from NASA ADS.*\n",
    f"## First Author ({len(first_author)})\n",
]
lines += [format_paper(p) for p in first_author]
lines += [f"\n## Co-authored ({len(coauthor)})\n"]
lines += [format_paper(p) for p in coauthor]

with open("publications.md", "w") as f:
    f.write("\n".join(lines))

print(f"Written {len(papers)} papers.")
