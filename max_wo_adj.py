def findMaxSum(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    # Initialize variables to store the maximum sum excluding and including the current element
    exclude = 0
    include = arr[0]

    # Iterate through the array starting from the second element
    for i in range(1, n):
        # Calculate the new values for excluding and including the current element
        new_exclude = max(exclude, include)  # Exclude the current element
        new_include = exclude + arr[i]        # Include the current element

        # Update the variables for the next iteration
        exclude, include = new_exclude, new_include

    # Return the maximum of the last iteration (maximum sum including or excluding the last element)
    return max(exclude, include)

# Example usage:
arr1 = [5, 5, 10, 100, 10, 5]
n1 = len(arr1)
print(findMaxSum(arr1, n1))  # Output: 110

arr2 = [3, 2, 7, 10]
n2 = len(arr2)
print(findMaxSum(arr2, n2))  # Output: 13
