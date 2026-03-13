import pandas as pd

def parse_table(csv_file):

    df = pd.read_csv(csv_file)

    rows = []

    for _, r in df.iterrows():

        row = {

            "cement_kg_m3": r.get("Cement"),
            "fly_ash_kg_m3": r.get("Fly Ash"),
            "water_kg_m3": r.get("Water"),
            "slump_flow_mm": r.get("Slump Flow"),
            "compressive_strength_mpa": r.get("Strength")

        }

        rows.append(row)

    return rows
