from os import strerror
archivo ='C:/Users/Fabio/Documents/Curso_Python/Ejercicios/manejoArchivos/'
try:
	ccnt = lcnt = 0
	for line in open(archivo +'archivo1.txt', 'rt',encoding="UTF-8"):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCaracteres en el archivo: ", ccnt)
	print("Lineas en el archivo:     ", lcnt)
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))