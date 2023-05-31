# Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor estricto).  En  caso  de  no  existir  el  mayor  estricto  devolver -1.  No  utilizar  operadores  lógicos  (and,  or,  not).  Desarrollar también  un  programa  para  ingresar  los  tres  valores,  invocar  a  la  función  y  mostrar  el  máximo  hallado,  o  un  mensaje informativo si éste no existe.

def mayorDeTres(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
    if num2 > num3:
        if num2 > num1:
            return num2
    if num3 > num1:
        if num3 > num2:
            return num3
            
    return -1

num1 = int(input("Ingrese primer valor: "))
num2 = int(input("Ingrese segundo valor: "))
num3 = int(input("Ingrese tercer valor: "))
num = mayorDeTres(num1, num2, num3)            

if num == -1:
    print("Los numeros ingresados no tienen mayor estricto")
else:
    print(num)    