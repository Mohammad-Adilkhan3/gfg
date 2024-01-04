def singleElement(arr, N):
    ones = 0
    twos = 0

    for i in range(N):
        twos = twos | (ones & arr[i])
        ones = ones ^ arr[i]
        common_bit_mask = ~(ones & twos)
        ones &= common_bit_mask
        twos &= common_bit_mask

    return ones

# Example usage:
arr1 = [1, 10, 1, 1]
N1 = 4
result1 = singleElement(arr1, N1)
print("Example 1:", result1)

arr2 = [3, 2, 1, 34, 34, 1, 2, 34, 2, 1]
N2 = 10
result2 = singleElement(arr2, N2)
print("Example 2:", result2)
