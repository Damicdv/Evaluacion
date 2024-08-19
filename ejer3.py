from PIL import Image
ruta = str(input("Ingrese la ruta de su imagen: "))
rotacion = int(input("Ingrese un número para que su imagen sea rotada: "))
img = Image.open(ruta)
img.show()
img2 = img.rotate(rotacion)
img2.show()
img2.save(f"Rot.{img.format}")