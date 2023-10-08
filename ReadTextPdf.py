from PyPDF2 import PdfReader

reader = PdfReader("LESSON5Proccessed.pdf")

page = reader.pages[0]

print(page.extract_text())