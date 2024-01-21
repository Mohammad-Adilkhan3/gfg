def hasArrayTwoCandidates(self,arr, n, x):
		# code here
		new_set=set()
		for i in range(n):
		    target=x-arr[i]
		    if target in new_set:
		        return True
	        new_set.add(arr[i])
	    return False
