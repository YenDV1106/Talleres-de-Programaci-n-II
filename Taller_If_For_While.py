#Taller de programación IF, FOR y WHILE
#Jen Jesús Leal Ruiz

#Ejercicio 1:

lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

if lado1 > 0 and lado2 > 0 and lado3 > 0:

    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        print("Los lados forman un triángulo válido.")

        if lado1 == lado2 and lado2 == lado3:
            print("Clasificación: Equilátero")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Clasificación: Isósceles")
        else:
            print("Clasificación: Escaleno")
    else:
        print("Error: Los lados no cumplen la condición de existencia.")
else:
    print("Error: Todos los lados deben ser mayores que cero.")

    #Ejercicio 2:

    cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
aprobados = 0
reprobados = 0
suma_promedios = 0
promedio_mas_alto = 0.0
promedio_mas_bajo = 5.0

for i in range(1, cantidad_estudiantes + 1):
    print(f"\nEstudiante {i}:")
    nota1 = float(input("Calificación 1 (0.0 - 5.0): "))
    nota2 = float(input("Calificación 2 (0.0 - 5.0): "))
    nota3 = float(input("Calificación 3 (0.0 - 5.0): "))
    
    if 0.0 <= nota1 <= 5.0 and 0.0 <= nota2 <= 5.0 and 0.0 <= nota3 <= 5.0:
        promedio = (nota1 + nota2 + nota3) / 3
        suma_promedios += promedio
        
        if promedio <= 2.9:
            clasificacion = "Reprobado"
            reprobados += 1
        elif promedio <= 3.9:
            clasificacion = "Aprobado"
            aprobados += 1
        elif promedio <= 4.5:
            clasificacion = "Sobresaliente"
            aprobados += 1
        else:
            clasificacion = "Excelente"
            aprobados += 1
            
        print(f"Promedio: {promedio:.2f} - {clasificacion}")
        
        if promedio > promedio_mas_alto:
            promedio_mas_alto = promedio
        if promedio < promedio_mas_bajo:
            promedio_mas_bajo = promedio
    else:
        print("Error: Las calificaciones deben estar entre 0.0 y 5.0.")

if cantidad_estudiantes > 0:
    promedio_general = suma_promedios / cantidad_estudiantes
    print("\n--- RESUMEN FINAL ---")
    print(f"Estudiantes aprobados: {aprobados}")
    print(f"Estudiantes reprobados: {reprobados}")
    print(f"Promedio general del grupo: {promedio_general:.2f}")
    print(f"Promedio más alto: {promedio_mas_alto:.2f}")
    print(f"Promedio más bajo: {promedio_mas_bajo:.2f}")

    #Ejercicio 3:

    numero = int(input("Ingrese un número entero mayor que 1: "))

if numero > 1:
    divisores = ""
    contador_divisores = 0
    i = 1
    
    while i <= numero:
        if numero % i == 0:
            contador_divisores += 1
            if divisores == "":
                divisores = str(i)
            else:
                divisores = divisores + ", " + str(i)
        i += 1
        
    print(f"Divisores: {divisores}")
    
    if contador_divisores == 2:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")
else:
    print("El número debe ser estrictamente mayor que 1.")

#Ejercicio 4:

saldo = 1500000.0
opcion = 0
depositos_realizados = 0
retiros_realizados = 0
movimientos = ""

