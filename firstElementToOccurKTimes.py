def firstElementKTime(a, n, k):
    count_dict = {}  # Dictionary to store the count of each element

    for i in range(n):
        if a[i] in count_dict:
            count_dict[a[i]] += 1
        else:
            count_dict[a[i]] = 1

        if count_dict[a[i]] == k:
            return a[i]

    return -1  # No element occurs at least k times

# Example usage:
arr1 = [1, 7, 4, 3, 4, 8, 7]
n1 = len(arr1)
k1 = 2
print(firstElementKTime(arr1, n1, k1))  # Output: 4

arr2 = [3, 1, 3, 4, 5, 1, 3, 3, 5, 4]
n2 = len(arr2)
k2 = 3
print(firstElementKTime(arr2, n2, k2))  # Output: 3
