def Suma(num1,num2):
    return num1+num2


num1=int(input ("Escribir un numero"))
num2=int(input ("Escribir un segundo numero"))
resultado=Suma(num1,num2)
if resultado>100:
    resultado=resultado/5
else:
    resultado=resultado*2
print("El resultado es: ",resultado)