def swapNibbles(n):
    # Ensure the input is within the byte range (0 to 255)
    assert 0 <= n <= 255
    
    # Extract left nibble (shift right by 4 bits)
    left_nibble = (n >> 4) & 0x0F
    
    # Extract right nibble (mask with 0x0F)
    right_nibble = n & 0x0F
    
    # Swap nibbles: right nibble shifted left by 4, left nibble stays in place
    result = (right_nibble << 4) | left_nibble
    
    return result

# Example usage
print(swapNibbles(100))  # Output: 70
print(swapNibbles(129))  # Output: 24
