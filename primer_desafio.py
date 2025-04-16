import random

ingreso_numero = input("Ingrese el la altura en centimetros: ")

if int(ingreso_numero) < 160:
    print("Base")
elif 160 <= int(ingreso_numero) <= 179:
    print ("Escolta")
elif 180 < int(ingreso_numero) <= 199:
    print ("Alero")
elif int(ingreso_numero) >= 200:
    print ("Ala-Pivot o Pivot")

nota_aleatoria = random.randint(1,10)

print(nota_aleatoria)

if nota_aleatoria <= 3:
    print("Desaprobado")
elif 3 < nota_aleatoria <= 5:
    print("Aprobado")
elif 5 < nota_aleatoria <= 10:
    print("Promicion directa")