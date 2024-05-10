def combinationSum2(arr, n, k):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, n):
            # Avoid duplicates by skipping identical elements
            if i > start and arr[i] == arr[i - 1]:
                continue
            backtrack(i + 1, target - arr[i], path + [arr[i]])
    
    arr.sort()  # Sort the array to ensure non-decreasing order
    result = []
    backtrack(0, k, [])
    return result

# Example usage:
# Example 1
n1 = 5
k1 = 7
arr1 = [1, 2, 3, 3, 5]
print(combinationSum2(arr1, n1, k1))  # Output: [[1, 3, 3], [2, 5]]

# Example 2
n2 = 6
k2 = 30
arr2 = [5, 10, 15, 20, 25, 30]
print(combinationSum2(arr2, n2, k2))  # Output: [[5, 10, 15], [5, 25], [10, 20], [30]]
