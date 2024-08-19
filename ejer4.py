from PIL import Image
import os
ruta = str(input("Ingrese la ruta de una imagen: "))
if os.path.exists("recortes"):
    X = 0
if os.path.exists(ruta):
    if os.path.exists("recortes"):
        X=X+1
        img = Image.open(ruta)
        print(f"limites de la imagen:{img.size}")
        x0 = int(input("Ingrese la posición inicial en x: "))
        y0 = int(input("Ingrese la posición inicial en y: "))
        ancho = int(input("Ingrese el ancho: "))
        alto = int(input("Ingrese el alto: "))
        img2 = img.crop((x0,y0,ancho,alto))
        img2.save(f"recortes/recorte{X}.jpg")
    else:
        os.makedirs("recortes")
        img = Image.open(ruta)
        print(f"limites de la imagen:{img.size}")
        x0 = int(input("Ingrese la posición inicial en x: "))
        y0 = int(input("Ingrese la posición inicial en y: "))
        ancho = int(input("Ingrese el ancho: "))
        alto = int(input("Ingrese el alto: "))
        img2 = img.crop((x0,y0,ancho,alto))
        img2.save(f"recortes/recorte0.jpg")
else:
    print("~~ La ruta ingresada es erronea ~ ~")