print("Calculadora de propina en Python")

while True:
    respuesta = input("¿Desea dejar propina? (Sí/No): ").strip().lower()

    if respuesta == "si":
        porcentaje = float(input("Introduce el porcentaje de propina que deseas dar (por ejemplo, 15 para el 15%): "))
        resultado = (porcentaje / 100) 
        print(f"La propina es: {resultado:.2f}")
        break  #sal del bucle mientras se haya dado una respuesta válida
    elif respuesta == "no":
        print("No se dará propina.")
        break  #sal del bucle mientras se haya dado una respuesta válida
    else:
        print("Error: Por favor, responda 'Sí' o 'No'.")
