import pandas as pd

MATERIAL_KEYWORDS = [
    "specific gravity",
    "water absorption",
    "bulk density",
    "fineness modulus"
]

EXPERIMENT_KEYWORDS = [
    "cement",
    "fly ash",
    "slag",
    "superplasticizer",
    "slump",
    "compressive strength",
    "v-funnel"
]


def classify_table(csv_file):

    try:
        df = pd.read_csv(csv_file)

        text = df.to_string().lower()

        for word in EXPERIMENT_KEYWORDS:
            if word in text:
                return "EXPERIMENT_TABLE"

        for word in MATERIAL_KEYWORDS:
            if word in text:
                return "MATERIAL_TABLE"

        return "OTHER"

    except:
        return "OTHER"
