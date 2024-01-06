def sumOfPowers(a, b):
    def prime_factors_count(n):
        count = 0
        while n % 2 == 0:
            count += 1
            n //= 2

        i = 3
        while i * i <= n:
            while n % i == 0:
                count += 1
                n //= i
            i += 2

        if n > 1:
            count += 1
        return count

    total_sum = 0
    for num in range(a, b + 1):
        total_sum += prime_factors_count(num)

    return total_sum

# Example usage:
a = 9
b = 12
result = sumOfPowers(a, b)
print("Output:", result)
