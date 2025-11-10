# Reto del día 9

TIPOS_ENTRADA_VALIDOS = ("Observación", "Prueba", "Error", "Mantenimiento")
NOMBRE_ARCHIVO = "laboratorio.txt"


def registrar_entrada():
    print("\n--- Registrar entrada ---")
    print("Tipos permitidos:")
    for i, t in enumerate(TIPOS_ENTRADA_VALIDOS, start=1):
        print(f"{i}. {t}")

    tipo_elegido = None
    while True:
        dato = input("Escribe el tipo a elegir: ").strip()
        if not dato:
            print("No puede estar vacio. Intenta de nuevo.")
            continue

        try:
            num = int(dato)
            if 1 <= num <= len(TIPOS_ENTRADA_VALIDOS):
                tipo_elegido = TIPOS_ENTRADA_VALIDOS[num - 1]
                break
            else:
                print("Número fuera de rango. Intenta de nuevo.")
                continue
        except ValueError:
            texto = dato.lower()
            encontrado = None
            for t in TIPOS_ENTRADA_VALIDOS:
                if texto == t.lower():
                    encontrado = t
                    break
            if encontrado is not None:
                tipo_elegido = encontrado
                break
            else:
                print("Error: ingrese una valor válido.")

    while True:
        descripcion = input("Descripción: ").strip()
        if descripcion:
            break
        else:
            print("Error: la descripción no puede estar vacía.")

    try:
        with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as f:
            f.write(f"TIPO: {tipo_elegido} - DESCRIPCIÓN: {descripcion}\n")
        print("✔ Entrada guardada correctamente.")
    except Exception:
        print("✖ No se pudo guardar la entrada.")


def ver_log():
    print("\n--- Ver log ---")
    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
            contenido = f.read().strip()
        if contenido:
            print("\n==== CONTENIDO DEL LOG ====\n")
            print(contenido)
            print("\n  \n")
        else:
            print("El log está vacío o no se ha creado.")
    except FileNotFoundError:
        print("El log está vacío o no se ha creado.")
    except Exception:
        print("Error: Ocurrió un problema al leer el archivo.")


def main():
    print("Cuaderno de Laboratorio (simple)")
    print("Archivo de datos:", NOMBRE_ARCHIVO)

    while True:
        print("\nOpciones: ")
        print("- Registrar")
        print("- Ver_log")
        print("- Salir")
        opcion = input("\n Elige una opción: ").strip().lower()

        if opcion == "registrar":
            registrar_entrada()
        elif opcion == "ver_log":
            ver_log()
        elif opcion == "salir":
            print("\nCerrando sistema.....")
            print("Sistema finalizado")

            break
        else:
            print("Opción no válida. Intenta de nuevo escribiendo 'registrar', 'ver_log' o 'salir'.")
main()
