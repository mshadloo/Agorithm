def binarySearch(arr, element):
    l = 0
    r = len(arr) - 1
    while(l <= r):
        mid = ((l + r) // 2)
        if(arr[mid] == element):
            return mid
        if(arr[mid] < element):
            l = mid + 1
        else:
            r = mid - 1
    print(str(element) + ' is not in the given list')


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binarySearch(arr, 11))
