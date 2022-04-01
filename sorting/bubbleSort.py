def bubbleSorting(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


value = [-2, 45, 0, 11, -9]
bubbleSorting(value)

print("Sorted")
print(value)
