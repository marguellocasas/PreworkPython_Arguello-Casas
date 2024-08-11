es_primo = float(input("ingrese el numero:"))

def saberSiesprimo(numero):
  if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos
  elif numero == 2:
        return True  # El 2 es el único número primo par
  elif numero % 2 == 0:
        return False  # Los números pares mayores que 2 no son primos

    # Verifica los posibles divisores desde 3 hasta la raíz cuadrada del número
  for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False  # Si encuentra un divisor, no es primo

  return True  # Si no encuentra divisores, es primo

if saberSiesprimo(es_primo) == True:
  print("este numero es primo")
else:
  print("este numero no es primo")




