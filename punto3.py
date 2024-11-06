#Aplicar sueldo del empleado
SueldoTabajador = float(input("digite su sueldo: "))
aumento = SueldoTabajador +(SueldoTabajador* 0.15)


if SueldoTabajador < 300000 :
    print("su sueldo es de: " , aumento)

else:
   print (" su sueldo es de : " , SueldoTabajador)
