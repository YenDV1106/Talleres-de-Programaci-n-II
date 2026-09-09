#Parcial corte 1
#Jen Jeús Leal Ruiz
#Ejercicio 1

def agregar_estudiante(lista):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    nota = float(input("Nota: "))
    estudiante = {"nombre": nombre, "edad": edad, "nota": nota}
    lista.append(estudiante)

def promedio(lista):
    suma = 0
    for est in lista:
        suma = suma + est["nota"]
    return suma / len(lista)

def mejor_estudiante(lista):
    mejor = lista[0]
    for est in lista:
        if est["nota"] > mejor["nota"]:
            mejor = est
    return mejor["nombre"], mejor["nota"], mejor["edad"]

estudiantes = []
cantidad = int(input("¿Cuántos estudiantes desea registrar?: "))
for i in range(cantidad):
    agregar_estudiante(estudiantes)

nombre, nota, edad = mejor_estudiante(estudiantes)

print("\nTotal estudiantes:", len(estudiantes))
print("Promedio general:", promedio(estudiantes))
print("Mejor estudiante:", nombre, "–", nota, "–", edad)

#Ejercicio 2

def buscar(inventario, codigo):
    for prod in inventario:
        if prod[0] == codigo:
            return prod
    return None

def valor_total(inventario):
    total = 0
    for prod in inventario:
        precio = prod[2]
        cantidad = prod[3]
        total = total + (precio * cantidad)
    return total

def actualizar_stock(inventario, codigo, nueva_cantidad):
    for i in range(len(inventario)):
        if inventario[i][0] == codigo:
            temp = list(inventario[i])
            temp[3] = nueva_cantidad
            inventario[i] = tuple(temp)

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
print("Código\tNombre\t\t\tPrecio\tCantidad\tValor Total")
for prod in inventario:
    cod = prod[0]
    nom = prod[1]
    prec = prod[2]
    cant = prod[3]
    v_total = prec * cant
    print(f"{cod}\t{nom}\t{prec}\t{cant}\t\t{v_total}")

#Ejercicio 3

ventas = {
    "enero":    [1200, 1500,  800, 900],
    "febrero":  [1000, 1100, 1200],
    "marzo":    [1800, 1700, 1600, 2000]
}

def total_mes(ventas, mes):
    suma = 0
    for v in ventas[mes]:
        suma = suma + v
    return suma

def promedio_general(ventas):
    suma_total = 0
    contador = 0
    for mes in ventas:
        for v in ventas[mes]:
            suma_total = suma_total + v
            contador = contador + 1
    return suma_total / contador

def mejor_mes(ventas):
    mayor_total = 0
    mes_mayor = ""
    for mes in ventas:
        total = total_mes(ventas, mes)
        if total > mayor_total:
            mayor_total = total
            mes_mayor = mes
    return mes_mayor

def filtrar_ventas_altas(ventas, limite):
    altas = []
    for mes in ventas:
        for v in ventas[mes]:
            if v >= limite:
                altas.append(v)
    return altas

limite_ingresado = 1500

print("Total por mes:")
print("Enero:", total_mes(ventas, "enero"))
print("Febrero:", total_mes(ventas, "febrero"))
print("Marzo:", total_mes(ventas, "marzo"))

print("\nPromedio general trimestral:", promedio_general(ventas))
print("\nMejor mes:", mejor_mes(ventas))
print("\nVentas mayores al límite ingresado:", filtrar_ventas_altas(ventas, limite_ingresado))