#User function Template for python3

class Solution:
    #User function Template for python3
    import bisect
    import math
    def print_divisors(self, n):
        # code here
        sn=[]
        ln=[]
        for i in range(1,int(n**0.5)+1):
            if n%i ==0:
                sn.append(i)
                if i != n//i:
                    ln.append(n//i)
        res=sn+ln[::-1]
        for d in res:
            print(d, end=' ')