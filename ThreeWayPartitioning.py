def threeWayPartition(array, a, b):
    n = len(array)
    low, mid, high = 0, 0, n - 1
    
    while mid <= high:
        if array[mid] < a:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
        elif array[mid] > b:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
        else:
            mid += 1
    
    return 1

# Example usage:
array1 = [1, 2, 3, 3, 4]
a1, b1 = 1, 2

array2 = [1, 4, 3, 6, 2, 1]
a2, b2 = 1, 3

threeWayPartition(array1, a1, b1)
threeWayPartition(array2, a2, b2)

print("Modified array 1:", array1)
print("Modified array 2:", array2)
