suma_pares = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        suma_pares += numero
print(f"La suma de todos los números pares del 1 al 100 es: {suma_pares}")