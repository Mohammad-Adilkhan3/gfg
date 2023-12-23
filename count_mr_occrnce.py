def count_occurrence(arr, n, k):
    count_map = {}

    # Count occurrences of each element in the array
    for num in arr:
        count_map[num] = count_map.get(num, 0) + 1

    # Count elements with more than n/k occurrences
    count = 0
    threshold = n // k

    for key, value in count_map.items():
        if value > threshold:
            count += 1

    return count

# Example 1
N1 = 8
arr1 = [3, 1, 2, 2, 1, 2, 3, 3]
k1 = 4
print(count_occurrence(arr1, N1, k1))  # Output: 2

# Example 2
N2 = 4
arr2 = [2, 3, 3, 2]
k2 = 3
print(count_occurrence(arr2, N2, k2))  # Output: 2
