# Reto 2
# Calculadora de números

numero = float(input("\nIngrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))
print("\nEl primer numero ingresado es: ", numero)
print("El segundo numero ingresado es: ", numero2)

#Operaciones basicas
print(f"\nSuma (a + b): {numero + numero2}")
print(f"Resta (a - b): {numero - numero2}")
print(f"Multiplicación (a * b): {numero * numero2}")

if numero2 != 0:
    print(f"División (a / b): {numero / numero2}")
else:
    print("División (a / b): No se puede dividir entre cero")

print(f"Módulo 2 de a (a % 2): {numero % 2}")
print(f"Módulo 2 de b (b % 2): {numero2 % 2}")

print(f"\nPotencia cúbica del primer número (a^3): {numero ** 3}")
print(f"Potencia cúbica del segundo termino (b^3): {numero2 ** 3}")

#Sumar al numero ingresado
numero3 = float(input("\nIngrese un numero nuevo: "))
numero3 += 2
print("El valor final es: ", numero3)

numero4 = float(input("Ingrese un numero nuevo: "))
numero4 += 2
print("El valor final es: ", numero4)

print("\nLos valores restando 13 son:")
#Sumar 13 al numero ingresado
numero3 -= 13
print("El valor final es: ", numero3)
numero4 -= 13
print("El valor final es: ", numero4)

# Comparaciones
print("\nComparaciones entre los dos numeros:")
print("Igualdad (a == b): ", numero3 == numero4)
print("Desigualdad (a != b): ", numero3 != numero4)
print("Mayor que (a > b): ", numero3 > numero4)
print("Menor que (a < b): ", numero3 < numero4)

#Tablas de verdad
print("\nTablas de verdad:")
print("AND, OR, NOT")

# --- AND ---
print("\nTABLA DE VERDAD - AND")
A = True; B = True
resultado_and = A and B
print( A, B, "=",resultado_and)

A = True; B = False
resultado_and = A and B
print( A, B, "=",resultado_and)

A = False; B = True
resultado_and = A and B
print( A, B,"=", resultado_and)

A = False; B = False
resultado_and = A and B
print(A, B,"=" ,resultado_and)

# --- OR ---
print("\nTABLA DE VERDAD - OR")
A = True; B = True
resultado_or = A or B
print(A, B, "=", resultado_or)

A = True; B = False
resultado_or = A or B
print(A, B, "=", resultado_or)

A = False; B = True
resultado_or = A or B
print(A, B, "=", resultado_or)

A = False; B = False
resultado_or = A or B
print(A, B, "=", resultado_or)

# --- NOT ---
print("\nTABLA DE VERDAD - NOT")
A = True
resultado_not = not A
print(A, "=", resultado_not)

A = False
resultado_not = not A
print(A, "=", resultado_not)

