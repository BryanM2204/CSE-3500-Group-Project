def ternarySearch(ar, key):
    # set pointers for beginning and ending of the array
    l = 0
    r = len(ar) - 1

    # iterative method
    while r >= l:

        # Find mid1 and mid2
        mid1 = l + (r-l) // 3
        mid2 = r - (r-l) // 3

        # Check if target value is at any mid
        if key == ar[mid1]:
            return mid1
        if key == ar[mid2]:
            return mid2

        # if the target value is less than the element at mid1
        if key < ar[mid1]:
            r = mid1 - 1

        # the target value is greater than the element at mid2
        elif key > ar[mid2]:
            l = mid2 + 1

        # else the target is in the segment between mid1 and mid2
        else:
            l = mid1 + 1
            r = mid2 - 1

    # target not found
    return -1


if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 5

    p = ternarySearch(ar, key)

    print("Index of", key, "is", p)
    

    # check for item not present in the array
    key = 50

    p = ternarySearch(ar, key)

    print("Index of", key, "is", p)

