from src.table_extractor import extract_tables
import os

PDF_FOLDER = "test_run/papers"
TABLE_FOLDER = "test_run/tables"

for pdf in os.listdir(PDF_FOLDER):

    if pdf.endswith(".pdf"):

        path = os.path.join(PDF_FOLDER, pdf)

        print("Processing:", pdf)

        extract_tables(path, TABLE_FOLDER)
