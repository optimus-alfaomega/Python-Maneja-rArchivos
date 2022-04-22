from os import strerror

try:
	fo = open('textoNuevo.txt', 'wt') #un nuevo archivo (textoNuevo.txt) es creado
	for i in range(20):
		s = "línea #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))