def kombinasi(angka, jumlah, temp=None):
    if temp is None:
        temp = []
    total = 0
    for num in temp:
        total += num
    if total == jumlah:
        for i in range(len(temp)):
            print(temp[i], end=' ')
        print()
    if total >= jumlah:
        return
    for i in range(len(angka)):
        n = int(angka[i])
        kombinasi(angka[i:], jumlah, temp + [n])

angka = input().split()
jumlah = int(input())
kombinasi(angka, jumlah)