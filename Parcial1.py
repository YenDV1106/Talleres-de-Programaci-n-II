#Parcial corte 1
#Jen Jeús Leal Ruiz
#Ejercicio 1

def agregar_estudiante(lista):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    nota = float(input("Nota: "))
    lista.append({"nombre": nombre, "edad": edad, "nota": nota})

def promedio(lista):
    return sum(est["nota"] for est in lista) / len(lista) if lista else 0.0

def mejor_estudiante(lista):
    est = max(lista, key=lambda x: x["nota"])
    return est["nombre"], est["nota"], est["edad"]

estudiantes = []
cantidad = int(input("¿Cuántos estudiantes desea registrar?: "))
for _ in range(cantidad):
    agregar_estudiante(estudiantes)

nombre, nota, edad = mejor_estudiante(estudiantes)

print(f"\nTotal estudiantes: {len(estudiantes)}")
print(f"Promedio general: {promedio(estudiantes):.1f}")
print(f"Mejor estudiante: {nombre} – {nota} – {edad}")

#Ejercicio 2

def buscar(inventario, codigo):
    for prod in inventario:
        if prod[0] == codigo:
            return prod
    return None

def valor_total(inventario):
    return sum(precio * cantidad for _, _, precio, cantidad in inventario)

def actualizar_stock(inventario, codigo, nueva_cantidad):
    for i, prod in enumerate(inventario):
        if prod[0] == codigo:
            temp = list(prod)
            temp[3] = nueva_cantidad
            inventario[i] = tuple(temp)
            break

inventario = [
    ("P001", "Laptop Gaming pro player", 800.0, 5),
    ("P002", "Mouse Para mancos", 20.0, 15),
    ("P003", "Teclado RGB", 50.0, 10),
    ("P004", "Monitor 4k con más fps", 150.0, 7),
    ("P005", "Impresora 3D", 200.0, 3),
    ("P006", "Auriculares Estereo", 30.0, 12)
]

actualizar_stock(inventario, "P002", 20)

print("Inventario actual:")
print(f"{'Código':<8} {'Nombre':<10} {'Precio':<10} {'Cantidad':<10} {'Valor Total':<10}")
for cod, nom, prec, cant in inventario:
    print(f"{cod:<8} {nom:<10} {prec:<10.2f} {cant:<10} {prec * cant:<10.2f}")

#Ejercicio 3

ventas = {
    "enero":    [1200, 1500,  800, 900],
    "febrero":  [1000, 1100, 1200],
    "marzo":    [1800, 1700, 1600, 2000]
}

def total_mes(ventas, mes):
    return sum(ventas[mes])

def promedio_general(ventas):
    todas = [v for lista in ventas.values() for v in lista]
    return sum(todas) / len(todas)

def mejor_mes(ventas):
    return max(ventas, key=lambda m: total_mes(ventas, m))

def filtrar_ventas_altas(ventas, limite):
    return [v for lista in ventas.values() for v in lista if v >= limite]

limite_ingresado = 1500

print("Total por mes:")
print(f"Enero: {total_mes(ventas, 'enero')}")
print(f"Febrero: {total_mes(ventas, 'febrero')}")
print(f"Marzo: {total_mes(ventas, 'marzo')}")
print(f"\nPromedio general trimestral: {promedio_general(ventas):.2f}")
print(f"\nMejor mes: {mejor_mes(ventas).capitalize()}")
print(f"\nVentas mayores al límite ingresado: {filtrar_ventas_altas(ventas, limite_ingresado)}")