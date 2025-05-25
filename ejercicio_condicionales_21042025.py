'''
Facturación del Servicio de Agua Potable
El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. 
Para garantizar un uso eficiente del recurso y establecer una estructura justa de costos, se han definido diferentes tarifas y 
ajustes según el consumo y el tipo de cliente.
Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y 
un costo variable por metro cúbico consumido. Además, se aplican bonificaciones y 
recargos dependiendo del consumo y la categoría del usuario. En algunos casos especiales, 
también pueden otorgarse descuentos adicionales.
A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios 
para determinar el monto final a pagar.
Tarifa base:
Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
El costo por metro cúbico (m³) de agua es de $200/m³.
Bonificaciones y Recargos según tipo de cliente:
Cliente Residencial:
Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.
Cliente Comercial:
Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
Si el consumo es menor a 50 m³, se aplica un recargo del 5%.
Cliente Industrial:
Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
consumo.
Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
Si el consumo es menor a 200 m³, se aplica un recargo del 10%.
Casos especiales:
Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
En todos los casos, se aplica el IVA del 21% sobre el total.
Requerimientos del programa:
Solicitar al usuario:
Cantidad de metros consumidos
Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
Calcular:
Subtotal de consumo.
Bonificaciones, si corresponde
Recargos, si corresponde
Subtotal, con recargos y bonificaciones.
IVA aplicado (21%), si corresponde.
Total final a pagar.
Mostrar en pantalla el desglose de los cálculos

'''

consumo_mtsc = float(input("Ingrese el consumo del usuario (metros cubicos): "))

tipo_cliente = str(input("Ingrese el tipo de cliente (Residencial/Comercial/Industrial)"))


tarifa_fija = 7000
consumo_y_tarifa = consumo_mtsc + tarifa_fija
costo_por_mt3 = 200
iva = 1.21
bonificacion = 1
recargo = 1
precio_final = 0

match tipo_cliente:
    case "Residencial":
        if (consumo_mtsc < 30):
            bonificacion = 0.90
        elif (consumo_mtsc > 80):
            recargo = 1.15
            
    case "Comercial":
        if (consumo_mtsc > 150):
            bonificacion = 0.92  
        elif (consumo_mtsc > 300):
            bonificacion = 0.88
        elif (consumo_mtsc < 50):
            recargo = 1.05

    case "Industrial":
        if (consumo_mtsc > 500):
            bonificacion = 0.80
        elif (consumo_mtsc > 1000):
            bonificacion = 0.70
        elif (consumo_mtsc < 200):
            recargo = 1.10

    case _:
        print("Error al ingresar el tipo de cliente")

consumo_mtsc = consumo_y_tarifa * bonificacion
consumo_mtsc = consumo_y_tarifa * recargo

print("Subtotal: "+ (consumo_y_tarifa))
print("Bonificaciones: "+ (consumo_y_tarifa ))
print("Recargos: ")
print("Subtotal (con recargos y bonificaciones): ")
print("IVA aplicado (21%)")
print("Total a pagar: ")
