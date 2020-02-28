counter = 0; accAge = 0; accWeight = 0; b3a4 = 0; b4a6 = 0; h6 = 0

while True:
  age = input("Ingrese su edad: ")
  weight = input("Ingrese su peso: ")
  counter += 1

  if int(age) >= 30 and int(age) < 40:
    b3a4 += 1
  
  if int(age) >= 40 and int(age) < 60:
    b4a6 += 1
  
  if int(age) > 60:
    h6 += 1

  accAge = accAge + int(age)
  averageAge = accAge / counter

  accWeight = accWeight + float(weight)
  averageWeight = accWeight / counter
    
  if counter % 5 == 0:
    finish = input("Tiene " + str(counter) + " encuestados ¿Desea finalizar?\n(si - no): ")
    if finish == "si":
      break

print("Cantidad de encuestados: " + str(counter))
print("Cantidad de encuestados cuya edad está entre 30 y 40: " + str(b3a4))
print("Cantidad de encuestados cuya edad está entre 40 y 60: " + str(b4a6))
print("Cantidad de encuestados cuya edad es mayor a 60: " + str(h6))
print("El promedio de edades es: " + str(averageAge))
print("El promedio de peso es: " + str(averageWeight))