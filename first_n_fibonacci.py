def printFibb(self,n):
        # your code here
        r=[]
        x=0
        y=1
        while n>0:
            x,y=y,x+y
            r.append(x)
            n-=1
        return r
n=int(input())
print(printFibb(n))
