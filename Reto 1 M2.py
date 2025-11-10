#Reto del día 1 M2
class Componente:
    #Constructor
    def __init__(self, tipo_componente, numero_serie, costo):
     print(f"Construyendo un componente de tipo {tipo_componente} de serie {numero_serie} y costo {costo}...")
    
    #Atributos, para hacerlos mutables
     self.numero_serie = numero_serie
     self.tipo = tipo_componente
     self.costo = costo

    #Atributos por defecto
     self.historial_revisiones = []
     self.esta_activo = True

#Creando objetos
c1 = Componente("motor", "MTR-1001", "550.75")
c2 = Componente("sensor", "SNR-2050", "80.20")

print("\n---Objetos creados---")
print(f"Es un {c1.tipo} con S/N {c1.numero_serie} y costo {c1.costo}")
print(f"Es un {c2.tipo} con S/N {c2.numero_serie} y costo {c2.costo}")

#Mofificando atributos
c1.historial_revisiones.append("2025-10-25")
c1.historial_revisiones.append("2025-11-24")
print(f"Historial de revisiones del {c1.tipo} S/N {c1.numero_serie}: {c1.historial_revisiones}")
c2.esta_activo = False
print(f"El {c1.tipo} está activo? = {c2.esta_activo}")

#Repote de c1
print("\n---Reporte del Componente 1---")
print(f"Tipo: {c1.tipo}")
print(f"Número de Serie: {c1.numero_serie}")
print(f"Costo: {c1.costo}")
print(f"Historial de Revisiones: {c1.historial_revisiones}")
print(f"Estado activo: {c1.esta_activo}")

#Reporte de c2
print("\n---Reporte del Componente 2---")
print(f"Tipo: {c2.tipo}")
print(f"Número de Serie: {c2.numero_serie}")
print(f"Costo: {c2.costo}")
print(f"Historial de Revisiones: {c2.historial_revisiones}")
print(f"Estado activo: {c2.esta_activo}")
