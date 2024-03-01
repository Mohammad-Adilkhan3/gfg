def peakElement(arr, n):
    left, right = 0, n - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[mid + 1]:
            # The peak element is in the left half, including mid
            right = mid
        else:
            # The peak element is in the right half, excluding mid
            left = mid + 1

    # At the end of the loop, left and right will be equal, and the peak element will be at that index
    return left

# Example usage:
arr1 = [1, 2, 3]
n1 = len(arr1)
print(peakElement(arr1, n1))  # Output: 2

arr2 = [1, 1, 1, 2, 1, 1, 1]
n2 = len(arr2)
print(peakElement(arr2, n2))  # Output: Any index among {0, 1, 3, 5, 6}
