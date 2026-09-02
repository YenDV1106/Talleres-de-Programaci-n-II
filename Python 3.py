x = 5
y = 3
print (x + y)
print (x - y)
print (x * y)
print (x / y)
print (x % y)
print (x ** y)
print (x // y)
print (x == y)
print (x != y)
print (x > y)
print (x < y)
print (x >= y)
print (x <= y)

x=5
print (x>3 and x<10)
print (x>3 or x<4)
print (not(x>3 and x<10))

x = ["manzana" , "Limon"]
y = ["manzana" , "Limon"]
z = x
print (x is z)
print (x is y)
print (x == y)

x = ["manzana", "Limon"]
print ("manzana" in x)

x = ["manzana", "Limon"]
print ("pera" not in x)

x = abs (-7.25)
print (x)

x = pow (4, 3)
print (x)

import math
x = math.sqrt(64)
print (x)

import math
x = math.ceil(14.23)
y = math.floor(5.12)
print (x)
print (y)

print (2 + 3 * 6//2)
print ((4 + 6) // (2 + 3))
print ((4 // 2) ** 5)
print ((4 // 2) ** (5 + 1))
print ((-3) ** 2)
print ((-3 ** 2))

#Actividad
#Parte 1
print(2 + 3 + 1 + 2)  # Resultado: 8 (int)
print(2 + 3 * 1 + 2)  # Resultado: 7 (int)
print((2 + 3) * 1 + 2)  # Resultado: 7 (int)
print((2 + 3) * (1 + 2))  # Resultado: 15 (int)
print(+---6)  # Resultado: -6 (int)
print(-+-+6)  # Resultado: 6 (int)

# Parte 2
print(1 / 2 / 4.0)  # Resultado: 0.125 (float)
print(1 / 2.0 / 4.0)  # Resultado: 0.125 (float)
print(1 / 2.0 / 4)  # Resultado: 0.125 (float)
print(1.0 / 2 / 4)  # Resultado: 0.125 (float)
print(4**.5)  # Resultado: 2.0 (float)
print(4.0 ** (1 / 2))  # Resultado: 2.0 (float)
print(4.0 ** (1 / 2) + 1 / 2)  # Resultado: 2.5 (float)
print(4.0 ** (1.0 / 2) + 1 / 2.0)  # Resultado: 2.5 (float)
print(3e3 / 10)  # Resultado: 300.0 (float)
print(10 / 5e-3)  # Resultado: 2000.0 (float)
print(10 / 5e-3 + 1)  # Resultado: 2001.0 (float)
print(3 / 2 + 1)  # Resultado: 2.5 (float)