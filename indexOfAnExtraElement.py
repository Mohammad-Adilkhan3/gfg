def findExtra(arr1, arr2, n):
    left, right = 0, n - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Compare elements at mid in both arrays
        if mid < n - 1 and arr1[mid] == arr2[mid]:
            left = mid + 1
        else:
            right = mid
    
    return left

# Example usage:
n = 7
arr1 = [2, 4, 6, 8, 9, 10, 12]
arr2 = [2, 4, 6, 8, 10, 12]
print(findExtra(arr1, arr2, n))  # Output: 4

n = 6
arr1 = [3, 5, 7, 8, 11, 13]
arr2 = [3, 5, 7, 11, 13]
print(findExtra(arr1, arr2, n))  # Output: 3
