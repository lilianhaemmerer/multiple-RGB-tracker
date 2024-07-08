import matplotlib.pyplot as plt
import normes
import fonction_rgb
import numpy as np

plt.style.use('_mpl-gallery')


espaceInterPoints = 5
nombreDePoints = 256 // espaceInterPoints
x, y, z = 0, 0, 0
xs, ys, zs = [], [], []
couleursInt = []
couleursstr =[]
compteur = 0
couleur = [(50,150,210), (210,65,60), (30,30,30), (15,200,60), (200,200,200)]
rayon = 30
pointsbouleX, pointsbouleY, pointsbouleZ, couleurboule = [], [], [], []
for indiceX in range(nombreDePoints):
       for indiceY in range(nombreDePoints):
              for indiceZ in range(nombreDePoints):
                     xs.append(indiceX * espaceInterPoints)
                     ys.append(indiceY * espaceInterPoints)
                     zs.append(indiceZ * espaceInterPoints)
                     z = z + espaceInterPoints
                     couleursInt.append([indiceX * espaceInterPoints, indiceY * espaceInterPoints, indiceZ * espaceInterPoints])
                     compteur = compteur + 1
              y = y + espaceInterPoints
       x = x + espaceInterPoints

"""
for numero_point in range(compteur):
       vecteur = [xs[numero_point], ys[numero_point], zs[numero_point]]
       if normes.is_in_Boule_Norme_inf(vecteur, couleur, rayon) == True:
              pointsbouleX.append(xs[numero_point])
              pointsbouleY.append(ys[numero_point])
              pointsbouleZ.append(zs[numero_point])
              couleurboule.append(couleursInt[numero_point])
"""
for indiceCouleur in range(len(couleur)):
       for numero_point in range(compteur):
              vecteur = [xs[numero_point], ys[numero_point], zs[numero_point]]
              if normes.is_in_Boule_Norme_inf(vecteur, couleur[indiceCouleur], rayon) == True:
                     pointsbouleX.append(xs[numero_point])
                     pointsbouleY.append(ys[numero_point])
                     pointsbouleZ.append(zs[numero_point])
                     couleurboule.append(couleursInt[numero_point])



for i in couleurboule:
       couleursstr.append(fonction_rgb.coordonneesRGB_2_hexadecimalRGB(i))

print (compteur)
print (len(couleurboule))
#print (couleursInt)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(pointsbouleX, pointsbouleY, pointsbouleZ, c = couleursstr, marker = "s", alpha = 1)
#ax.scatter(pointsbouleX, pointsbouleY, pointsbouleZ, marker = "s", alpha = 1)
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


