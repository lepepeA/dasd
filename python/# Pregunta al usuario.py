respuesta = input("¿Desea continuar? (si/no): ")


continuar = False


if respuesta.lower() == "si":
    continuar = True
    print("El programa continuará.")
else:
    print("El programa se cerrará.")

