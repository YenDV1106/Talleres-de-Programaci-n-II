# Ejercicio 1:
numeros = [10, 25, 5, 40, 15]
print("Ejercicio 1:", numeros)

# Ejercicio 2:
numeros.append(50)
print("Ejercicio 2:", numeros)

# Ejercicio 3:
numeros.remove(25)
print("Ejercicio 3:", numeros)

# Ejercicio 4:
print(f"Ejercicio 4: Mayor = {max(numeros)}, Menor = {min(numeros)}")

# Ejercicio 5:
print("Ejercicio 5: Suma =", sum(numeros))

# Ejercicio 6:
pares = sum(1 for n in numeros if n % 2 == 0)
print("Ejercicio 6: Cantidad de pares =", pares)

# Ejercicio 7:
print("Ejercicio 7: Inverso =", numeros[::-1])

# Ejercicio 8:
lista_usuario = []
for i in range(5):
    num = int(input(f"Ingresa el número {i+1}: "))
    lista_usuario.append(num)
print("Ejercicio 8:", lista_usuario)

# Ejercicio 9:
buscado = int(input("Ingresa un número a buscar: "))
if buscado in numeros:
    print(f"Ejercicio 9: El número {buscado} sí existe en la lista.")
else:
    print(f"Ejercicio 9: El número {buscado} no existe en la lista.")

# Ejercicio 10:
duplicados = [n * 2 for n in numeros]
print("Ejercicio 10:", duplicados)

# Ejercicio 11:
tupla = (10, 20, 30, 20, 50)
print("Ejercicio 11:", tupla)

# Ejercicio 12:
print(f"Ejercicio 12: Primero = {tupla[0]}, Último = {tupla[-1]}")

# Ejercicio 13:
print("Ejercicio 13: El 20 aparece", tupla.count(20), "veces")

# Ejercicio 14:
lista_desde_tupla = list(tupla)
print("Ejercicio 14:", lista_desde_tupla)

# Ejercicio 15:
nombres = ("Pepe", "Manolo", "Pancracio", "Juan")
print("Ejercicio 15: Longitud =", len(nombres))

# Ejercicio 16:
persona = {
    "Nombre": "Pechyplayer",
    "Edad": 37,
    "Ciudad": "Bogotá"
}
print("Ejercicio 16:", persona)

# Ejercicio 17:
print("Ejercicio 17: Valores =", list(persona.values()))

# Ejercicio 18:
persona["Profesion"] = "Influencer"
print("Ejercicio 18:", persona)

# Ejercicio 19:
persona["Edad"] = 23
print("Ejercicio 19:", persona)

# Ejercicio 20:
del persona["Ciudad"]
print("Ejercicio 20:", persona)

# Ejercicio 21:
estudiantes = {"LLinais": 4.5, "Marilitriza": 3.8, "Parra": 4.2}
promedio_grupo = sum(estudiantes.values()) / len(estudiantes)
print(f"Ejercicio 21: Promedio del grupo = {promedio_grupo:.2f}")

# Ejercicio 22:
personas = [("LLinais", 20), ("Marilitriza", 15), ("Parra", 18), ("Fanniluh", 12)]
mayores = [nombre for nombre, edad in personas if edad >= 18]
print("Ejercicio 22: Mayores de edad =", mayores)

# Ejercicio 23:
notas_alumnos = {
    "LLinais": [4.5, 4.0, 5.0],
    "Marilitriza": [3.0, 3.5, 4.0],
    "Parra": [5.0, 4.8, 4.2]
}
print("Ejercicio 23:")
for nombre, notas in notas_alumnos.items():
    prom = sum(notas) / len(notas)
    print(f"  {nombre}: {prom:.2f}")

# Ejercicio 24:
db_estudiantes = [
    {"nombre": "Edilberto", "edad": 20, "carrera": "Vendedor de Vive100"},
    {"nombre": "Yunilutrixis", "edad": 22, "carrera": "TikToker"},
    {"nombre": "Patroclo", "edad": 21, "carrera": "Medicina"}
]
print("Ejercicio 24:")
for est in db_estudiantes:
    print(f"  Nombre: {est['nombre']}, Edad: {est['edad']}, Carrera: {est['carrera']}")

# Ejercicio 25:
tienda = {}
tienda["Supercoco"] = 1.5
tienda["Pan"] = 2.0
tienda["Suero Costeño"] = 1.2
print("Ejercicio 25 - Catálogo:", tienda)
buscar_p = "Pan"
if buscar_p in tienda:
    print(f"  {buscar_p} encontrado. Precio: ${tienda[buscar_p]}")
else:
    print(f"  {buscar_p} no está en la tienda.")

#¿Qué diferencia hay entre lista y tupla?
#Las listas son mutables (se pueden modificar, agregar o eliminar elementos con .append(), .remove(), etc.), mientras que las tuplas son inmutables (no se pueden alterar una vez creadas).

#¿Cuándo es mejor usar diccionarios?
#Cuando necesitas asociar información mediante claves explícitas (pares clave-valor) para acceder a los datos rápidamente por su nombre en lugar de por una posición numérica (índice).

#¿Qué estructura te pareció más útil?
#El diccionario, por su flexibilidad para estructurar datos complejos (como perfiles de usuario o registros tipo base de datos).

lista_bonus = []

while True:
    print("\n MENÚ")
    print("1. Agregar elemento")
    print("2. Mostrar lista")
    print("3. Eliminar elemento")
    print("4. Salir")
    
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        elem = input("Ingresa el elemento a agregar: ")
        lista_bonus.append(elem)
        print(f"'{elem}' agregado correctamente.")
    elif opcion == "2":
        print("Lista actual:", lista_bonus)
    elif opcion == "3":
        elem = input("Ingresa el elemento a eliminar: ")
        if elem in lista_bonus:
            lista_bonus.remove(elem)
            print(f"'{elem}' eliminado.")
        else:
            print("El elemento no existe en la lista.")
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")