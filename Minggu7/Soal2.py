def quick_sort(arr, start, stop):
    if start < stop:
        pivotindex = partition_rand(arr, start, stop)
        quick_sort(arr, start, pivotindex-1)
        quick_sort(arr, pivotindex+1, stop)

def partition_rand(arr, start, stop):
    randpivot = (start + stop) // 2
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)

def partition(arr, start, stop):
    pivot = start
    i = start + 1
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[pivot], arr[i-1] = arr[i-1], arr[pivot]
    pivot = i - 1
    return pivot

arr = []
jumlah = int(input())
data = input().split()
for i in data:
    arr.append(int(i))
    
quick_sort(arr, 0, len(arr)-1)
for i in range(jumlah):
    print(f"Bebek ke-{i+1}: {arr[i]}")
