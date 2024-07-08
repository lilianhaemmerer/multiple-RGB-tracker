import PIL.Image as pil

def telechargementImageUnique(nom_image):
    img = pil.open(nom_image)
    print()
    print("l'image ",nom_image," a été ouverte")
    largeur, hauteur = img.size
    #print (largeur, hauteur)
    retourTab = []
    for j in range(hauteur):
        tabLigne = []
        for i in range(largeur):
            r, g, b = img.getpixel((i, j ))
            tabLigne.append([r, g, b])
        retourTab.append(tabLigne)
    img.close()
    print("l'image ",nom_image," a été fermée")
    return (retourTab)

def nom_image(nom_video: str, numero: int)->str:
    if numero < 10:
        nom = nom_video + "000" + str(numero) + ".png"
    elif (numero >= 10) and (numero < 100):
        nom = nom_video + "00" + str(numero) + ".png"
    else:
        nom = nom_video + "0" + str(numero) + ".png"
    return (nom)



