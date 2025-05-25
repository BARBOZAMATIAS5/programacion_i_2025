import random

ingreso_numero = int(input("Ingrese el la altura en centimetros: "))

if ingreso_numero < 160:
    print("Base")
elif ingreso_numero < 180:
    print ("Escolta")
elif ingreso_numero < 200:
    print ("Alero")
else:
    print ("Ala-Pivot o Pivot")

nota_aleatoria = random.randint(1,10)

print(nota_aleatoria)

if nota_aleatoria < 3:
    print("Desaprobado")
elif nota_aleatoria < 5:
    print("Aprobado")
else:
    print("Promocion directa")