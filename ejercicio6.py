variableTipoSrting = 'oso'

def funcionparasabersiespalindromo(otraVariablequeUsaLaFuncion):
    otraVariablequeUsaLaFuncion = otraVariablequeUsaLaFuncion.lower()
    otraVariablequeUsaLaFuncion = otraVariablequeUsaLaFuncion.replace(" ", "")
    return otraVariablequeUsaLaFuncion == otraVariablequeUsaLaFuncion[::-1]

if funcionparasabersiespalindromo(variableTipoSrting):
    print(f"la palabra '{variableTipoSrting}'es palindromo ")
else:
      print(f"la palabra '{variableTipoSrting}'no es palindromo ") 


