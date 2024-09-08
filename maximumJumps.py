def minJumps(arr):
    n = len(arr)
    
    # If array size is 1, no jump is needed.
    if n == 1:
        return 0
    
    # If the first element is 0, we can't move anywhere.
    if arr[0] == 0:
        return -1
    
    # maxReach keeps track of the farthest point we can reach
    maxReach = arr[0]
    
    # step keeps track of the number of steps we can take before we need to jump
    step = arr[0]
    
    # jump stores the number of jumps we have made
    jumps = 1
    
    # Traverse the array from the second element
    for i in range(1, n):
        # If we have reached the last element
        if i == n - 1:
            return jumps
        
        # Updating maxReach
        maxReach = max(maxReach, i + arr[i])
        
        # We use a step to get to the current index
        step -= 1
        
        # If no more steps are left
        if step == 0:
            # We must jump to continue
            jumps += 1
            
            # Check if the current index is beyond the maximum reach
            if i >= maxReach:
                return -1
            
            # Re-initialize the steps to the amount of steps to reach maxReach from position i
            step = maxReach - i
    
    return -1  # If we exit the loop, it means we can't reach the end

# Example usage:
arr1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr2 = [1, 4, 3, 2, 6, 7]
arr3 = [0, 10, 20]

print(minJumps(arr1))  # Output: 3
print(minJumps(arr2))  # Output: 2
print(minJumps(arr3))  # Output: -1
