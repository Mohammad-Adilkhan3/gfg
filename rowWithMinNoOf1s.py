def minRow(n, m, a):
    min_ones_count = float('inf')
    min_row_index = -1
    
    for i in range(n):
        ones_count = a[i].count(1)
        if ones_count < min_ones_count:
            min_ones_count = ones_count
            min_row_index = i + 1
    
    return min_row_index

# Example usage:
n1, m1 = 4, 4
a1 = [[1, 1, 1, 1],
      [1, 1, 0, 0], 
      [0, 0, 1, 1],
      [1, 1, 1, 1]]

n2, m2 = 3, 3
a2 = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

print("Minimum row index for Example 1:", minRow(n1, m1, a1))
print("Minimum row index for Example 2:", minRow(n2, m2, a2))
