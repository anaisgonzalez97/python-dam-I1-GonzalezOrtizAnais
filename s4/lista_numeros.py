# Pedir los números
entrada_usuario = input("Dime números separados por comas: ")

# 1. DIVIDIR la entrada usando las comas
# Ejemplo: "5, 3, 7" → ['5', ' 3', ' 7']
lista_texto = entrada_usuario.split(',')

# 2. LIMPIAR espacios en blanco
# Ejemplo: ['5', ' 3', ' 7'] → ['5', '3', '7']
lista_limpia = []
for texto in lista_texto:
    texto_limpio = texto.strip()  # quita espacios
    lista_limpia.append(texto_limpio)

# 3. CONVERTIR a números decimales
# Ejemplo: ['5', '3', '7'] → [5.0, 3.0, 7.0]
numeros = []
for texto in lista_limpia:
    numero = float(texto)  # convierte texto a número
    numeros.append(numero)

# 4. CALCULAR resultados
suma_total = sum(numeros)
promedio = suma_total / len(numeros) #Cuenta cuántos elementos hay en una lista
numero_mas_grande = max(numeros)

# 5. BUSCAR repetidos
repetidos = {}
for num in numeros:
    if numeros.count(num) > 1:  # si aparece más de una vez
        repetidos[num] = numeros.count(num)

# 6. MOSTRAR resultados
print("\n--- RESULTADOS ---")
print(f"Números: {numeros}")
print(f"Suma: {suma_total}")
print(f"Promedio: {promedio}")
print(f"Número más grande: {numero_mas_grande}")

if repetidos:
    print("Números repetidos:")
    for num, veces in repetidos.items(): #items = elementos de
        print(f"  El {num} aparece {veces} veces")
else:
    print("No hay números repetidos")