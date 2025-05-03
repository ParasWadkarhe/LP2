def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  # Assume the current index has the smallest element
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:  # Greedily pick smaller element
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the smallest to front
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
