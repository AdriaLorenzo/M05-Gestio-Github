import random
import time 

numaleatorio = random.randint(0, 100)

numero = -1


while numaleatorio != numero:
    
    tiempo1= time.time()
    numero = int (input('Introduce un numero entre (0-100) = '))

    if numaleatorio < numero:
        print ('El numero introducido es mas pequeño')
    
    elif numaleatorio > numero:
        print ('El numero introducido es mas grande')

tiempo2= time.time()

tiempo = tiempo2 - tiempo1
print ('El tiempo tardado es ' , tiempo)
