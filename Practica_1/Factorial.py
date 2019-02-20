print('Programa para conocer el factorial de un numero')
print('Ingrese el numero')
n=int(input())
factorial = 1
for i in range(n):
    factorial *= n
    n -= 1
print(factorial)
    
