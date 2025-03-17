def binarySearch(array, target):

    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            print(True)
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(False)
    return False
        

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 20, 34]
tt = 10
binarySearch(numbers, 34)
