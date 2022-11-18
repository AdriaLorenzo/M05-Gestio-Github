
print ('Apartado A')

numero1 = float(input("Introduce el primer numero = "))
numero2 = float(input("Introduce el segundo entero = "))

if (numero2 > numero1):
    float(input("Introduce el segundo entero = "))

print ('\n Apartado B')

i = 0

numero1 = float(input("Introduce un numero = "))


while (i < 1):
    numero2 = float(input("Introduce un numero = "))
    if (numero1 > numero2):
        break
    else:
        numero1 = numero2

print ('\nApartado C')

limite = int (input ('Ingrese el limite = '))
suma = 0

while suma < limite:
    numero = int (input ('Ingrese el numero = '))
    suma = suma + numero

print ('\nApartado D')

for i in range (100, 999, 1):
    if (i % 7==0 and i % 5==0):
        print (i,' ')

print ('\nApartado E')

for i in range(1,9):
    for j in range(0,9):
        for k in range(0,9):
            if (i % 2==0) and (j % 2==0) and (k % 2==0):
                print(i,j,k)

print ('\nApartado F')

for i in range(1,9):
    for j in range(1,9):
        for k in range(1,9):
            if( i != k ) and (i != j) and (j != k):
                print(i,j,k)