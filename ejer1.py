import PIL.Image
ruta = str(input("Ingrese la ruta de una imagen: "))
img = PIL.Image.open(ruta)
img.show()
print(f"""
      Nombre = {img.filename}
      Extension = {img.format}
      Resolucion = {img.size}
      Cantidad de px = {img.width+img.height}px
      Ubicacion = {ruta}
      """)