def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def deretFibo(n):
    data = []
    for i in range(1, n + 1):
        data.append(Fibonacci(i))
    return data

inAngka = int(input())
print(*deretFibo(inAngka))