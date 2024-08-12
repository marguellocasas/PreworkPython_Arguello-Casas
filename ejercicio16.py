# Definimos la lista
lista = [1, 2, 3, 4, 5, 6, 7]
par = 0
impar = 0

# Definimos la función que cuenta cuántos números son pares e impares
def funcionCuantosParesImparesHay(numero):


  for item in numero:
    if item % 2 == 0:
      par +=1
    else:
      impar +=1

      return par, impar
    

funcionCuantosParesImparesHay(lista)

print(f"el numero de pares es: '{par}'el numero de impares es: '{impar}'")