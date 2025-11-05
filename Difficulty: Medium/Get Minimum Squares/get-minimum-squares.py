import math
class Solution:
	def minSquares(self, n):
		# Code here
		is_sq=lambda x:int(x**0.5)**2==x
		if is_sq(n):return 1
		while n%4==0: n//=4
		if n%8==7: return 4
		return 2 if any(is_sq(n- a*a)for a in range(1,math.isqrt(n)+1)) else 3
		