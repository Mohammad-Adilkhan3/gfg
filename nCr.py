def nCr(self, n, r):
        # code here
        import math
        if(n<r):
            return 0
        if(n==r):
            return 1
        k=n-r
        n1=(math.factorial(n))
        r1=(math.factorial(r))
        nr=(math.factorial(k))
        k=(n1//(nr*r1))%(1000000007)
        return k
