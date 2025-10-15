"""
Programa: Análisis de Calificaciones
Descripción: Analiza una lista de notas y genera un boletín estadístico
"""

def analizar_calificaciones():
    """
    Función principal que solicita calificaciones y muestra un resumen estadístico
    """
    
    
    print("ANALIZADOR DE CALIFICACIONES")
 
    
    # Solicitar lista de calificaciones
    while True:
        try:
            # Pedir las calificaciones como texto separado por comas
            entrada = input("Ingresa las calificaciones separadas por comas: ")
            
            # Convertir a string y limpiar espacios en blanco
            lista_texto = [nota.strip() for nota in entrada.split(",")]
            
            # Convertir a números decimales (float)
            calificaciones = []
            for nota_texto in lista_texto:
                nota = float(nota_texto)  # Convierte texto a número
                if nota < 0 or nota > 10:
                    print("Error: Las notas deben estar entre 0 y 10")
                    break
                calificaciones.append(nota) #añade nota a la lista
            else:
                # Si no hubo break, todas las notas son válidas
                if calificaciones:  # Verificar que la lista no esté vacía
                    break
                
        except ValueError:
            print("Error: Asegúrate de ingresar solo números (ej: 7.5, 8, 6)")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    # ========== CÁLCULOS ESTADÍSTICOS ==========
    
    # Número total de notas
    total_notas = len(calificaciones) #len devuelve el numero de elementos que hay en una lista
    
    # Media (promedio) redondeada a 2 decimales
    media = round(sum(calificaciones) / total_notas, 2)
    
    # Nota mínima y máxima
    nota_minima = min(calificaciones)
    nota_maxima = max(calificaciones)
    
    # Porcentaje de aprobados (>=5) y sobresalientes (>=9)
    aprobados = [nota for nota in calificaciones if nota >= 5] #Para cada nota en calificaciones, inclúyela en la nueva lista aprobados SOLO SI la nota es mayor o igual a 5
    sobresalientes = [nota for nota in calificaciones if nota >= 9] #Para cada nota en calificaciones, inclúyela en la nueva lista aprobados SOLO SI la nota es mayor o igual a 9
    
    porcentaje_aprobados = round((len(aprobados) / total_notas) * 100, 2)
    porcentaje_sobresalientes = round((len(sobresalientes) / total_notas) * 100, 2)
    
    # Moda (nota más repetida)
    frecuencia = {} #Crear diccionario vacío
    for nota in calificaciones:
        frecuencia[nota] = frecuencia.get(nota, 0) + 1
        #busca la nota en el diccionario Si la nota EXISTE: devuelve su valor actual; Si la nota NO EXISTE: devuelve 0. Suma 1 al valor obtenido y guarda el nuevo valor en el diccionario
    
    # Encontrar la máxima frecuencia
    max_frecuencia = max(frecuencia.values())
    
    # Encontrar todas las notas con esa frecuencia (puede haber empate)
    modas = [nota for nota, freq in frecuencia.items() if freq == max_frecuencia]
    
    # ========== MOSTRAR RESULTADOS ==========
    
    print("\n" + "RESUMEN ESTADÍSTICO")
    print("=" * 30)
    
    # Información básica
    print(f"• Total de notas: {total_notas}")
    print(f"• Nota media: {media}")
    print(f"• Nota mínima: {nota_minima}")
    print(f"• Nota máxima: {nota_maxima}")
    
    # Porcentajes
    print(f"• Aprobados (≥5): {porcentaje_aprobados}%")
    print(f"• Sobresalientes (≥9): {porcentaje_sobresalientes}%")
    
    # Moda
    if len(modas) == 1: #si hay una moda
        print(f"• Moda (nota más frecuente): {modas[0]} (aparece {max_frecuencia} veces)")
    else: #si hay mas de una...
        print(f"• Modas (notas más frecuentes): {', '.join(map(str, modas))} (aparecen {max_frecuencia} veces cada una)")
        #Convierte cada número a texto (string), une todos los elementos con comas
        #map(str, modas): "Convierte todos estos números en textos"
        # join(): "Une todos estos textos poniendo comas entre ellos"
    
    # ========== MENSAJE FINAL ==========
    
    print("\n" + " DIAGNÓSTICO DEL GRUPO")
    print("=" * 25)
    
    if media >= 8:
        print("¡NIVEL EXCELENTE!")
        print("   El grupo demuestra un dominio sobresaliente")
    elif media >= 5:
        print("NIVEL MEDIO")
        print("   El grupo tiene un rendimiento adecuado")
    else:
        print("NECESITA REFUERZO")
        print("   Se recomienda apoyo adicional para el grupo")
    
    print("\n" + "=" * 50)

# ========== EJECUTAR EL PROGRAMA ==========
if __name__ == "__main__": # Solo haz estos pasos si este es el papel principal
    analizar_calificaciones()