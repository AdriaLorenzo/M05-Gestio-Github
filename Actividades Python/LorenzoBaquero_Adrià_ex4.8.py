numero = int(input("Introduce el numero de elementos que quiere visualizar = "))

numero = numero - 2
i = 0
fibonacci = [0,1]
elemento = 0

while i < numero:
    elemento = fibonacci[i] + fibonacci[i+1]
    i = i + 1
    fibonacci.append(elemento)

for i in range (len (fibonacci)):
    print (fibonacci[i])

