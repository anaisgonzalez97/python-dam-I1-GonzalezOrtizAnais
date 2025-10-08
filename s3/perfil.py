#pedir nombre + año de nacimiento, clacular edad, 
# clasificar por tramo (-18, 18 -65, +65)
#manejo de error si no mete número
#comentarios

# Programa para calcular edad y clasificar por tramos etarios
# con manejo de errores para entrada no numérica

def calcular_edad():
    """
    Función principal que solicita nombre y año de nacimiento,
    calcula la edad y clasifica por tramos etarios
    """
    
    # Solicitar nombre del usuario
    nombre = input("Por favor, ingresa tu nombre: ")
    
    # Solicitar año de nacimiento con manejo de errores
    while True:
        try:
            año_nacimiento = int(input("Por favor, ingresa tu año de nacimiento: ")) #input es como println y scanner juntos
            
            # Validar que el año sea razonable (entre 1900 y el año actual)
            año_actual = 2025 
            if año_nacimiento < 1900 or año_nacimiento > año_actual:
                print(f"Error: El año debe estar entre 1900 y {año_actual}") #muestra esto por pantalla
                continue
                
            break  # Salir del bucle si la entrada es válida
            
        except ValueError:
            print("Error: Debes ingresar un número válido para el año de nacimiento")
    
    # Calcular la edad
    edad = año_actual - año_nacimiento
    
    # Clasificar por tramos etarios
    if edad < 18:
        tramo = "Menor de edad (-18)"
    elif 18 <= edad <= 65:
        tramo = "Adulto (18-65)"
    else:
        tramo = "Adulto mayor (+65)"
    
    # Mostrar resultados
    print("\n" + "="*40)
    print(f"Nombre: {nombre}")
    print(f"Año de nacimiento: {año_nacimiento}")
    print(f"Edad: {edad} años")
    print(f"Clasificación: {tramo}")
    print("="*40)

# Ejecutar el programa
if __name__ == "__main__":
    calcular_edad()