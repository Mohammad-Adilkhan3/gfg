def setBits(self, N):
		# code here
		cnt = 0
        while(N>0):
            rem = N % 2
            if(rem == 1):
                cnt += 1
            N //= 2
        return cnt
