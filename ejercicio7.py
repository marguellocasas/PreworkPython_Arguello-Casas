def funcionparasumarnumeros(variable1, variable2):
    return variable1 + variable2

def funcionpararestarnumeros(variable1, variable2):
    return variable1 - variable2

def funcionparadividirnumeros(variable1, variable2):
    if variable2 != 0:
        return variable1 / variable2
    else:
        return "Error: División por cero no permitida"

def funcionparamultiplicarnumeros(variable1, variable2):
    return variable1 * variable2

def queelclientedigaquequierehacer():
    print("Seleccione 1 si desea sumar")
    print("Seleccione 2 si desea restar")
    print("Seleccione 3 si desea dividir")
    print("Seleccione 4 si desea multiplicar")

    while True:
        # El siguiente código se ejecuta siempre y cuando la condición sea verdadera
        seleccion = input("Seleccione una de las opciones (1, 2, 3, 4): ")

        if seleccion in ['1', '2', '3', '4']:
            numero1 = float(input("Deme el primer valor: "))
            numero2 = float(input("Deme el segundo valor: "))

            if seleccion == "1":
                # Sumar
                print(f"El total de la suma es '{funcionparasumarnumeros(numero1, numero2)}' ")
            elif seleccion == "2":
                # Restar
                print(f"El total de la resta es '{funcionpararestarnumeros(numero1, numero2)}'")
            elif seleccion == "3":
                # Dividir
                print(f"El total de la división es '{funcionparadividirnumeros(numero1, numero2)}'")
            elif seleccion == "4":
                # Multiplicar
                print(f"El total de la multiplicación es '{funcionparamultiplicarnumeros(numero1, numero2)}'")
            break
        else:
            print("Selección no válida")

# Ejecutar la función principal
queelclientedigaquequierehacer()
