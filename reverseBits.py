def reversedBits(x):
    result = 0
    
    # Iterate through 32 bits
    for _ in range(32):
        # Extract the least significant bit of x
        bit = x & 1
        
        # Shift the result to the left and append the extracted bit
        result = (result << 1) | bit
        
        # Shift x to the right to discard the least significant bit
        x >>= 1
    
    return result

# Example usage:
x1 = 1
x2 = 5

print("Reversed binary form of", x1, "in decimal:", reversedBits(x1))
print("Reversed binary form of", x2, "in decimal:", reversedBits(x2))
