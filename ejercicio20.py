lista_usuario =(input("ingrese la lista de numeros que quiere sumar"))

lista_numeros = lista_usuario.split(',')

lista =[]

for item in lista_numeros:
  numero =float(item)
  lista.append(numero)


  

def sum_lista(lista_numeros):
  suma = sum(lista_numeros)
  return suma


print(f"la suma de todos los numeros es: '{sum_lista(lista)}'")


