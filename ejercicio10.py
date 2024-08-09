def determinardiadesemana(numdedia):

  if numdedia == 1:
    return "lunes"
  elif numdedia == 2:
    return "martes"
  elif numdedia == 3:
    return "miercoles"
  elif numdedia == 4:
    return "jueves"
  elif numdedia == 5:
    return "viernes"
  elif numdedia == 6:
    return "sabado"
  elif numdedia == 7:
    return "domingo"
  else:
   return "numero invalido"
  
vardia = float(input("introduzca un valor del 1 al 7"))
print(f"dia de la semana '{determinardiadesemana(vardia)}'")