while opcion != 5:
    print("\n--- MENÚ CAJERO ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver movimientos realizados")
    print("5. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        print(f"Saldo actual: ${saldo:,.2f}")
    elif opcion == 2:
        monto = float(input("Ingrese la cantidad a depositar: "))
        if monto > 0:
            saldo += monto
            depositos_realizados += 1
            movimientos += f"Depósito: +${monto:,.2f}\n"
            print("Depósito realizado con éxito.")
        else:
            print("Error: No se permiten depósitos negativos.")
    elif opcion == 3:
        monto = float(input("Ingrese la cantidad a retirar: "))
        costo_retiro = 4500.0
        total_a_descontar = monto + costo_retiro
        
        if monto < 10000:
            print("Error: El retiro mínimo es de $10.000.")
        elif total_a_descontar > saldo:
            print("Error: Fondos insuficientes (incluyendo la comisión de $4.500).")
        else:
            saldo -= total_a_descontar
            retiros_realizados += 1
            movimientos += f"Retiro: -${monto:,.2f} (Comisión: ${costo_retiro:,.2f})\n"
            print("Retiro realizado con éxito.")
    elif opcion == 4:
        print("\n--- MOVIMIENTOS ---")
        print(f"Total depósitos: {depositos_realizados}")
        print(f"Total retiros: {retiros_realizados}")
        print(movimientos if movimientos else "Sin movimientos registrados.")
    elif opcion == 5:
        print("Saliendo del cajero automático...")
    else:
        print("Opción inválida.")

#Ejercicio 5:

cantidad_productos = int(input("Ingrese la cantidad de productos comprados: "))
subtotal_general = 0
total_descuentos_general = 0

for i in range(1, cantidad_productos + 1):
    print(f"\nProducto {i}:")
    nombre = input("Nombre: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    tipo = input("Tipo (alimento, aseo, otro): ").lower()
    
    subtotal_producto = precio * cantidad
    descuento_producto = 0
    
    if tipo == "alimento":
        descuento_producto = subtotal_producto * 0.05
    elif tipo == "aseo":
        if cantidad >= 3:
            descuento_producto = subtotal_producto * 0.10
    elif tipo == "otro":
        descuento_producto = 0
        
    subtotal_general += subtotal_producto
    total_descuentos_general += descuento_producto
    
    print(f"Subtotal de {nombre}: ${subtotal_producto:,.2f}")
    print(f"Descuento aplicado: ${descuento_producto:,.2f}")

descuento_adicional = 0
if subtotal_general > 300000:
    descuento_adicional = subtotal_general * 0.05
    total_descuentos_general += descuento_adicional

total_definitivo = subtotal_general - total_descuentos_general

print("\n--- RESUMEN DE FACTURA ---")
print(f"Total antes del descuento general: ${subtotal_general:,.2f}")
print(f"Total de descuentos: ${total_descuentos_general:,.2f}")
print(f"Total definitivo: ${total_definitivo:,.2f}")

#Ejercicio 6:

cantidad = 0
positivos = 0
negativos = 0
pares = 0
impares = 0
suma = 0
mayor = 0
menor = 0

numero = int(input("Ingrese un número entero (0 para terminar): "))

if numero == 0:
    print("El primer número ingresado fue 0. No se realizaron cálculos.")
else:
    mayor = numero
    menor = numero
    
    while numero != 0:
        cantidad += 1
        suma += numero
        
        if numero > 0:
            positivos += 1
        else:
            negativos += 1
            
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
            
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
            
        numero = int(input("Ingrese otro número (0 para terminar): "))
        
    promedio = suma / cantidad
    print("\n--- ESTADÍSTICAS ---")
    print(f"Cantidad ingresada: {cantidad}")
    print(f"Positivos: {positivos} | Negativos: {negativos}")
    print(f"Pares: {pares} | Impares: {impares}")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Número mayor: {mayor}")
    print(f"Número menor: {menor}")

#Ejercicio 7:

decimal = int(input("Ingrese un número entero positivo: "))

if decimal > 0:
    aux = decimal
    binario = ""
    while aux > 0:
        residuo = aux % 2
        binario = str(residuo) + binario
        aux = aux // 2
    print(f"Número decimal: {decimal}")
    print(f"Resultado binario: {binario}")
elif decimal == 0:
    print("Resultado binario: 0")
else:
    print("Error: Ingrese un número entero positivo.")

#Ejercicio 8:

terminos = int(input("Ingrese la cantidad de términos: "))

if terminos > 0:
    a = 0
    b = 1
    suma = 0
    pares = 0
    impares = 0
    serie = ""

    for i in range(terminos):
        if i == 0:
            actual = a
        elif i == 1:
            actual = b
        else:
            siguiente = a + b
            a = b
            b = siguiente
            actual = siguiente
            
        suma += actual
        if actual % 2 == 0:
            pares += 1
        else:
            impares += 1
            
        if i == 0:
            serie = str(actual)
        else:
            serie += ", " + str(actual)

    print(f"Serie completa: {serie}")
    print(f"Suma de términos: {suma}")
    print(f"Términos pares: {pares}")
    print(f"Términos impares: {impares}")
else:
    print("Ingrese una cantidad mayor a cero.")

#Ejercicio 9:

pares_tablas = 0
impares_tablas = 0
mayores_50 = 0

for i in range(1, 11):
    print(f"\nTABLA DEL {i}")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} × {j} = {resultado}")
        
        if resultado % 2 == 0:
            pares_tablas += 1
        else:
            impares_tablas += 1
            
        if resultado > 50:
            mayores_50 += 1

print("\n--- RESUMEN ---")
print(f"Resultados pares: {pares_tablas}")
print(f"Resultados impares: {impares_tablas}")
print(f"Resultados mayores que 50: {mayores_50}")

#Ejercicio 10:

n = int(input("Ingrese un número entre 3 y 10: "))

if 3 <= n <= 10:
    for i in range(1, n + 1):
        linea = ""
        for j in range(1, i + 1):
            linea += str(j) + " "
        print(linea)
        
    for i in range(n - 1, 0, -1):
        linea = ""
        for j in range(1, i + 1):
            linea += str(j) + " "
        print(linea)
else:
    print("El número debe estar entre 3 y 10.")

#Ejercicio 11:

import random

print("Seleccione la dificultad:")
print("1. Fácil: 1 a 20, 6 intentos")
print("2. Intermedio: 1 a 50, 5 intentos")
print("3. Difícil: 1 a 100, 4 intentos")

dificultad = int(input("Opción: "))

if dificultad == 1:
    limite = 20
    intentos = 6
elif dificultad == 2:
    limite = 50
    intentos = 5
elif dificultad == 3:
    limite = 100
    intentos = 4
else:
    limite = 20
    intentos = 6

numero_secreto = random.randint(1, limite)
adivinado = False

for intento_actual in range(1, intentos + 1):
    print(f"\nIntento {intento_actual} de {intentos}")
    intento_usuario = int(input(f"Adivine el número (1 a {limite}): "))
    
    if intento_usuario == numero_secreto:
        print("Número correcto")
        intentos_restantes = intentos - intento_actual + 1
        puntaje = intentos_restantes * 20
        print(f"Puntaje obtenido: {puntaje}")
        adivinado = True
        break
    elif intento_usuario < numero_secreto:
        print("El número secreto es mayor")
    else:
        print("El número secreto es menor")

if not adivinado:
    print(f"\nPerdiste. El número secreto era: {numero_secreto}")
    print("Puntaje: 0")

#Ejercicio 12:

usuario_correcto = "administrador"
clave_correcta = "Python2026"
intentos_maximos = 3
acceso_concedido = False

for intento in range(1, intentos_maximos + 1):
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso_concedido = True
        break
    else:
        intentos_restantes = intentos_maximos - intento
        if intentos_restantes > 0:
            print(f"Credenciales incorrectas. Quedan {intentos_restantes} intentos.")
        else:
            print("Sistema bloqueado por exceder los intentos fallidos.")

if acceso_concedido:
    opcion_menu = 0
    while opcion_menu != 3:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Consultar información")
        print("2. Cambiar contraseña")
        print("3. Cerrar sesión")
        
        opcion_menu = int(input("Seleccione una opción: "))
        
        if opcion_menu == 1:
            print("Información del sistema: Operación segura.")
        elif opcion_menu == 2:
            clave_actual = input("Ingrese su contraseña actual: ")
            if clave_actual == clave_correcta:
                nueva_clave = input("Ingrese la nueva contraseña: ")
                clave_correcta = nueva_clave
                print("Contraseña actualizada con éxito.")
            else:
                print("Contraseña actual incorrecta.")
        elif opcion_menu == 3:
            print("Cerrando sesión...")
        else:
            print("Opción inválida.")

#Ejercicio Integrador:

opcion = 0
cantidad_ventas = 0
total_bruto = 0
total_descuentos = 0
total_recargos = 0
total_recibido = 0

venta_mayor = 0
venta_menor = 0
pagos_efectivo = 0
pagos_tarjeta = 0
pagos_transferencia = 0
clientes_con_descuento = 0
suma_ventas = 0

while opcion != 5:
    print("\nSISTEMA DE VENTAS")
    print("1. Registrar una venta")
    print("2. Consultar resumen de ventas")
    print("3. Consultar venta mayor y menor")
    print("4. Aplicar cierre de caja")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("\n--- REGISTRO DE VENTA ---")
        cliente = input("Nombre del cliente: ")
        cantidad_prod = int(input("Cantidad de productos: "))
        precio_unit = format_precio = float(input("Precio de cada producto: "))
        
        if cantidad_prod > 0 and precio_unit > 0:
            subtotal_venta = cantidad_prod * precio_unit
            medio_pago = input("Medio de pago (efectivo, tarjeta, transferencia): ").lower()
            
            descuento_venta = 0
            recargo_venta = 0
            recibio_desc = False
            
            if subtotal_venta > 500000:
                descuento_venta += subtotal_venta * 0.10
                recibio_desc = True
                
            if medio_pago == "efectivo":
                pagos_efectivo += 1
                if subtotal_venta > 200000:
                    descuento_venta += subtotal_venta * 0.03
                    recibio_desc = True
            elif medio_pago == "tarjeta":
                pagos_tarjeta += 1
                recargo_venta = subtotal_venta * 0.02
            elif medio_pago == "transferencia":
                pagos_transferencia += 1
            else:
                print("Medio no reconocido, se procesará por transferencia sin recargo.")
                pagos_transferencia += 1

            if recibio_desc:
                clientes_con_descuento += 1

            neto_venta = subtotal_venta - descuento_venta + recargo_venta
            
            cantidad_ventas += 1
            total_bruto += subtotal_venta
            total_descuentos += descuento_venta
            total_recargos += recargo_venta
            total_recibido += neto_venta
            suma_ventas += neto_venta
            
            if cantidad_ventas == 1:
                venta_mayor = neto_venta
                venta_menor = neto_venta
            else:
                if neto_venta > venta_mayor:
                    venta_mayor = neto_venta
                if neto_venta < venta_menor:
                    venta_menor = neto_venta
                    
            print(f"Venta registrada. Total a pagar: ${neto_venta:,.2f}")
        else:
            print("Error: El precio y la cantidad deben ser positivos.")

    elif opcion == 2:
        if cantidad_ventas == 0:
            print("Aún no existen ventas registradas.")
        else:
            promedio_ventas = suma_ventas / cantidad_ventas
            print("\n--- RESUMEN DE VENTAS ---")
            print(f"Cantidad de ventas: {cantidad_ventas}")
            print(f"Valor total bruto: ${total_bruto:,.2f}")
            print(f"Total descuentos: ${total_descuentos:,.2f}")
            print(f"Total recargos: ${total_recargos:,.2f}")
            print(f"Dinero definitivo recibido: ${total_recibido:,.2f}")
            print(f"Promedio de ventas: ${promedio_ventas:,.2f}")
            print(f"Pagos en efectivo: {pagos_efectivo}")
            print(f"Pagos con tarjeta: {pagos_tarjeta}")
            print(f"Pagos por transferencia: {pagos_transferencia}")
            print(f"Clientes con descuento: {clientes_con_descuento}")

    elif opcion == 3:
        if cantidad_ventas == 0:
            print("Aún no existen ventas registradas.")
        else:
            print("\n--- VENTA MAYOR Y MENOR ---")
            print(f"Venta más alta: ${venta_mayor:,.2f}")
            print(f"Venta más baja: ${venta_menor:,.2f}")

    elif opcion == 4:
        if cantidad_ventas == 0:
            print("Aún no existen ventas registradas.")
        else:
            print("\n--- CIERRE DE CAJA ---")
            print(f"Total transacciones: {cantidad_ventas}")
            print(f"Efectivo total esperado en caja: ${total_recibido:,.2f}")
            print("Cierre aplicado exitosamente.")

    elif opcion == 5:
        print("Saliendo del sistema de ventas...")

    else:
        print("Opción inválida.")