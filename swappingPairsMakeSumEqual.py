def findSwapValues(a, n, b, m):
    SumA = sum(a)
    SumB = sum(b)
    
    # If the difference between sums is not even, return -1
    if (SumB - SumA) % 2 != 0:
        return -1
    
    # Calculate the target difference
    diff = (SumB - SumA) // 2
    
    # Convert array b to a set for O(1) lookups
    b_set = set(b)
    
    # Check for each element in array a
    for x in a:
        y = x + diff
        if y in b_set:
            return 1
    
    return -1

# Example usage:
n = 6
m = 4
a = [4, 1, 2, 1, 1, 2]
b = [3, 6, 3, 3]
print(findSwapValues(a, n, b, m))  # Output: 1

n = 4
m = 4
a = [5, 7, 4, 6]
b = [1, 2, 3, 8]
print(findSwapValues(a, n, b, m))  # Output: 1
