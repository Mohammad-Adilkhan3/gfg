class Solution:
	def countTriplet(self, arr):
		# code here
		lth=len(arr)
        arr.sort()
        res=0
        for c in range(lth-1,1,-1):
            tar=arr[c]
            left=0
            right=c-1
            while left<right:
                if arr[left]+arr[right]==tar:
                    res+=1
                    left+=1
                    right-=1
                elif arr[left]+arr[right]<tar:
                    left+=1
                else:
                    right-=1
        return res

