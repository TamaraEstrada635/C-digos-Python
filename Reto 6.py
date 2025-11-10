#Reto del día 6

print("-"*10,"Lista de compras","-"*10)
lista_inicial = ["leche", "pan", "huevos"]
print(f"La lista inicial es {lista_inicial}")

while True:
    print("Elige la accion que deseas realizar")
    print("* Añadir")
    print("* Quitar")
    print("* Ver")
    print("* Inspeccionar")
    print("* Salir")
    accion = input("\nIngrese la accion a realizar: ").lower()

    if accion == "salir":
        print("Saliendo de la lista de compras")
        break

    elif accion == "añadir":
        producto = input("Que articulo quieres añadir: ").lower()
        if producto in lista_inicial:
            print(f"El articulo '{producto}' ya está en la lista")
            continue
        elif producto == "":
            print("Error: No se puede añadir un artículo vacío")
            continue
        else:
            lista_inicial.append(producto)
            print(f"Objeto añadido, nueva lista {lista_inicial}")

    elif accion == "quitar":
        try:
            eliminado = input("Que articulo quieres eliminar: ").lower()
            lista_inicial.remove(eliminado)
            print(f"Objeto eliminado, nueva lista {lista_inicial}")
        except ValueError:
            print(f"Error: El artículo '{eliminado}' no está en la lista")

    elif accion == "ver": 
        if len(lista_inicial) == 0:
            print("La lista está vacía")
        else:
            lista_inicial.sort()
            print(f"La lista actual es: {lista_inicial}")

    elif accion == "inspeccionar": 
        try:
            indice = int(input("Que numero de articulo quieres inspeccionar? (empezando desde 0): "))
            print(f"El articulo en la posicion {indice} es: {lista_inicial[indice]}")
        except ValueError:
            print("Error: Debes ingresar un número válido")
        except IndexError:
            print(f"Error: La posición {indice} no existe. La lista tiene {len(lista_inicial)} elementos.")

    else:
        print("Accion no reconocida")