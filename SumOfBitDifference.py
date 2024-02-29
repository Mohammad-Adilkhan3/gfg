def sumBitDifferences(arr, n):
    # Initialize result
    res = 0

    # Traverse over all bits
    for i in range(32):
        
        # Count number of elements
        # with i'th bit set
        count = 0
        for j in range(n):
            if ( (arr[j] & (1 << i)) ):
                count += 1

        # Add "count * (n - count) * 2"
        # to the answer
        res += (count * (n - count) * 2)

    return res

# Example usage:
arr1 = [1, 2]
n1 = len(arr1)
print(sumBitDifferences(arr1, n1))
# Output: 4

arr2 = [1, 3, 5]
n2 = len(arr2)
print(sumBitDifferences(arr2, n2))
# Output: 8
