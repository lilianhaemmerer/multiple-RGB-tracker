def coordonneesRGB_2_hexadecimalRGB(tableau):
	#tableau de dimension 3
	retourchaine = ""
	for i in tableau:
		retourchaine = retourchaine + dec2hex(i)
	retourchaine = "#" + retourchaine
	return(retourchaine)

def unitehexadecimal(i):
	#i entre 0 et 15
	if i < 10:
		return str(i)
	if i == 10:
		return("a")
	if i == 11:
		return("b")
	if i == 12:
		return("c")
	if i == 13:
		return("d")
	if i == 14:
		return("e")
	return ("f")

def dec2hex(i):
	#i inferieur à 255
	return (unitehexadecimal(i//16)+unitehexadecimal(i%16))
