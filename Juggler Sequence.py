def jugglerSequence(n):
    sequence = [n]  # Initialize the sequence with the given number
    while n != 1:
        if n % 2 == 0:
            n = int(n ** 0.5)  # Calculate the square root for even numbers
        else:
            n = int(n ** 1.5)  # Calculate the cube root for odd numbers
        sequence.append(n)  # Append the next number to the sequence
    return sequence

# Test cases
print(jugglerSequence(9))  # Output: [9, 27, 140, 11, 36, 6, 2, 1]
print(jugglerSequence(6))  # Output: [6, 2, 1]
