#Segundo Parcial
#Jen Jesus Leal Ruiz

MAX_VEHICULOS = 30
COLUMNAS = 6

PLACA = 0
PROPIETARIO = 1
CELULAR = 2
DIA_INGRESO = 3
DIA_SALIDA = 4
DIAS_DEMORA = 5

matriz = []

def leer_entero(mensaje, minimo, maximo):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            numero = int(valor)
            if numero >= minimo and numero <= maximo:
                return numero
        print("Dato no valido, debe ser un numero entre", minimo, "y", maximo)


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Este campo no puede quedar vacio")


def buscar_vehiculo(placa):
    for i in range(len(matriz)):
        if matriz[i][PLACA] == placa:
            return i
    return -1


def registrar_ingreso():
    if len(matriz) >= MAX_VEHICULOS:
        print("El taller ya tiene el maximo de", MAX_VEHICULOS, "vehiculos")
        return

    placa = leer_texto("Placa del vehiculo: ").upper()
    if buscar_vehiculo(placa) != -1:
        print("Ese vehiculo ya fue registrado este mes")
        return

    propietario = leer_texto("Nombre del propietario: ")
    celular = leer_texto("Numero de celular: ")
    dia_ingreso = leer_entero("Dia del mes en que ingreso (1-31): ", 1, 31)

    fila = [placa, propietario, celular, dia_ingreso, 0, 0]
    matriz.append(fila)
    print("Vehiculo registrado correctamente")


def registrar_salida():
    if len(matriz) == 0:
        print("Todavia no hay vehiculos registrados")
        return

    placa = leer_texto("Placa del vehiculo que sale: ").upper()
    posicion = buscar_vehiculo(placa)

    if posicion == -1:
        print("No existe un vehiculo con esa placa")
        return

    if matriz[posicion][DIA_SALIDA] != 0:
        print("Ese vehiculo ya tiene registrada su salida")
        return

    dia_ingreso = matriz[posicion][DIA_INGRESO]
    dia_salida = leer_entero("Dia del mes en que salio (1-31): ", dia_ingreso, 31)

    matriz[posicion][DIA_SALIDA] = dia_salida
    matriz[posicion][DIAS_DEMORA] = dia_salida - dia_ingreso
    print("Salida registrada, la reparacion demoro", matriz[posicion][DIAS_DEMORA], "dia(s)")


def reporte_terminados():
    print()
    print("===== VEHICULOS REPARADOS =====")
    terminados = 0

    for fila in matriz:
        if fila[DIA_SALIDA] != 0:
            terminados += 1
            print("Placa:", fila[PLACA], "| Dias en el taller:", fila[DIAS_DEMORA])

    if terminados == 0:
        print("Aun no hay vehiculos reparados")
    else:
        print("Total de vehiculos terminados:", terminados)


def reporte_ingresados():
    print()
    print("===== VEHICULOS INGRESADOS EN EL MES =====")

    if len(matriz) == 0:
        print("Aun no hay vehiculos registrados")
        return

    for fila in matriz:
        print("Placa:", fila[PLACA], "| Propietario:", fila[PROPIETARIO], "| Celular:", fila[CELULAR])
    print("Total de vehiculos ingresados:", len(matriz))


def mostrar_menu():
    print()
    print("======== Taller Mecanico el Yen ========")
    print("1. Registrar ingreso de un vehiculo")
    print("2. Registrar salida de un vehiculo")
    print("3. Reporte de vehiculos terminados")
    print("4. Reporte de todos los vehiculos ingresados")
    print("5. Cerrar la aplicacion")


def main():
    opcion = 0
    while opcion != 5:
        mostrar_menu()
        opcion = leer_entero("Elija una opcion: ", 1, 5)

        if opcion == 1:
            registrar_ingreso()
        elif opcion == 2:
            registrar_salida()
        elif opcion == 3:
            reporte_terminados()
        elif opcion == 4:
            reporte_ingresados()
        else:
            print("Cerrando la aplicacion...")

main()