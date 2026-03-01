class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	index = 0 
        n=len(arr)
        for i in range(n):
            if arr[i] != 0:
                arr[i], arr[index] = arr[index], arr[i]
                index += 1