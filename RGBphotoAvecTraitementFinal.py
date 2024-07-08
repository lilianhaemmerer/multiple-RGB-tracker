import matplotlib.pyplot as plt
import fonction_rgb
import acces_memoire as memo

plt.style.use('_mpl-gallery')

#img = pil.open(nomImage)
image = memo.telechargementImageUnique("ImageTest7RGB.JPG")
hauteur = len(image)
largeur = len(image[0])
tableauSignatures = []
tableauSansRepetition = []
imageSansRepetition = []



def signatureDirecte(tab):
       return(tab[0] + 1000*tab[1] + 1000 * 1000 * tab[2])
def signatureReciproque(nombre):
       retour = []
       retour.append(nombre%1000)
       nombre = (nombre - retour[0])//1000
       retour.append(nombre%1000)
       nombre = (nombre - retour[0])//1000
       retour.append(nombre%1000)
       return retour

print ("definition des fonction faites")
"""
print(signatureDirecte([255,255,255]))
print(signatureReciproque(255255255))
"""

print ("begin")



for ligne in range (hauteur):
       for colonne in range (largeur):
              tableauSignatures.append(signatureDirecte(image[ligne][colonne]))
 
print ("fin du remplissage des signatures")

tableauSignatures.sort()

print ("fin du tri du tableauSignatures")

memoire = tableauSignatures[0]
tableauSansRepetition.append(memoire)

for element in range(1, len(tableauSignatures)):
       if (tableauSignatures[element] != memoire):
              memoire = tableauSignatures[element]
              tableauSansRepetition.append(memoire)

print (len(tableauSignatures), len(tableauSansRepetition))
print ("rate :", len(tableauSansRepetition) / len(tableauSignatures))

imageSansRepetition = [signatureReciproque(element) for element in tableauSansRepetition]
print ("retour aux coordonnées RGB")




########################################################################################
#partie graphique

couleursstr = []
xs = [element[0] for element in imageSansRepetition]
ys = [element[1] for element in imageSansRepetition]
zs = [element[2] for element in imageSansRepetition]
for i in imageSansRepetition:
       couleursstr.append(fonction_rgb.coordonneesRGB_2_hexadecimalRGB(i))

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(xs, ys, zs, c = couleursstr, marker = "s", alpha = 1)
"""
ax.set(xticklabels=["rouge"],
       yticklabels=["vert"],
       zticklabels=["bleu"])
"""
ax.set_xlim(0, 256)
ax.set_ylim(0, 256)
ax.set_zlim(0, 256)

ax.set(xlabel='Rouge')
ax.set(ylabel='Vert')
ax.set(zlabel='Bleu')

plt.show()