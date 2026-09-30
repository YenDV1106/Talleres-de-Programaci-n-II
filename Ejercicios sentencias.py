#Ejercicios Semana 8
#Juan Ruiz
#Jen Leal
#Ejercicio 1
Tasa_anual = 0.15
capital_inicial = float(input("Ingrese el capital a invertir: $"))
tasa_mensual = (1 + Tasa_anual) ** (1 / 12) - 1
ganancia = capital_inicial * tasa_mensual
total_final = capital_inicial + ganancia
print(f"Tasa mensual equivalente: {tasa_mensual * 100:.2f}%")
print(f"Ganancia en el mes: ${ganancia:,.2f}")
print(f"Total disponible: ${total_final:,.2f}")

#Ejercicio 2
Sueldo_base = 2000000
ventas = float(input("Ingrese el total de ventas del mes: $"))
comision = ventas * 0.10
total_sueldo = Sueldo_base + comision
print(f"Comisión por ventas: ${comision:,.2f}")
print(f"Total del sueldo: ${total_sueldo:,.2f}")

#Ejercicio 3
Total_de_la_compra = float(input("Ingrese el total de la compra: $"))
descuento = Total_de_la_compra * 0.15
total_a_pagar = Total_de_la_compra - descuento
print(f"Descuento: ${descuento:,.2f}")
print(f"Total a pagar: ${total_a_pagar:,.2f}")

#Ejercicio 4
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
examen_final = float(input("Ingrese la nota del examen final: "))
trabajo_final = float(input("Ingrese la nota del trabajo final: "))
promedio = (nota1 + nota2 + nota3) / 3
nota_final = promedio * 0.40 + examen_final * 0.50 + trabajo_final * 0.10
print(f"Promedio de las notas: {promedio:.2f}")
print(f"Nota final: {nota_final:.2f}")

#Ejercicio 5
pesos = float(input("Ingrese la cantidad de pesos colombianos a convertir: $"))
tasa_de_cambio = float(input("Ingrese la tasa de cambio actual (1 USD = ? COP): "))
dolares = pesos / tasa_de_cambio
print(f"La cantidad de dólares que puede obtener es: ${dolares:,.2f}")

# Ejercicio 6
numero = float(input("Ingresa un número: "))
absoluto = abs(numero)

print(f"El valor absoluto es: {absoluto}\n")

# Ejercicio 7
presion = float(input("Ingresa la presión: "))
volumen = float(input("Ingresa el volumen: "))
temperatura = float(input("Ingresa la temperatura: "))

masa = (presion * volumen) / (0.37 * (temperatura + 460))
print(f"La masa de aire es: {masa:.2f}\n")

# Ejercicio 8
edad = int(input("Ingresa tu edad: "))

num_pulsaciones = (220 - edad) / 10
print(f"Pulsaciones recomendadas por cada 10 segundos: {num_pulsaciones:.1f}")