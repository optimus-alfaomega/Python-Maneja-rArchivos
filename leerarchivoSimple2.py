
from os import strerror
#el leer un archivo muy grande (en terabytes) usando este método puede dañar tu sistema operativo 
archivo ='C:/Users/Fabio/Documents/Curso_Python/Ejercicios/manejoArchivos/'
try:
    cnt = 0
    s = open(archivo +'archivo1.txt', "rt")
    content = s.read() #volcado de memoria
    for ch in content:
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCaracteres en el archivo: ", cnt)
    print("\n\nlongitud de  el archivo: ", len(content))
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))