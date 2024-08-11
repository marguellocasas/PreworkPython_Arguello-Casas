palabra = input("ingrese la oracion deseada")

def contador_palabras(palabra):
  palabra = palabra.split()
  return len(palabra)

print(f" la cantidad de palabras en esta oracion es: '{contador_palabras(palabra)}'")
