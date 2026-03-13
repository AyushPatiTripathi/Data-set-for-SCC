import pandas as pd
import requests
import os
from tqdm import tqdm

DATA = pd.read_csv("data/paper_metadata.csv")

SAVE_DIR = "data/raw_papers"

os.makedirs(SAVE_DIR, exist_ok=True)

for i,row in tqdm(DATA.iterrows(), total=len(DATA)):

    url = row["pdf_url"]

    if pd.isna(url):
        continue

    try:

        r = requests.get(url, timeout=15)

        filename = SAVE_DIR + f"/paper_{i}.pdf"

        with open(filename,"wb") as f:
            f.write(r.content)

    except:
        pass
