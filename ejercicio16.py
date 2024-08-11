lista_numeros = float(input("ingrese los numeros separados por comas"))

def contar_pares_e_impares(lista_numeros):

  pares = 0 
  impares = 0
  for numero in lista_numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
  return pares, impares
print(f"Cantidad de números impares: '{contar_pares_e_impares(lista_numeros)}'")
print(f"Cantidad de números impares: '{contar_pares_e_impares(lista_numeros)}'")

