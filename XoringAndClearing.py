def calculateXOR(arr):
    n = len(arr)
    
    # Step 1: Calculate bitwise XOR of each element with its index
    for i in range(n):
        arr[i] ^= i
    
    # Step 2: Print the modified array
    print(*arr)
    
    # Step 3: Set all elements of the array to zero
    for i in range(n):
        arr[i] = 0
    
    # Step 4: Print the array after setting all elements to zero
    print(*arr)

# Example usage:
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [10, 20, 30, 40]

print("Output for Example 1:")
calculateXOR(arr1)

print("\nOutput for Example 2:")
calculateXOR(arr2)
#for gfg:
def printArr(self, n, arr):
        # printing array elements with spaces
        n = len(arr)

    def setToZero(self, n, arr):
        # setting all elements to zero
        for i in range(n):
            arr[i] = 0
        print(*arr)
        

    def xor1ToN(self, n, arr):
        # doing xor with indices
        for i in range(n):
            arr[i] ^= i
        print(*arr)
