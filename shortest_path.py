def minimumStep (self, n):
        #complete the function here
        steps = 0
    
        while n>1:
            if n%3==0:
                n=n//3
            else:
                n-=1
            steps+=1
        
        return steps
n=int(input())
print(minimumStep(n))
