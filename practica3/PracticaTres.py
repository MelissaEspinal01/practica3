def menu():
    print("A) Ejercicio 1")
    print("B) Ejercicio 2")
    print("C) Ejercicio 3")
    print("D) Salir")

def ejercicio1(numero_mes):
    meses = ( "Enero", "Febrero", "Marzo", "Abril", 
            "Mayo", "Junio", "Julio", "Agosto", 
            "Septiembre", "Octubre", "Noviembre",
            "Diciembre" 
            ) 

    if 1 <= numero_mes <= 12:
        return meses[numero_mes - 1]
    else: 
        return "Número de mes inválido" 
    

def ejercicio2(cadena):
    palabras = cadena.split() 
    return len(palabras) 


def seleccionarOpcion(opcion):
    print("\n")
    opcion = opcion.upper()
    
    if opcion == "A":
        numero = int(input("Ingresa un número entre 1 y 12: ")) 
        nombre_mes = ejercicio1(numero)
        print(nombre_mes)
    elif opcion == "B":
        cadena = input("Escriba una frase: ")
        cantidad_palabras = ejercicio2(cadena) 
        print(f"La frase tiene {cantidad_palabras} palabras.")
    elif opcion == "C":
        print("Aun no esta listo")
    elif opcion == "D":
        print("Gracias por revisar :3")
    else:
        print("Esta opcion no es valida :(")

while True: 
    menu()
    
    opcion = input("Ingresa una opcion A-D: ")
    seleccionarOpcion(opcion)
    
    if opcion.upper() == "D":
        break