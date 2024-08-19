from PIL import Image
marcar = str(input("Ingrese la ruta de una imagen a marcar: "))
logo = str(input("Ingrese la ruta de un logo: "))
img = Image.open(marcar)
logito = Image.open(logo)
logov2 = logito.resize((50,50))
print("""
      Opciones para marcar:
      
    1 Superior izquierda
    
    2 Superior derecha
    
    3 Inferior izquierda
    
    4 Inferior derecha
    
      """)
option = int(input())
if option == 1:
    img.paste(logov2,(50,50))
    img.save("Arribaizquierda.jpg")
    img.show()
else:
    if option == 2:
        img.paste(logov2,(img.height-logov2.height-50,50))
        img.save("Arribaderecha.jpg")
        img.show()
    else:
        if option == 3:
            img.paste(logov2,(50,img.width-logov2.width-50))
            img.save("abajoIzquierda.jpg")
            img.show()
        else:
            if option == 4:
                img.paste(logov2,(img.height-logov2.height-50,img.width-logov2.width-50))
                img.save("abajoDerecha.jpg")
                img.show()