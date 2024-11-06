#leer  registro de personas
nombre = (input (" digite el nombre: "))
edad   = int (input ("digite su edad: "))
sexo   = (input("digite su sexo M/H: "))
EstadoCivil = int( input ("digite su estado civil: "))

if sexo == "hombre" and edad > 40 and EstadoCivil == "casado":
    print("(nombre) es una hombre mayor de 40 años y esta casado" )
    
elif sexo == "mujer" and edad < 50 and EstadoCivil == "soltera":
    print ("(nombre) es una mujer soltera menor de 50 años")
else:
        ("(nombre) no cumple los requisitos ")

