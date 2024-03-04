def swapElements(self, arr, n):
	    #Code here
	    for i in range(n-1):
	        if i+2<n:
        	    t=arr[i]
        	    arr[i]=arr[i+2]
        	    arr[i+2]=t
    	return arr
	        
