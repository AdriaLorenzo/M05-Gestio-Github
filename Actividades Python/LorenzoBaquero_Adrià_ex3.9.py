a = float(input('Ingrese el coeficiente a = '))
b = float(input('Ingrese el coeficiente b = '))

if (a!=0):
    x = (-b / a)
    print ('El resultado es: ' , x)
elif ((a==0) & (b!=0)):
    print ('No existe solucion')
elif ((a == 0) & (b == 0)):
    print ('Existen infinitas soluciones')