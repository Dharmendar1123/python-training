def selectionSorting(arr):
    for i in range(len(arr)):
        min = arr[i]
        pos = i
        for j in range(i, len(arr) - 1):
            if arr[j + 1] < min:
                min = arr[j + 1]
                pos = j+1
        arr[pos] = arr[i]
        arr[i] = min


values = [-2, 45, 0, 11, -9]
selectionSorting(values)

print("Sorted")
print(values)
