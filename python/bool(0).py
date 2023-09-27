print("calculadora python prueba 2")
gasto = float(input("dime tu gasto completo: "))
while True:
 
 respuesta =  str(input("quieres dejar propina? (si/no)\n "))
 if respuesta == "si":
    print("De acuerdo")
    porcentaje = float(input("Dime el porcentaje de propina que quieres dejar(el porcentaje se agregara automaticamente): "))
    total = (porcentaje / 100) * gasto
    totalreal = round(total, 1)
    print("Ok tu gasto seria: " + str(gasto))
    print("La propina que dejarias seria: " + str(totalreal))
    print("Muchas gracias por la propina")
    break

 else: 
   respuesta == "no": print("ok muchas gracias")
   break
   