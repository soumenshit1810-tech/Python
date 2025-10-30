def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [10, 20, 30, 40, 50]
x = int(input("Enter element to search: "))
pos = binary_search(arr, x)

if pos != -1:
    print("Element found at index", pos)
else:
    print("Element not found")
