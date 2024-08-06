def calcular_IMC (peso, altura):
  return peso / altura

variable1 = float(input("introduce tu peso en kilogramos "))
variable2 = float(input("introduce tu altura en centimetros "))

print(f"tu IMC es '{calcular_IMC(variable1, variable2)}'")