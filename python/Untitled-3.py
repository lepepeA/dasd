print ("Porcentaje python prueba")
gasto = int(input("Introduce el gasto total:\n"))

respuesta = bool(input("¿ Desea dejar propina ? \n"))
if respuesta.lower() == "Yes":
    continuar = True
else: 
 print("el programa cierrara :")
if continuar:
    print("El programa continuará.")
 porcentaje = (input("Introduce la cantidad de porcentaje de propina que quieres dar:"))
resultado = (porcentaje / 100) * gasto


print("La propina es: "+ str(resultado) )
else: print("El programa se cerrara.")