import pandas as pd

dataset = []

dataset.append({
    "cement_kg_m3":420,
    "fly_ash_kg_m3":80,
    "water_kg_m3":180,
    "slump_flow_mm":710,
    "compressive_strength_mpa":52
})

df = pd.DataFrame(dataset)

df.to_csv("scc_dataset.csv", index=False)
