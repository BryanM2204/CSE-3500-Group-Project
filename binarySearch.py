def binarySearch(arr, x):
    # set the pointers for the beginning and ending of the array
    low = 0
    high = len(arr) - 1

    # iterative method 
    while low <= high:
        
        # calculate the midpoint
        mid = low + (high - low) // 2

        # Check if target is present at mid
        if arr[mid] == x:
            return mid

        # If target value is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If target value is smaller, ignore right half
        else:
            high = mid - 1

    # not present
    return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 3

    result = binarySearch(arr, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")