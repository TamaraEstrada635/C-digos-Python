# Reto del día 4
lista_1 = ["leche","huevo","pan"]
print("Lista inicial")
print(lista_1)

# Opciones que tenemos
print("\nOpciones que puedes tomar: ")
print("Añadir")
print("Eliminar")
print("Revisar")

# Desicion de usuario
opcion = input("Desicion a tomar: ")

# Ejecucion de opciones 
if opcion.lower() == "añadir" :
  objeto = str(input("Articulo que desea añadir: "))
  lista_1.append(objeto)
  print ("Articulo añadido correctamente")
  print("Lista modificada", lista_1)

elif opcion.lower() == "eliminar" :
  objeto = str(input("Articulo que desea eliminar: "))
  lista_1.remove(objeto)
  print ("Articulo eliminado correctamente")
  print("Lista modificada:", lista_1)

elif opcion.lower() == "revisar" : 
  print ("Revision de lista")
  print("Lista:", lista_1)
 

