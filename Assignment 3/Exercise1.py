def binarySearch(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, target, low, mid - 1)
    else:
        return binarySearch(arr, target, mid + 1, high)

arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binarySearch(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found in array")
