#Pedir 3 números
#Mostrar suma, media y mayor
#Adaptación libre
#Guardar en S3_prompts.txt → prompt + explicación + adaptación

print("=== CALCULADORA DE 3 NÚMEROS ===")
print("Vamos a calcular la suma, media y el número mayor")

# Pedir los 3 números al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

# Calcular la suma
suma = numero1 + numero2 + numero3

# Calcular la media (promedio)
media = suma / 3

# Encontrar el número mayor
mayor = numero1
if numero2 > mayor:
    mayor = numero2
if numero3 > mayor:
    mayor = numero3

# Mostrar los resultados
print("\n--- RESULTADOS ---")
print(f"Los números ingresados son: {numero1}, {numero2}, {numero3}")
print(f"Suma: {suma}")
print(f"Media: {media}")
print(f"Número mayor: {mayor}")