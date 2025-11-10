# Reto del día 7

print("-"*10,"Datos de estudiantes","-"*10)
datos_diccionario = {}
nuevo_estudiante = {
    "ID":{
        "nombre":"",
        "materia":"",
        "calificaciones":[],            
        }
    }
materias_validas = ("Resistencia de los materiales", "Control clasico", "Programacion avanzada")

while True:
    print("Que accion desea realizar")
    print("* Registrar estudiante")
    print("* Buscar estudiante")
    print("* Calcular promedio")
    print("* Ver todos los estudiantes")
    print("* Salir")
    accion = input("Ingrese la accion a realizar: ").lower()

    if accion == "salir":
        print("Saliendo del programa")
        break

    elif accion == "registrar estudiante":

        while True:
            id_estudiante = input("Ingrese el ID del estudiante: ")
            if id_estudiante in datos_diccionario:
                print("El ID del estudiante ya existe. Ingrese un ID diferente.")
            else:
                break
        

        while True:
            nombre = input("Ingrese el nombre del estudiante: ")
            if nombre.strip() == "":
                print("El nombre no puede estar vacío. Ingrese un nombre válido.")
            else:
                break
        

        while True:
            materia = input("Ingrese la materia del estudiante: ")
            if materia not in materias_validas:
                print("Materia no valida. Las materias validas son:")
                for materia_valida in materias_validas:
                    print(f"- {materia_valida}")
            else:
                break
        

        while True:
            calificaciones = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones_lista = []
            calificaciones_validas = True
            
            for calificacion in calificaciones.split(","):
                try:
                    calif_float = float(calificacion)
                    calificaciones_lista.append(calif_float)
                except ValueError:
                    print(f"Error: '{calificacion}' no es un número válido. Intente de nuevo.")
                    calificaciones_validas = False
                    break
            
            if calificaciones_validas and len(calificaciones_lista) > 0:
                break
            elif len(calificaciones_lista) == 0:
                print("Debe ingresar al menos una calificación válida.")

        datos_diccionario[id_estudiante] = {
            "nombre": nombre,
            "materia": materia,
            "calificaciones": calificaciones_lista
        }
        print(f"Estudiante {nombre} registrado exitosamente.")
    
    elif accion == "buscar estudiante":
        while True:
            id_estudiante = input("Ingrese el ID del estudiante: ")
            if id_estudiante in datos_diccionario:
                estudiante = datos_diccionario[id_estudiante]
                print(f"Nombre: {estudiante['nombre']}")
                print(f"Materia: {estudiante['materia']}")
                print(f"Calificaciones: {estudiante['calificaciones']}")
                break
            else:
                print("Estudiante no encontrado. Ingrese un ID válido.")

    elif accion == "calcular promedio":
        
        while True:
            id_estudiante = input("Ingrese el ID del estudiante: ")
            if id_estudiante in datos_diccionario:
                estudiante = datos_diccionario[id_estudiante]
                calificaciones = estudiante["calificaciones"]
                if len(calificaciones) == 0:
                    print("El estudiante no tiene calificaciones registradas.")
                else:
                    promedio = sum(calificaciones) / len(calificaciones)
                    print(f"El promedio de calificaciones de {estudiante['nombre']} es: {promedio}")
                break
            else:
                print("Estudiante no encontrado. Ingrese un ID válido.")
    
    elif accion == "ver todos los estudiantes":
        if len(datos_diccionario) == 0:
            print("No hay estudiantes registrados.")
        else:
            for id_estudiante, datos in datos_diccionario.items():
                print(f"ID: {id_estudiante}")
                print(f"Nombre: {datos['nombre']}")
                print(f"Materia: {datos['materia']}")
                print(f"Calificaciones: {datos['calificaciones']}")
                print("-" * 30)
    else:
        print("Accion no valida. Intente de nuevo.")
