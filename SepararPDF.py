from PyPDF2 import PdfWriter, PdfReader
from datetime import datetime
import os
def croppingPages(pdf,pages):
     reader = PdfReader(pdf)
     writer = PdfWriter()

     now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

     path = os.path.join("pdf_processed",now)

     os.makedirs(path,True)


     for numPage in pages:
          writer.add_page(reader.pages[numPage-1])

     with open(f"{path}/{pdf}","wb") as mypdf:
          writer.write(mypdf)

     writer.close()

     os.remove(pdf)     

if __name__ == "__main__":
     croppingPages("LESSON8.pdf",[4,5])



