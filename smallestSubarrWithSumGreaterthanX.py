def smallestSubWithSum(arr, n, x):
    min_length = n + 1
    start = 0
    end = 0
    curr_sum = 0
    
    while end < n:
        # Keep adding elements while the sum is smaller than or equal to x
        while curr_sum <= x and end < n:
            curr_sum += arr[end]
            end += 1
        
        # If the sum becomes greater than x, update the min_length
        while curr_sum > x and start < n:
            min_length = min(min_length, end - start)
            curr_sum -= arr[start]
            start += 1
    
    return min_length if min_length != n + 1 else 0

# Example usage:
arr1 = [1, 4, 45, 6, 0, 19]
x1 = 51
print(smallestSubWithSum(arr1, len(arr1), x1))  # Output: 3

arr2 = [1, 10, 5, 2, 7]
x2 = 9
print(smallestSubWithSum(arr2, len(arr2), x2))  # Output: 1
