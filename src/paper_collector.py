import requests
import json

BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

def search_papers(query, limit=100):

    params = {
        "query": query,
        "limit": limit,
        "fields": "title,year,authors,openAccessPdf,externalIds"
    }

    response = requests.get(BASE_URL, params=params)

    data = response.json()

    papers = []

    for p in data["data"]:

        paper = {
            "title": p.get("title"),
            "year": p.get("year"),
            "doi": p.get("externalIds", {}).get("DOI"),
            "pdf_url": None
        }

        if p.get("openAccessPdf"):
            paper["pdf_url"] = p["openAccessPdf"]["url"]

        papers.append(paper)

    return papers


if __name__ == "__main__":

    papers = search_papers("self compacting concrete mix design", 50)

    for p in papers:
        print(p)
