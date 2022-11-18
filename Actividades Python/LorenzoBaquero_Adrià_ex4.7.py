latas = int (input('Introduce el numero de latas que quieres apilar = '))

apilable = 0
i = 1

while i <= latas:

    apilable = apilable + 1
    latas = latas - apilable
    i = i + 1

if (latas == 0 ):
    print ('El numero es apilable')
    
else:
    print ('El numero no es apilable')
