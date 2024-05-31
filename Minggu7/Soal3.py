def quicksortLen(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = []
    right = []
    for x in arr[:-1]:
        if len(x) <= len(pivot):
            left.append(x)
        else:
            right.append(x)
    return quicksortLen(left) + [pivot] + quicksortLen(right)

def quicksortAlphabet(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksortAlphabet(left) + middle + quicksortAlphabet(right)

inputNum = int(input())
data = []
for i in range (inputNum):
    data.append(input())

sortAlphabet = quicksortAlphabet(data)
sortLen = quicksortLen(sortAlphabet)

for i in sortLen:
    print(i)
