"""
AUTOMATIZACION:

COMPRESION DE IMAGENES!


"""




from pickletools import optimize
from PIL import Image
import os

Folder = "C:\\Users\\JZ9\\Downloads\\"

if __name__ == "__main__":
    for filename in os.listdir(Folder):
        name, extension = os.path.splitext(Folder + filename)
        
        if extension in [".jpg",".jpeg",".png"]:
            picture = Image.open(Folder+filename)
            picture.save(Folder + "compressed_"+filename, optimize=True, quality=60)
