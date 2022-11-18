tamaño = float(input('Ingrese el tamaño de un tornillo = '))

if tamaño == 1 or tamaño < 3:
    print ('El tornillo es pequeño')
elif tamaño == 3 or tamaño < 5:
    print ('El tornillo es mediano')
elif tamaño == 5 or tamaño < 6.5:
    print ('El tornillo es grande')
elif tamaño == 6.5 or tamaño < 8.5:
    print ('El tornillo es muy grande')
else:
    print ('El tamaño no es correcto.')