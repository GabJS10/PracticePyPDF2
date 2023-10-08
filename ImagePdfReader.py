from PyPDF2 import PdfReader
import os

def extractImages(path_pdf):
    folder_path = os.path.dirname(path_pdf)
    images_folder_path = os.path.join(folder_path,"images")
    os.makedirs(images_folder_path,True)

    reader = PdfReader(path_pdf)
    numberImage = 0
    for page in reader.pages:
        for image_file_object in page.images:
            with open(f"{images_folder_path}/{str(numberImage)}-{image_file_object.name}", "wb") as image:
              image.write(image_file_object.data)
              numberImage += 1     


if __name__ == "__main__":
    extractImages(r"C:\Users\Gabriel\Desktop\ProyectosDjango\PracticaPyPDF2\pdf_processed\2023-10-07 10-59-50\LESSON8.pdf")
