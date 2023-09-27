print("*********************")
print("CAlculadora en python")
print("*********************")

print("Eliga un numero dependiendo del tipo de operacion que quiera hacer")
operacion = input("1)Suma\n 2)Resta\n 3)Multiplicacion\n 4)Division\n 5)Division exacta\n 6)Exponente\n 7)Modulo o resto")
if operacion == "1":
    numero = input("De el primero numero: ")
    numero += input("De el segundo numero: ")
    print("el numero es ", numero)
    
elif operacion == "2":
    numero = int(input("da el primer numero: "))
    numero -= int(input("da el segundo numero: "))
    print ("el numero es ", numero)
    
    
elif operacion == "3":
     numero = int(input("da el primer numero: "))
     numero *= int(input("da el segundo numero: "))
     print("Su resultado es: ", numero)
elif operacion == "4":
      numero = float(input("da el primer numero: "))
      numero /= float(input("da el segundo numero: "))
      print("Su resultado es: ", numero)
elif operacion == "5":
     numero = int(input("da el primer numero: "))
     numero //= int(input("da el segundo numero: "))
     print("Su resultado es ", numero)
elif operacion == "6":
     numero = int(input("da el primer numero: "))
     numero **= int(input("da el segundo numero: "))
     print("Su resultado es ", numero)
elif operacion == "7":
     numero = int(input("da el primer numero: "))
     numero %= int(input("da el segundo numero: "))
     print("Su resultado es ", numero )
else:
     print("sa")


