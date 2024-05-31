def binary_search(arr,x):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = (high+low)//2
        if mid < x:
            low = mid + 1
        elif mid > x:
            high = mid
        else:
            return arr[mid - 1]
    return 0

jenis = int(input())
banyak = [] #banyak hewan tiap jenis
for i in range(jenis):
    temp = int(input())
    banyak.append(temp)

data = [] #baris hewan
for i in range(len(banyak)):
    temp = i+1
    for j in range(banyak[i]):
        data.append(temp)

tanya = [] # pertanyaan jenis keberapa
banyak_tanya = int(input())
for i in range(banyak_tanya):
    temp = int(input())
    tanya.append(temp)

jawab = [] #jawaban
for i in tanya:
    jawab.append(binary_search(data,i))

for i in jawab:
    print(i)
