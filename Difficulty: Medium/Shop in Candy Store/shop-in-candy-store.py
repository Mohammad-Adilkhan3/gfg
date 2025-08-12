class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        n=len(prices)
        prices.sort()
        m,M,i,j=0,0,0,n-1
        while n>0:
            m+=prices[i]
            M+=prices[j]
            i+=1
            j-=1
            n-=k+1
        return [m,M]
        
        