from src.table_classifier import classify_table
import os

TABLE_FOLDER = "test_run/tables"

for file in os.listdir(TABLE_FOLDER):

    path = os.path.join(TABLE_FOLDER, file)

    table_type = classify_table(path)

    if table_type != "OTHER":

        print(table_type, ":", file)
