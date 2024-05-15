def find_median(self, v):
	    import math
		# Code here
		v.sort()
        t=((len(v)//2))
        S=len(v)
        if S%2==0:
            s=(v[t]+v[t-1])//2
            return s
        else:
            p=v[t]
            return p
