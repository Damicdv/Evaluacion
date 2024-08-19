from PIL import Image
imagen = str(input("ingrese la ruta de una imagen: "))
img = Image.open(imagen)
img.show()
img.save("Mirawe.jpg")