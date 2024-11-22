def linearSearch(arr, x):
    # Set N to length of array
    N = len(arr)

    # iterate through each element - checking to see if there's a match
    for i in range(0, N):
        if (arr[i] == x):
            return i
        
    # return -1 if not present
    return -1
    

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 9]
    target = 3

    print(linearSearch(arr, target))