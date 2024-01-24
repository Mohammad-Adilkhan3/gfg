def nthFibonacci(self, n : int) -> int:
        # code here
        a=0
        b=1
        mod=1000000007
        for i in range(1,n):
            c=(a+b)%mod
            a=b
            b=c
            
        return c
        
