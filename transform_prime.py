def minNumber(self, arr,n):
        # code here
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        array_sum = sum(arr)
        if is_prime(array_sum):
            return 0
        for i in range(1, array_sum):
            if is_prime(array_sum + i):
                return i
        return 1
n=int(input())
a=list(map(int,input().split()))
print(minNumber(a,n))
