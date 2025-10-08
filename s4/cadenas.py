"""
CONTADOR DE CARACTERES
Cuenta vocales, consonantes, mayúsculas y total de caracteres
"""

# Pedir una palabra o frase al usuario
texto = input("Escribe una palabra o frase: ")

# Inicializar contadores en cero
total_caracteres = 0
vocales = 0
consonantes = 0
mayusculas = 0

# Definir qué letras son vocales (incluyendo mayúsculas y minúsculas)
vocales_lista = "aeiouáéíóúAEIOUÁÉÍÓÚ"

# Recorrer cada carácter del texto
for letra in texto:
    # Solo contar letras (no espacios, signos, números, etc.)
    if letra.isalpha():  # isalpha() verifica si es una letra
        total_caracteres += 1
        
        # Contar mayúsculas
        if letra.isupper():
            mayusculas += 1
        
        # Contar vocales y consonantes
        if letra in vocales_lista:
            vocales += 1
        else:
            consonantes += 1

# Mostrar los resultados
print("\n--- RESULTADOS ---")
print(f"Texto analizado: '{texto}'")
print(f"Total de letras: {total_caracteres}")
print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")
print(f"Mayúsculas: {mayusculas}")

