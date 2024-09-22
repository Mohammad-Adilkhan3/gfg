def sumOfDivisors(self, N):
    	#code here 
    	sum = 0
        for i in range(1,N+1,1):
            sum = sum + (N//i*i)
        return sum 
