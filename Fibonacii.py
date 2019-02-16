print("Ingrese el numero de valores de la sucesion de Fibonacci que desea")
m=int(input())

def fib(n):
    a = 0
    b = 1
    for k in range(n):
        c = a+b
        a = b
        b = c
    return b
for x in range(m):
    print(fib(x))
