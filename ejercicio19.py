anio = float(input("ingrese el año: "))

def es_bisciesto(anio):
  if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):  
        return True
  else:
        return False
if es_bisciesto(anio):
   print(f"El año {anio} es bisiesto.")
else:
   print(f"El año {anio} no es bisiesto.")

