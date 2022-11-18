correcto = 'iloveyou123'
i = 1

while i <=3:

    contra = input('Ingrese su contraseña = ')

    if (contra == correcto ):
        print('Enhorabuena! Su contraseña es correcta! Sus intentos fueron' , i)
        break
    else:
        print('Lo la contraseña insertada es incorrecta! Te quedan' , (3-i))
    i= i +1
        
if i==3:
    print ('Intentos agotados')
        
