import math 

error = float (input ('Error maximo? = '))
while error <=0:
    error = float (input ('Error maximo? = '))

angulo = float (input ('Introduce un angulo = '))
while not (-180 <= angulo <= 180):
    angulo = float (input ('Introduce un angulo = '))

angulo = angulo * math.pi / 180

indice = 1
termino = angulo
sin = angulo

while math.fabs (termino) > error:
    indice = indice + 2
    termino = - termino * angulo * angulo / (indice-1)
    sin = sin

print (f'El sin de {angulo} rad es {sin}')