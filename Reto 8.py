# Reto del día 8

COMPONENTES_PERMITIDOS = ("Motor", "Sensor", "Batería", "Chasis")
inventario_componentes = {}

def solicitar_serial():
    while True:
        try:
            serial = input("Ingrese el Número de Serie (S/N): ").strip()
            if not serial:
                raise ValueError("El serial no puede estar vacío")
            if not serial.replace("-", "").replace("_", "").isalnum():
                raise ValueError("El serial debe ser alfanumérico")
            return serial
        except ValueError as error:
            print(f"Error: {error}")

def solicitar_categoria():
    while True:
        try:
            print(f"Categorías permitidas: {', '.join(COMPONENTES_PERMITIDOS)}")
            categoria = input("Ingrese la categoría del componente: ").strip().capitalize()
            if categoria not in COMPONENTES_PERMITIDOS:
                raise ValueError(f"Categoría inválida")
            return categoria
        except ValueError as error:
            print(f"Error: {error}")

def solicitar_valor_prueba(numero):
    while True:
        try:
            valor = input(f"Ingrese el valor de prueba {numero} (0-100): ")
            valor_float = float(valor)
            if valor_float < 0 or valor_float > 100:
                raise ValueError("El valor debe estar entre 0 y 100")
            return valor_float
        except ValueError:
            print("Error: Ingrese un número válido")

def obtener_tres_valores():
    try:
        valores = []
        for n in range(1, 4):
            valores.append(solicitar_valor_prueba(n))
        return valores
    except Exception as error:
        print(f"Error obteniendo valores: {error}")
        return None

def agregar_componente():
    print("\n--- AGREGAR COMPONENTE ---")
    try:
        serial = solicitar_serial()
        if serial in inventario_componentes:
            raise KeyError(f"Serial {serial} ya existe")
        categoria = solicitar_categoria()
        valores = obtener_tres_valores()
        if valores is None or len(valores) != 3:
            raise ValueError("Error en los valores de prueba")
        inventario_componentes[serial] = {
            "categoria": categoria,
            "valores_prueba": valores,
            "status": "Pendiente"
        }
        print(f"✓ Componente {serial} agregado")
    except KeyError as error:
        print(f"Error: {error}")
    except ValueError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Error inesperado: {error}")

def encontrar_componente():
    print("\n--- ENCONTRAR COMPONENTE ---")
    try:
        if not inventario_componentes:
            raise ValueError("Inventario vacío")
        serial = solicitar_serial()
        if serial not in inventario_componentes:
            raise KeyError(f"Serial {serial} no encontrado")
        componente = inventario_componentes[serial]
        print(f"\nInformación del componente {serial}:")
        print(f"  Categoría: {componente['categoria']}")
        print(f"  Valores de prueba: {componente['valores_prueba']}")
        print(f"  Status: {componente['status']}")
    except ValueError as error:
        print(f"Info: {error}")
    except KeyError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Error inesperado: {error}")

def analizar_componente():
    print("\n--- ANALIZAR COMPONENTE ---")
    try:
        if not inventario_componentes:
            raise ValueError("Inventario vacío")
        serial = solicitar_serial()
        if serial not in inventario_componentes:
            raise KeyError(f"Serial {serial} no encontrado")
        componente = inventario_componentes[serial]
        valores = componente["valores_prueba"]
        if not valores or len(valores) != 3:
            raise ValueError("Valores de prueba inválidos")
        promedio = sum(valores) / len(valores)
        if promedio >= 90.0:
            nuevo_status = "Aprobado"
        else:
            nuevo_status = "Rechazado"
        componente["status"] = nuevo_status
        print(f"✓ Componente {serial} analizado:")
        print(f"  Valores: {valores}")
        print(f"  Promedio: {promedio:.2f}")
        print(f"  Status: {nuevo_status}")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Error inesperado: {error}")

def mostrar_inventario():
    print("\n--- INVENTARIO COMPLETO ---")
    try:
        if not inventario_componentes:
            raise ValueError("Inventario vacío")
        for serial, componente in inventario_componentes.items():
            print(f"Serial: {serial} - Categoría: {componente['categoria']} - Status: {componente['status']}")
    except ValueError as error:
        print(f"Info: {error}")
    except Exception as error:
        print(f"Error inesperado: {error}")

def contar_recursivo(lista_componentes, categoria_buscar, posicion=0):
    try:
        if posicion >= len(lista_componentes):
            return 0
        componente_actual = lista_componentes[posicion]
        if not isinstance(componente_actual, dict) or "categoria" not in componente_actual:
            raise ValueError("Estructura de datos inválida")
        if componente_actual["categoria"] == categoria_buscar:
            return 1 + contar_recursivo(lista_componentes, categoria_buscar, posicion + 1)
        else:
            return contar_recursivo(lista_componentes, categoria_buscar, posicion + 1)
    except RecursionError:
        print("Error: Demasiadas recursiones")
        return 0
    except Exception as error:
        print(f"Error en conteo: {error}")
        return 0

def ejecutar_conteo():
    print("\n--- CONTEO POR CATEGORÍA ---")
    try:
        if not inventario_componentes:
            raise ValueError("Inventario vacío")
        categoria = solicitar_categoria()
        lista_componentes = list(inventario_componentes.values())
        if not lista_componentes:
            raise ValueError("Sin datos para procesar")
        total = contar_recursivo(lista_componentes, categoria)
        print(f"✓ Total de componentes de categoría '{categoria}': {total}")
    except ValueError as error:
        print(f"Info: {error}")
    except Exception as error:
        print(f"Error inesperado: {error}")

def terminar_programa():
    try:
        print("\nCerrando sistema...")
        exit()
    except Exception as error:
        print(f"Error al terminar: {error}")

def presentar_menu():
    try:
        print("\n       SISTEMA DE GESTIÓN DE COMPONENTES")
        print("1. agregar")
        print("2. encontrar")
        print("3. analizar")
        print("4. mostrar")
        print("5. contar")
        print("6. terminar")
        
    except Exception as error:
        print(f"Error mostrando menú: {error}")

def main(): #Ejecucuion principal
    try:
        print("Bienvenido al Sistema de Gestión de Componentes")
        comandos = {
            "agregar": agregar_componente,
            "encontrar": encontrar_componente,
            "analizar": analizar_componente,
            "mostrar": mostrar_inventario,
            "contar": ejecutar_conteo,
            "terminar": terminar_programa
        }
        while True:
            try:
                presentar_menu()
                comando = input("Seleccione comando: ").strip().lower()
                if comando in comandos:
                    comandos[comando]()
                else:
                    raise ValueError("Comando no válido")
            except ValueError as error:
                print(f"Error: {error}")
            except KeyboardInterrupt:
                print("\nInterrupción detectada")
            except Exception as error:
                print(f"Error inesperado: {error}")
    except Exception as error:
        print(f"Error crítico: {error}")
    finally:
        print("Sistema finalizado")

main()