
def convertirDolaresaEuros (USD):
  return USD * 0.85

def convertirEurosaDolares (EUR):
  return EUR / 0.85

#preguntar al cliente que quiere hacer
def quequierehacerelcliente ():
  print("Opción A si quiere convertir USD a EUR")
  print("Opción B si quiere convertir EUR a USD")

Seleccion = input("Seleccione la opción deseada: ")

if Seleccion == "A":
  USD = float(input("cantidad de USD a convertir: ") )
  print(f"total USD'{convertirDolaresaEuros(USD)}'")

elif Seleccion == "B":
  EUR = float(input("cantidad de EUR a convertir: "))
  print(f"total EUR '{convertirEurosaDolares(EUR)}'")

else: 
  print("seleccion no valida")
