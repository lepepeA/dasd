numero1 = input("introduce el primero numero: ")
numero2 = input("introduce el segundo numero: ")
numero3 = input("introduce el tercer numero: ")

if numero3 < numero2 < numero1:
    print("el numero", numero1, "es el mayor")
elif numero3 < numero1 < numero2:
    print("el numero", numero2, "es el mayor")
elif numero1 < numero2 < numero3:
    print("el numero", numero3, "es el mayor")
elif numero1 < numero3 < numero2:
    print("el numero", numero2, "es el mayor")
elif numero2 < numero3 < numero1:
    print("el numero", numero1, "es el mayor")
elif numero2 < numero1 < numero3:
    print("el numero", numero3, "es el mayor")
