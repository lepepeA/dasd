def calcular_propina(total, porcentaje):
    propina = total * (porcentaje / 100)
    return propina

def main():
    print("Calculadora de Propinas")
    total = float(input("Ingrese el total de la factura: $"))
    
    print("Seleccione el porcentaje de propina:")
    print("1. 5%")
    print("2. 10%")
    print("3. 20%")
    
    opcion = int(input("Elija una opción (1/2/3): "))
    
    if opcion == 1:
        porcentaje = 5
    elif opcion == 2:
        porcentaje = 10
    elif opcion == 3:
        porcentaje = 20
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        return
    
    propina = calcular_propina(total, porcentaje)
    total_con_propina = total + propina
    
    print(f"Propina: ${propina:.2f}")
    print(f"Total con propina: ${total_con_propina:.2f}")

if __name__ == "__main__":
    main()
