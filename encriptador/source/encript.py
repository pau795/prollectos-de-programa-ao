"""
######################################################################
# POGRAMAÇAO                                                         #
######################################################################
"""

#kek
def rot13(text):
	texto_encriptado = ""
#	alfabeto = [chr(x) for x in range(ord("a"), ord("z")+1)]
	alfabeto = range(0, 27)
	for c in text:
		posicion = ord(c)-ord("a")
		posicion2 = (posicion + 13)%26
		car_final = posicion2+ord("a")
		texto_encriptado += chr(car_final)
	return texto_encriptado

print(rot13(input()))

