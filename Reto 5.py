# Reto del día 5
cant_alumnos = int(input("Ingresa la cantidad de alumnos a registrar: "))

nombres_al = []
calificaciones = []

# Recolectar datos
for i in range(cant_alumnos):  # Repite para cada alumno
    nombre = input(f"Ingrese el nombre del alumno: ")
    calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
    nombres_al.append(nombre)
    calificaciones.append(calificacion)

#Listas vacias
aprobados = []
reprobados = []
excelentes = []

#Promedio del grupo
promedio = sum(calificaciones)/ len(calificaciones)

# Clasificacion de alumnos
for i in range(cant_alumnos):
 if calificaciones[i] == 10:
        excelentes.append(nombres_al[i])
 elif calificaciones[i] >= 6:
        aprobados.append(nombres_al[i])
 elif calificaciones[i] < 5:
        reprobados.append(nombres_al[i])

print("Numero total de estudiantes: ", cant_alumnos)
print("El promedio del grupo es: ", promedio)
print("Calificación más baja:", min(calificaciones))
print("Calificación más alta:", max(calificaciones))
print("Lista de excelentes: ", excelentes)
print("Lista de aprobados: ", aprobados)    
print("Lista de reprobados: ", reprobados)
