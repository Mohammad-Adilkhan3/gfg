def isAdditiveSequence(n):
    def isAdditive(num1, num2, remaining):
        if not remaining:
            return True
        sum_num = str(num1 + num2)
        if remaining.startswith(sum_num):
            return isAdditive(num2, int(sum_num), remaining[len(sum_num):])
        return False
    
    for i in range(1, len(n)):
        for j in range(i + 1, len(n)):
            num1 = int(n[:i])
            num2 = int(n[i:j])
            remaining = n[j:]
            if isAdditive(num1, num2, remaining):
                return True
    return False

# Test cases
print(isAdditiveSequence("1235813"))  # Output: True
print(isAdditiveSequence("11235815")) # Output: False
