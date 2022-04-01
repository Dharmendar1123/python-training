def insertionSorting(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > key:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            j = j - 1


values = [-2, 45, 0, 11, -9]
insertionSorting(values)

print("Sorted")
print(values)
