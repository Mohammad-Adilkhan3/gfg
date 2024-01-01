def canPair(nums, k):
    if len(nums) % 2 != 0:
        return False

    remainder_count = {}
    
    for num in nums:
        remainder = num % k
        if remainder in remainder_count:
            remainder_count[remainder] += 1
        else:
            remainder_count[remainder] = 1

    for remainder, count in remainder_count.items():
        if remainder == 0:
            if count % 2 != 0:
                return False
        elif k - remainder in remainder_count:
            if remainder_count[remainder] != remainder_count[k - remainder]:
                return False
        else:
            return False

    return True

# Example usage:
nums1 = [9, 5, 7, 3]
k1 = 6
result1 = canPair(nums1, k1)
print("Example 1:", result1)

nums2 = [4, 4, 4]
k2 = 4
result2 = canPair(nums2, k2)
print("Example 2:", result2)
