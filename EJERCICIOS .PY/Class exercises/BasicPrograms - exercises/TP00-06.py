# Realizar  un  programa  donde  se  vayan  ingresando  las  calificaciones  de  los  alumnos  de  un  curso.  Luego  de  ingresar  la calificación del último alumno, se ingresará un -1 para terminar la carga. El programa informará entonces la calificación promedio del curso.

notas = int(input("Ingrese la calificacion del alumno: "))
acum = 0
totalNotas = 0
while notas != -1:
    acum += 1
    totalNotas = totalNotas + notas
    notas = int(input("Ingrese la calificacion del alumno: "))


print("El promedio de notas es de: ")
print(totalNotas / acum)