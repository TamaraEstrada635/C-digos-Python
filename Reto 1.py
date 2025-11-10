# Reto 1 
ingrese_dato = str(input("\nIngrese su nombre: "))
print("Usuario: ", ingrese_dato.capitalize())

ingrese_numero = int(input("Ingrese su edad: "))
if ingrese_numero < 100:
 print ("Edad del usuario: ", ingrese_numero)
else :
 print("Edad inválida. Debe ser menor a 100.")

frase_fav = str(input("Ingrese la frase favorita del usuario: "))
print("Frase favorita del usuario: ", frase_fav.capitalize())

cant_dinero = float(input("Ingrese la cantidad de dinero del usuario: "))
print("La cantidad de dinero del usuario es: ", cant_dinero)

datos_usuario = input("¿Desea saber los datos del usuario ingresado?: ")
if datos_usuario.lower() == "si":
 print("\nDatos del usuario ingresado: ", ingrese_dato.capitalize(), ingrese_numero, frase_fav.capitalize(), cant_dinero, sep = "\n")