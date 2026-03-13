def validate_row(row):

    if row["cement_kg_m3"] < 250:
        return False

    if row["slump_flow_mm"] < 500:
        return False

    if row["compressive_strength_mpa"] < 10:
        return False

    return True
