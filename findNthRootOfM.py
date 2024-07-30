	def NthRoot(self, n, m):
		# Code here
		if m ==1:      
            return 1
        low =1        
        high= m
        
        while low <= high:
            mid = (low + high) // 2
            mid_pow= mid** n
            
            if mid_pow == m:
                return mid
            elif mid_pow > m:
                high = mid - 1
            else:
                low = mid +1
                
        return -1
