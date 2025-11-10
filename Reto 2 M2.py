#Reto del día 2 M2
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        print(f"Construyendo un vehículo de marca {marca}, modelo {modelo}, año {anio}...")
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self._encendido = False  # Atributo protegido
        self._kilometraje = 0    #Protegido

    def arrancar(self):
        print ("Intentando arrancar el vehículo...")
        if not self._encendido:
            self._encendido = True
            print(f"El vehículo {self.marca} {self.modelo} ha arrancado.")
        else:
            print(f"El vehículo ya estaba en marcha.")
            
    def apagar(self):
        print ("Intentando apagar el vehículo...")
        if self._encendido:
            self._encendido = False
            print(f"El vehículo {self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"El vehículo ya estaba apagado.")

    def get_kilometraje(self):
        return self._kilometraje
    
    def mostrar_info_base(self):
        print(f"\nInformación base del vehículo:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        print(f"Construyendo un coche con {num_puertas} puertas...")
        self.num_puertas = num_puertas

    def conducir(self,km):
        if self._encendido:
           self._kilometraje += km
           print(f"Conduciendo {km} km...")
        else:
           print("Error: El coche debe estar arrancado para conducir")

class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, capacidad_carga_kg):
        super().__init__(marca, modelo, anio)
        print(f"Construyendo un camión con capacidad de carga {capacidad_carga_kg} kg...")
        self.capacidad_carga_kg = capacidad_carga_kg
        self.__carga_actual_kg = 0.0

    def cargar(self, kilos):
        if self.__carga_actual_kg + kilos <= self.capacidad_carga_kg:
            self.__carga_actual_kg += kilos
            print(f"Carga exitosa. Carga actual: {self.__carga_actual_kg} kg")
        else:
            print("Error: Sobrecarga..")

    def descarga(self, kilos):
        if kilos <= self.__carga_actual_kg:
            self.__carga_actual_kg -= kilos
            print(f"Descarga exitosa. Carga actual: {self.__carga_actual_kg} kg")
        else:
            print("Error: No se puede descargar esa cantidad.")
        
    def get_carga_actual(self):
        return self.__carga_actual_kg
    
    #Demostraciones
print("\n---Creando un coche---")
mi_coche = Coche("Mustang", "Classic", 2020, 4)
mi_camion = Camion("Volvo", "FH16", 2019, 5000)

print("\n---Prueba del coche---")
mi_coche.conducir(100) #Falla
mi_coche.arrancar()
mi_coche.conducir(100) #Funciona
mi_coche.apagar()
print(f"Su kilometraje fue: {mi_coche.get_kilometraje()} km")

print(f"\n---Prueba del camión---")
mi_camion.cargar(3000) 
mi_camion.cargar(3000) #Sobrecarga
mi_camion.descarga(1000)
print(f"Su carga actual es: {mi_camion.get_carga_actual()} kg")
