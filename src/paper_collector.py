import requests

def search_papers(query, rows=20):

    url = "https://api.crossref.org/works"

    params = {
        "query": query,
        "rows": rows
    }

    response = requests.get(url, params=params)
    data = response.json()

    papers = []

    for item in data["message"]["items"]:

        paper = {
            "title": item.get("title", [""])[0],
            "doi": item.get("DOI"),
            "year": item.get("created", {}).get("date-parts", [[None]])[0][0]
        }

        papers.append(paper)

    return papers


if __name__ == "__main__":

    papers = search_papers("self compacting concrete mix design", 10)

    for p in papers:
        print(p)
