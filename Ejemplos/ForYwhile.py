for i in range(1, 5):
  print(i)
print("fin")

counter = 0
while counter < 5:
  print(counter)
  counter += 1
print("fin")

counter2 = 0
while True:
  counter2 += 1
  if counter2 == 10:
    break
  print(counter2)
print("fin")

while True:
  data = int(input("Ingrese 1 o 2: "))
  if data == 1 or data == 2:
    break
  else:
    print(u"Opción no válida")