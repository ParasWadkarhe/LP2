def selection_sort(arr, order='asc'):
    n = len(arr)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if (order == 'asc' and arr[j] < arr[idx]) or (order == 'desc' and arr[j] > arr[idx]):
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr

# User input
arr = list(map(int, input("Enter numbers separated by space: ").split()))
order = input("Enter sorting order (asc/desc): ").strip().lower()

# Sort and display result
sorted_arr = selection_sort(arr, order)
print("Sorted array:", sorted_arr)


# Enter numbers separated by space: 64 25 12 22 11
# Enter sorting order (asc/desc): desc
# Sorted array: [64, 25, 22, 12, 11]
