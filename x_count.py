def countX(self,L,R,X):
        #code here
        count = 0

        for num in range(L + 1, R):
            count += str(num).count(str(X))
    
        return count
l,r,x=map(int,input().split())
print(countX(l,r,x))
