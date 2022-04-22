from os import strerror

try:
    cnt = 0
    archivo ='C:/Users/Fabio/Documents/Curso_Python/Ejercicios/manejoArchivos/'
    s = open(archivo +'archivo1.txt', "rt",encoding="utf-8")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCaracteres en el archivo: ", cnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))