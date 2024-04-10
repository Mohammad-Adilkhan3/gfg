def findSingle(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

# Example usage:
arr = [1, 2, 2, 3, 3, 4, 4]
print("The single person in the party is:", findSingle(arr))
