class Solution:
	def maxProduct(self,arr):
		# code here
		n = len(arr)
        max_prod = arr[0]
        min_prod = arr[0]
        max_so_far = arr[0]
        for i in range(1, n):
            if arr[i] < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(arr[i], max_prod * arr[i])
            min_prod = min(arr[i], min_prod * arr[i])
            max_so_far = max(max_so_far, max_prod)
        return max_so_far