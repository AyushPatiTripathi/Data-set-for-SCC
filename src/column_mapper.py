import json
import pandas as pd

with open("configs/parameter_map.json") as f:
    PARAM_MAP = json.load(f)

def map_columns(df):

    mapped = {}

    for col in df.columns:

        col_lower = col.lower()

        for param, keywords in PARAM_MAP.items():

            for key in keywords:

                if key in col_lower:
                    mapped[param] = df[col]

    return pd.DataFrame(mapped)
