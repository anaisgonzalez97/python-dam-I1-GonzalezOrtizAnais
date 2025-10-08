# DETECTOR SIMPLE DE NÚMEROS PRIMOS

numero = int(input("Escribe un número: "))

if numero <= 1:
    print("NO es primo") #Si el número es 1, 0, o negativo NO es primo.
else:
    primo = True #si es +2 puede ser primo
    for i in range(2, numero): #rango entre 2 y el número dicho por el usuario
        if numero % i == 0: #¿El número se puede dividir exactamente por i? es decir, el resto es 0
            primo = False #si es asi, no es primo
            break
    
    if primo:
        print("SÍ es primo")
    else:
        print("NO es primo")