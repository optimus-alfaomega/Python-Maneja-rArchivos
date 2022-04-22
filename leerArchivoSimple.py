# se abre el archivo tzop.txt en modo lectura, devolviéndolo como un objeto de archivo
stream = open("C:/Users/Fabio/Documents/Curso_Python/Ejercicios/manejoArchivos/archivo1.txt", "rt", encoding = "utf-8") 
print(stream.read()) # se imprime el contenido del archivo