# Reto del día 3
nombre = input("Ingresa tu nombre: ")
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))

# Videojuegos
vi_juegos = input("Ingresa tus tres videojuegos favoritos (separados por comas): ")

#Lista 
perfil = [nombre] #solo nombre del usuario

#Calculo de edad
edad = 2025 - anio_nacimiento
perfil.append(edad)

juegos = vi_juegos.split(",")
perfil.extend(juegos) #añadir juegos a la lista perfil
perfil.insert(0, True)  #agregar True al inicio
juego_favorito = perfil.pop(3)

# comprobaciones
es_mayor_de_edad = edad >= 18
nombre_largo = len(nombre) > 10
es_gamer_retro = vi_juegos == "pacman" 

print("El perfil del usuario es:", perfil)
print("Su juego favorito del usuario es:", juego_favorito)
print("¿El usuario es mayor de edad?:",es_mayor_de_edad)
print("¿El usuario tiene un nombre largo?:", nombre_largo)
print("¿El usuario es gamer retro?:", es_gamer_retro) 
