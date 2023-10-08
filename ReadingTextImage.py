import pytesseract
from PIL import Image
import os


def read_text_image(image,filenametxt,dest_path):
     teseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
     pytesseract.pytesseract.tesseract_cmd = teseract_path


     imagen = Image.open(image)
     text = pytesseract.image_to_string(imagen)

     path_final = os.path.join(dest_path,filenametxt)

     if os.path.exists(path_final):
          with open(path_final,"a") as ar:
               ar.write(f"\n{text}")
     else:
          with open(path_final,"w") as ar:
               ar.write(text)     
     

     
if __name__ == "__main__":
     path = input("Dame la direccion de la imagen: ")
     read_text_image(r"{0}".format(path),"lesson8pt1.txt",r"C:\Users\Gabriel\Desktop")