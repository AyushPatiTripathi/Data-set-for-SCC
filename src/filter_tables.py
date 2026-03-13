import os
from table_classifier import is_scc_table

def filter_tables(table_folder):

    valid_tables = []

    for file in os.listdir(table_folder):

        if file.endswith(".csv"):

            path = os.path.join(table_folder, file)

            if is_scc_table(path):

                valid_tables.append(path)

    return valid_tables
