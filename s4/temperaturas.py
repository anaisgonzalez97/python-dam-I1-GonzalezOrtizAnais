"""
CONVERSOR DE TEMPERATURAS
Convierte grados Celsius a Fahrenheit o Kelvin
"""

# Mostrar mensaje de bienvenida
print("=== CONVERSOR DE TEMPERATURAS ===")
print("Este programa convierte Celsius a Fahrenheit o Kelvin")

# Pedir la temperatura al usuario
celsius = float(input("¿Qué temperatura en Celsius quieres convertir? "))

# Mostrar opciones disponibles
print("\n¿A qué unidad quieres convertir?")
print("1 - Fahrenheit")
print("2 - Kelvin")

# Pedir la opción al usuario
opcion = input("Elige 1 o 2: ")

# Realizar la conversión según la opción elegida
if opcion == "1":
    # Fórmula: Fahrenheit = (Celsius × 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    print(f"\n{celsius}°C = {fahrenheit}°F")
    
elif opcion == "2":
    # Fórmula: Kelvin = Celsius + 273.15
    kelvin = celsius + 273.15
    print(f"\n{celsius}°C = {kelvin}K")
    
else:
    print("\n Opción no válida. Por favor elige 1 o 2.")

# Mensaje final
print("\n¡Gracias por usar el conversor!")