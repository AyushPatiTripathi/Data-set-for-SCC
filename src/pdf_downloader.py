import requests
import os

def download_pdf(url, filename):

    response = requests.get(url)

    with open(filename, "wb") as f:
        f.write(response.content)

    print("Downloaded:", filename)
