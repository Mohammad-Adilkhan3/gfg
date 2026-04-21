from math import gcd
class Solution:
	def minSteps(self, m, n, d):
		# Code here
		if d > max(m, n) or d % gcd(m, n) != 0:
            return -1
        
        def simulate(jug1, jug2, target):
            
            a, b = 0, 0          
            steps = 0
            
            limit = jug1 * jug2 + 10
            
            while a != target and b != target and steps <= limit:
                if a == 0:            
                    a = jug1
                    steps += 1
                elif b == jug2:       
                    b = 0
                    steps += 1
                else:                 
                    pour = min(a, jug2 - b)
                    a -= pour
                    b += pour
                    steps += 1
            
            return steps if (a == target or b == target) else float('inf')

        path1 = simulate(m, n, d)   # Fill m first, pour into n
        path2 = simulate(n, m, d)   # Fill n first, pour into m
        
        result = min(path1, path2)
        return result if result != float('inf') else -1