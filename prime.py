def isPrime (self, N):
        # code here
        if N<=1 or N%2==0 :
            return 0
        elif N==2 :
            return 1
        for i in range(3,int(N**0.5)+1,2):
            if N%2==0:
                return 0
        return 1
n=int(input())
print(isPrime(n))
