def findNth(self,n):
        #code here
        result = 0
        base = 1
        while n > 0:
            result += (n % 9) * base
            n //= 9
            base *= 10
        return result
