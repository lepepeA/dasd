# Crear una lista de números
lista_num = [1, 2, 3, 4, 5]

# Acceder a elementos de la lista
primer_numero = lista_num[0]  # El primer elemento (índice 0) es 1
segundo_numero = lista_num[1]  # El segundo elemento (índice 1) es 2

# Modificar elementos de la lista
lista_num[3] = 10  # Cambiar el cuarto elemento a 10

# Agregar elementos a la lista
lista_num.append(6)  # Agregar el número 6 al final de la lista

# Longitud de la lista
longitud = len(lista_num)  # Esto dará como resultado 6

# Iterar a través de la lista
for numero in lista_num:
    print(numero)
