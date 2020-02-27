promedio = input("Ingrese su promedio: ")
tipoC = input("Si es alumno de pregrado digite 1, si es alumno de posgrado digite 2: ")
valCreditoPre = 50000
valCreditoPos = 300000
print(promedio.isdigit())
if (promedio.isdigit()) and tipoC.isdigit():
  print(promedio.isdigit())
  print(tipoC.isdigit())
  if int(promedio) >= 4.5 and int(tipoC) == 1:
    creditos = 28
    descuento = 25/100

    totalCreditos = creditos * valCreditoPre
    total = totalCreditos * descuento
    print("Total a pagar: " + str(total))
  elif int(promedio) >= 4 and float(promedio) < 4.5 and int(tipoC) == 1:
    creditos = 25
    descuento = 10/100

    totalCreditos = creditos * valCreditoPre
    total = totalCreditos * descuento
    print("Total a pagar: " + str(total))
  elif int(promedio) > 3.5 and float(promedio) < 4 and int(tipoC) == 1:
    creditos = 20

    totalCreditos = creditos * valCreditoPre
    total = totalCreditos
    print("Total a pagar: " + str(total))
  elif int(promedio) >= 2.5 and float(promedio) < 3.5 and int(tipoC) == 1:
    creditos = 15

    totalCreditos = creditos * valCreditoPre
    total = totalCreditos
    print("Total a pagar: " + str(total))
  elif int(promedio) < 2.5 and int(tipoC) == 1:
    print("No se puede matricular")
  elif float(promedio) >= 4.5 and int(tipoC) == 2:
    creditos = 20
    descuento = 20/100

    totalCreditos = creditos * valCreditoPos
    total = totalCreditos * descuento
    print("Total a pagar: " + str(total))
  elif int(promedio) < 4.5 and int(tipoC) == 2:
    creditos = 10

    totalCreditos = creditos * valCreditoPos
    total = totalCreditos
    print("Total a pagar: " + str(total))
  else:
    print("Error, tipo o promedio incorrectos")
else:
  print("El promedio y el tipo debe ser un número")