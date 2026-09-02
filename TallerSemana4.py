#Taller Semana 4
#Jen Leal Ruiz
#Juan Aguirre
#Parte Teórica
#Función para pedir datos: input()
#Tipo dedato que devuelve input(): Siempre devuelve una cadena de texto (str).
#Diferencia entre int() y float(): int() convierte un valor a número entero sin decimales, mientras que float() lo convierte a número con decimales.
#Operador + con cadenas: Sirve para concatenar (unir) dos o más cadenas de texto.
#Diferencia entre / y //: / realiza una división exacta y devuelve un float, mientras que // realiza una división entera y devuelve solo la parte entera.
#Parte practica
#Punto 1
nombre = input("Nombre: ")
edad = input("Edad: ")
ciudad = input("Ciudad: ")

print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad}.")

#Punto 2
num1 = float(input("Digite el primer número: "))
num2 = float(input("Digite el segundo número: "))

suma = num1 + num2
print("La suma es:", suma)

#Punto 3
num1 = float(input("Numero 1: "))
num2 = float(input("Numero 2: "))

print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)

#Punto 4
nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))
nota3 = float(input("Digite nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

print("El promedio es:", promedio)

#Punto 5
nombre = input("Nombre: ")
apellido1 = input("Apellido 1: ")
apellido2 = input("Apellido 2: ")

nombre_completo = f"{nombre} {apellido1} {apellido2}"
print("Nombre completo:", nombre_completo)

#Punto 6
edad = int(input("Edad: "))
meses = edad * 12

print(f"Has vivido aproximadamente {meses} meses.")

#Punto 7
base = float(input("Base: "))
altura = float(input("Altura: "))

area = base * altura
print("El área del rectángulo es:", area)

#Punto 8
radio = float(input("Radio: "))
area = 3.1416 * (radio ** 2)

print("El área del círculo es:", area)

#Punto 9
producto = input("Producto: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

total = precio * cantidad
print(f"Total a pagar: ${total:.0f}")

#Punto 10
empleado = input("Nombre del empleado: ")
horas = float(input("Número de horas trabajadas: "))
valor_hora = float(input("Valor de la hora: "))

salario = horas * valor_hora

print(f"\nEmpleado: {empleado}")
print(f"Salario: ${salario:.0f}")

#punto 11
texto = input("Digite una palabra: ")

print(texto.upper())
print(texto.lower())

#punto 12
nombre_completo = input("Digite el nombre completo: ")
print("Cantidad de caracteres:", len(nombre_completo))

#punto 13
nombre = input("Nombre: ")
carrera = input("Carrera: ")
universidad = input("Universidad: ")

print(f"Hola {nombre}, estudias {carrera} en la {universidad}.")

#Retos practicos
#Reto 1
cliente = input("Nombre del cliente: ")
comida = float(input("Precio de la comida: "))
bebida = float(input("Precio de la bebida: "))
personas = int(input("Cantidad de personas: "))

total = comida + bebida
valor_por_persona = total / personas

print(f"\nTotal de la cuenta: ${total:.0f}")
print(f"Valor por persona: ${valor_por_persona:.0f}")

#Reto 2
celsius = float(input("Temperatura en grados Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"Temperatura en Fahrenheit: {fahrenheit}°F")

#Reto 3
pesos = float(input("Cantidad en pesos: "))
tasa_dolar = float(input("Valor actual del dólar: "))

dolares = pesos / tasa_dolar
print(f"Puedes obtener: ${dolares:.2f} USD")

#Reto 4
cliente = input("Cliente: ")
producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad
iva = subtotal * 0.19
total = subtotal + iva

print("\n------ FACTURA ------")
print(f"Cliente: {cliente}")
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Precio unitario: ${precio:.0f}\n")
print(f"Subtotal: ${subtotal:.0f}")
print(f"IVA: ${iva:.0f}")
print(f"TOTAL: ${total:.0f}")

#Reto 5
vendedor = input("Nombre del vendedor: ")
cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
cantidad = int(input("Cantidad: "))
precio = float(input("Precio unitario: "))

subtotal = precio * cantidad
descuento = subtotal * 0.10
base_con_descuento = subtotal - descuento
iva = base_con_descuento * 0.19
total = base_con_descuento + iva

print("\n========= VENTA =========")
print(f"Vendedor: {vendedor}")
print(f"Cliente: {cliente}")
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}\n")
print(f"Subtotal: ${subtotal:.0f}")
print(f"Descuento: ${descuento:.0f}")
print(f"IVA: ${iva:.0f}\n")
print(f"TOTAL A PAGAR: ${total:.0f}")