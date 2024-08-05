palabra = 'casa'
vocales = "aeiouAEIOU"
contador_vocales = 0
for letra in palabra:
    if letra in vocales:
        contador_vocales += 1
print(f"El número de vocales en la palabra '{palabra}' es: {contador_vocales}")