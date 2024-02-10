def findFloor(self,A,N,X):
        #Your code here
        left = 0
        right = N - 1
        ans = -1
        while left <=right:
            mid = left + (right-left)//2
                
            if A[mid]>X:
                right = mid - 1
                    
            else:
                ans = mid
                left = mid + 1
    
        return ans
