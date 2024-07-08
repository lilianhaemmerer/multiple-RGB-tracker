from math import sqrt

def is_in_Boule_Norme_1(vector3, centre, rayon):
    somme = 0
    for i in range(3):
        somme = somme + abs(vector3[i] - centre[i])
    if (somme >= rayon):
        return False
    return True

def is_in_Boule_Norme_2(vector3, centre, rayon):
    somme = 0
    for i in range(3):
        somme = somme + (vector3[i] - centre[i])**2
    if (sqrt(somme) >= rayon) :
        return False
    return True

def is_in_Boule_Norme_inf(vector3, centre, rayon):
    coord_relatives = []
    for i in range (3):
        coord_relatives.append(abs(vector3[i] - centre[i]))
    if (max(coord_relatives) >= rayon):
        return False
    return True