print("Plato         Valor")
print("Hamburguesa   10000\nPerros        8000\nSalchipapas   6000\nChorizo       7000")

cantidadP = input("Ingrese la cantidad de personas: ")
cantidadP = int(cantidadP) + 1
hamCounter = 0
perCounter = 0
salcCounter = 0
choCounter = 0

acc = 0

for i in range(1, int(cantidadP)):
  order = input("Ingrese el pedido del cliente: ")

  if order.lower() == "hamburguesa":
    value = 10000
    hamCounter += 1
  elif order.lower() == "perros":
    value = 8000
    perCounter += 1
  elif order.lower() == "salchipapas":
    value = 6000
    salcCounter += 1
  elif order.lower() == "chorizo":
    value = 7000
    choCounter += 1
  else:
    value = 0
    print("Error")

  acc = acc + value

discount1 = 0
discount2 = 0

if acc > 20000:
  discount1 = (acc * 10)/100
  #total = acc - discount
  print("La compra es mayor a 20000, se le realizó un descuento del 10%")

if hamCounter >= 2 or perCounter >= 2 or salcCounter >= 2 or choCounter >= 2:
  discount2 = (acc * 5)/100
  #total = total - discount
  print("Por la compra de dos o mas productos iguales se le realiza un descuento del 5%")

total = acc - discount1 - discount2

tipIf = input("Desea incluir la propina? (si - no): ")
if tipIf == "si":
  tip = (total * 10)/100
  totalTip = tip + total

  print("Valor + propina: " + str(totalTip))
else:
  print("Valor: " + str(total))

