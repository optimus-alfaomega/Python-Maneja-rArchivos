from os import strerror
archivo ='C:/Users/Fabio/Documents/Curso_Python/Ejercicios/manejoArchivos/'
#la lectura del archivo es mas eficiente dado que solo almacena por lineas 
try:
    ccnt = lcnt = 0
    s = open(archivo +'archivo1.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCaracteres en el archivo: ", ccnt)
    print("Lineas en el archivo:     ", lcnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))