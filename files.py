"""
ORDENAR CARPETA DE DESCARGAS!




IMPORTANTE!!!!!!!!!!!! <--------
REEMPLAZAR NOMBRE DE USUARIO!!!!  <----------





------ NECESARIO DENTRO DE LA CARPETA DOCUMENTOS:
-IMG
-TORRENTS
-PDF
-Aplications
-ZIP


ORDENA ARCHIVOS DE LOS SIGUIENTES TIPOS:

.ZIP \ .RAR
.JPG \ .JPEG \ .PNG
.EXE
.TORRENT
.PDF

"""


from PIL import Image
import os

Folder = "C:\\Users\\JZ9\\Downloads\\"



if __name__ == "__main__":
    for filename in os.listdir(Folder):
        name, extension = os.path.splitext(Folder + filename)
        
        if extension in [".jpg",".jpeg",".png"]:
            img = "C:\\Users\\JZ9\\Documents\\IMG\\"
            os.rename(Folder + filename, img + filename)
            print(name + " : " + extension)

        if extension in [".exe"]:
            aplications = "C:\\Users\\JZ9\\Documents\\Aplications\\"
            os.rename(Folder + filename)
            print(name + " : " + extension, aplications + filename)       
        
        if extension in [".torrent"]:
            torrents = "C:\\Users\\JZ9\\Documents\\Torrents\\"
            os.rename(Folder + filename)
            print(name + " : " + extension, torrents + filename)

        if extension in [".pdf"]:
            PDF = "C:\\Users\\JZ9\\Documents\\PDF\\"
            os.rename(Folder + filename, PDF + filename)
            print(name + " : " + extension)


        if extension in [".zip", ".rar"]:
            ZIP = "C:\\Users\\JZ9\\Documents\\ZIP\\"
            os.rename(Folder + filename, ZIP + filename)
            print(name + " : " + extension)