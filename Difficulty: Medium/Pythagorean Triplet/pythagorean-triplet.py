class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here
    	s=[x*x for x in arr]
        s.sort()
        sa=set(s)
        
        mx=max(sa)
        for i in sa:
            for j in sa:
                if i==j or i+j>mx:
                    continue
                if i+j in sa:
                    return True
        return False