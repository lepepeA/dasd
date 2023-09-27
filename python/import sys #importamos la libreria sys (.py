import sys #importamos la libreria sys ( system )

def Agregar():
    num = int (input ("Digite un numero entero: "))
    lista_num.append(num)

def Eliminar():
    lista_num.pop()

def Mostrar():
    print(lista_num[:])

 lista_num = []

    while ( True ) :
        print ("\t\MENU DE ACCIONES PILA\n\n")
        print("1)Agregar\n2)Eliminar\n3)Mostrar\n4)Salir\n")
        op = int(input("Numero de opcion --> "))
        if op == 1:
            Agregar()

        elif op == 2:
            Eliminar()
        
        elif op == 3:
            Mostrar ()
        
        elif op == 4:
            s = input("Presione enter para salir. . . ")
            sys.exit() #usamos sys.exit () para salir del programa
        
        else:
            print("Opcion no valida")
            
