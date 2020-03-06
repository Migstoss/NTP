employee = 0
name = ""
salary = 0
eHours = 0
while employee < 2:
  name = input("Ingrese el nombre del empleado: ")
  salary = int(input("Ingrese el salario base del empleado: "))
  eHours = int(input("Ingrese el número de horas extras trabajadas por el empleado: "))

  valHE = (salary * 10)/100
  salaryHE = salary + (valHE * eHours)
  print("")
  print("Nombre del empleado: " + name)
  print("Salario del empleado: " + str(salary))
  print("Número de horas extra: " + str(eHours))
  print("Salario + horas extra: " + str(salaryHE) + " (Valor de la hora extra: " + str(valHE) + ")")
  if salaryHE >= 200000 and salaryHE <= 600000:
    print("Categoria: A")
  elif salaryHE > 600000:
    print("Categoria: B")
  print("")

  employee += 1

