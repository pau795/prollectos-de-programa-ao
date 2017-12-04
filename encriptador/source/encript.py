"""
######################################################################
# POGRAMAÇAO                                                         #
######################################################################
"""

#kek
def rot13(text):
	"""Encriptador de rotacion en 13"""
	texto_encriptado = ""
	alfabeto = range(0, 27)
	for c in text:
		posicion = ord(c)-ord("a")
		posicion2 = (posicion + 13)%26
		car_final = posicion2+ord("a")
		texto_encriptado += chr(car_final)
	return texto_encriptado

def rotn(text, n):
	"""Encriptador de rotacion en n. Sustituye la letra por la que esta
	13 posiciones en adelante. Si n=13, el encriptador funciona como
	desencriptador"""
	texto_encriptado = ""
	alfabeto = range(0, 27)
	for c in text:
		posicion = ord(c)-ord("a")
		posicion2 = (posicion + n)%26
		car_final = posicion2+ord("a")
		texto_encriptado += chr(car_final)
	return texto_encriptado

	

print(rot13(input()))

