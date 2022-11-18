primeracara = int(input('Ingresa la longitud de la primera cara = '))
segundacara = int(input('Ingresa la longitud de la segunda cara = '))
terceracara = int(input('Ingresa la longitud de la tercera cara = '))

if (primeracara==segundacara and segundacara==terceracara):
    print ('El triangulo es equilátero.')
elif primeracara==segundacara or segundacara==terceracara or primeracara==terceracara:
    print ('El triangulo es isósceles')
else:
    print ('El triangulo es escaleno')