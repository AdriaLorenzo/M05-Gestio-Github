i = 0
factorial = 1

while i <= 1:

    numero = float(input("Introduce un numero entero = "))

    # Indicamos que numeropantalla es igual a numero para poder imprimirlo en el print porque sino da el numero mal, ya que lo restamos.
    numeropantalla = numero

    if numero == 0 or numero == 20:
        print("El numero introducido es incorrecto.")
    # Hacemos un while unicamente para calcular el factorial, mientras que el numero introducido sea mayor que 1 nos funcionara, hasta 20 que es el maximo
    else:
        while numero > 0:
            factorial = factorial * numero
            numero = numero - 1
            i = i + 1
        print("El factorial de", numeropantalla, " es ", factorial)
