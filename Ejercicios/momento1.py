countHombresMoviles = 0; countHombresWeb = 0; countMujeresMoviles = 0; countMujeresWeb = 0
averageHM = 0; averageHW = 0; averageMM = 0; averageMW = 0
quantityGradesHM = 0; quantityGradesHW = 0; quantityGradesMM = 0; quantityGradesMW = 0
totalAverageHM = 0; totalAverageHW = 0; totalAverageMM = 0; totalAverageMW = 0
acc = 0
error = 0

print("Proceso de finalización del semestre")

numStudent = input("Ingrese en número de alumnos: ")

for i in range (0, int(numStudent)):

  gender = input("Ingrese si el estudiante es Hombre o Mujer: ")

  subject = input("Ingrese el programa academico\n(Moviles - Web): ")

  if gender.lower() == "hombre" and subject.lower() == "moviles":
    countHombresMoviles += 1
    print("A continuación va a ingresar una a una las 5 notas que sacó durante el curso")
    for i in range (0, 5):
      grades = input("Ingrese una nota que sacó durante el curso: ")
      quantityGradesHM += 1
      averageHM = averageHM + int(grades)

  elif gender.lower() == "hombre" and subject.lower() == "web":
    countHombresWeb += 1
    print("A continuación va a ingresar una a una las 5 notas que sacó durante el curso")
    for i in range (0, 5):
      grades = input("Ingrese una nota que sacó durante el curso: ")
      quantityGradesHW += 1      
      averageHW = averageHW + int(grades)

  elif gender.lower() == "mujer" and subject.lower() == "moviles":
    countMujeresMoviles += 1
    print("A continuación va a ingresar una a una las 5 notas que sacó durante el curso")
    for i in range (0, 5):
      grades = input("Ingrese una nota que sacó durante el curso: ")
      quantityGradesMM += 1      
      averageMM = averageMM + int(grades)

  elif gender.lower() == "mujer" and subject.lower() == "web":
    countMujeresWeb += 1
    print("A continuación va a ingresar una a una las 5 notas que sacó durante el curso")
    for i in range (0, 5):
      grades = input("Ingrese una nota que sacó durante el curso: ")
      quantityGradesMW += 1      
      averageMW = averageMW + int(grades)

  else:
    error += 1
  if averageHM > 0:
    totalAverageHM = averageHM/quantityGradesHM
  if averageHW > 0:
    totalAverageHW = averageHW/quantityGradesHW
  if averageMM > 0:
    totalAverageMM = averageMM/quantityGradesMM
  if averageMW > 0:
    totalAverageMW = averageMW/quantityGradesMW

print("\n")
print("Cantidad de hombres en Moviles: " + str(countHombresMoviles))
print("Promedio de notas de los hombres en móviles: " + str(totalAverageHM))
print("Cantidad de hombres en Web: " + str(countHombresWeb))
print("Promedio de notas de los hombres en web: " + str(totalAverageHW))
print("Cantidad de mujeres en Moviles: " + str(countMujeresMoviles))
print("Promedio de notas de las mujeres en moviles: " + str(totalAverageMM))
print("Cantidad de mujeres en Web: " + str(countMujeresWeb))
print("Promedio de notas de las mujeres en web: " + str(totalAverageMW))
print("Errores: " + str(error))
print("\n")

accAge = 0
countAD = 0
countHAD = 0
countMAD = 0
averageAD = 0

print("Proceso de admisión")

while True:
  finish = input("Desea continuar con el proceso de admisión?\n(Si - No): ")
  if finish.lower() == "no":
    break

  countAD += 1
  genderAD = input("Ingrese si el estudiante es hombre o mujer: ")

  if genderAD.lower() == "hombre":
    countHAD += 1
  elif genderAD.lower() == "mujer":
    countMAD += 1

  ageAD = input("Ingrese la edad del estudiante: ")

  accAge = accAge + int(ageAD)

if accAge > 0:
  averageAD = accAge / countAD

print("Total de estudiantes que se matricularon: " + str(countAD))
print("Cantidad de hombres que se matricularon: " + str(countHAD))
print("Cantidad de mujeres que se matricularon: " + str(countMAD))
print("Promadio de edad de los matriculados: " + str(averageAD))