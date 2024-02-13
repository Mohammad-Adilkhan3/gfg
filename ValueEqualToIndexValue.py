def valueEqualToIndex(self,arr, n):
		# code here
		ans=[]
        for i in range (0,n):
            if (arr[i]==i+1):
                ans.append(i+1)
                
        return ans
