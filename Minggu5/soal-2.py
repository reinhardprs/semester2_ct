def biner(n):
    if n == 0:
        return ''
    else:
        binary = n % 2
        return biner(n // 2) + str(binary)

inAngka = int(input())
print(biner(inAngka))
