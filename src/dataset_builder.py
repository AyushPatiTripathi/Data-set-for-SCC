import pandas as pd
import os

def build_dataset(folder):

    rows = []

    for file in os.listdir(folder):

        if file.endswith(".csv"):

            df = pd.read_csv(os.path.join(folder,file))

            rows.append(df)

    dataset = pd.concat(rows)

    dataset.to_csv("final_dataset/scc_dataset.csv", index=False)
