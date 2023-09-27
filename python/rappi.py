print ("**************************")
print ("sistema vacaional de rappi")
print ("**************************")

nombre = input("Por favor introduzca el nombre del empleado\n")
clave = int(input("Por favor introduzca la clave de su departamento, la clave de su departamento es el numero de su departamento:\n 1)Atencion al cliente\n 2)Logistica\n 3)Gerencia\n "))
antiguedad = float(input("Por favor introduzca su antiguedad en el departamento\n"))

if (clave == 1):
    if antiguedad == 1 and antiguedad < 2:
        print("el empleado ", nombre, "tiene derecho a 6 dias de vacaciones.")
    elif antiguedad >= 2 and antiguedad <= 6:
         print("el empleado ", nombre, "tiene derecho a 14 dias de vacaciones.")
    elif antiguedad >= 6:
        print("El empleado ", nombre, "tiene derecho a 20 dias de vacaciones.")
    else: 
        print("El empleado aun no tiene la antiguedad suficiente como para reclamar vacaciones.")
elif (clave == 2):
    if antiguedad == 1 and antiguedad < 2:
        print("El empleado ", nombre, "tiene derecho a 7 dias de vacaciones")
    elif antiguedad >=2 and antiguedad <= 6:
         print("El empleado ", nombre, "tiene derecho a 15 dias de vacaciones")
    elif antiguedad >= 6:
         print("El empleado", nombre, "tiene derecho a 22 dias de vacaciones")
    else: 
         print("El empleado aun no tiene la antiguedad suficiente como para reclamar vacaciones.")
elif (clave == 3):
    if antiguedad == 2 and antiguedad < 2:
        print ("El empleado ", nombre, "tiene derecho a 10 dias de vacaciones")
    elif antiguedad >=2 and antiguedad <= 6:
        print("El empleado ", nombre, "tiene derecho a 20 dias de vacaciones.")
    elif antiguedad >= 6:
        print("El empleado ", nombre, "tiene derecho a 30 dias de vacaciones.")
    else: 
         print("El empleado no tiene antiguedad suficiente en la empresa para poder reclamar vacaciones.")
else: print("Clave no reconocida por el sistema")