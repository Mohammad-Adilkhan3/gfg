def game_with_number(arr, n):
    for i in range(n - 1):
        arr[i] = arr[i] | arr[i + 1]
    return arr

# Example usage:
arr1 = [10, 11, 1, 2, 3]
n1 = 5
print(game_with_number(arr1, n1))
# Output: [11, 11, 3, 3, 3]

arr2 = [5, 9, 2, 6]
n2 = 4
print(game_with_number(arr2, n2))
# Output: [13, 11, 6, 6]
