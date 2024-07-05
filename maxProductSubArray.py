def maxProduct(self,arr, n):
		# code here
		ans = float('-inf')
        c=1
        t=1
        for i in range(0,len(arr)):
            c*=arr[i]
            t*=arr[len(arr)-1-i]
            
            if( c>ans):
                ans=c
            if(t>ans):
                ans=t
            if(c==0):
                c=1
            if(t==0):
                t=1
        return ans
