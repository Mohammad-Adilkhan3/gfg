#User function Template for python3


class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        ##Your code here
        x=bin(N)
        cnt=0
        res=0
        for i in x:
            if i=='1':
                cnt+=1
            else:
                cnt=0
            res=max(cnt,res)
        return res
            





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math





def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        obj = Solution()
        print(obj.maxConsecutiveOnes(n))
        T-=1

        print("~")
if __name__=="__main__":
    main()
# } Driver Code Ends