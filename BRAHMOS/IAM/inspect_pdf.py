
from pdfminer.high_level import extract_text
import os

files = ["ISIM Part 1.pdf"]

for pdf_path in files:
    if os.path.exists(pdf_path):
        print(f"=== {pdf_path} ===")
        # Extract all text (or limit pages if possible, but high_level does all)
        # We can pass page_numbers=[10,11,12] etc.
        try:
            text = extract_text(pdf_path, page_numbers=[10, 11, 12, 13, 14])
            print(text)
        except Exception as e:
            print(f"Error: {e}")
        print("\n")
