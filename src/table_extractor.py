import camelot
import os

def extract_tables(pdf_path, output_dir):

    tables = camelot.read_pdf(pdf_path, pages="all")

    print("Tables found:", tables.n)

    os.makedirs(output_dir, exist_ok=True)

    for i, table in enumerate(tables):

        df = table.df

        file_path = os.path.join(output_dir, f"table_{i}.csv")

        df.to_csv(file_path, index=False)
