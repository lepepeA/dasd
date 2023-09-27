print("Porcentaje python prueba")
gasto = int(input("Introduce el gasto total:\n"))

respuesta = input("¿Desea dejar propina? (Yes/No)\n")
if respuesta == "Yes":
    continuar = True
else: 
    print("El programa se cerrará.")
    continuar = False

if continuar:
    print("El programa continuará.")
    porcentaje = int(input("Introduce la cantidad de porcentaje de propina que quieres dar:\n"))
    resultado = (porcentaje / 100) * gasto
    print("La propina es: " + str(resultado))