#User function Template for python3
class Solution:
    def multiplication (ob,A,B):
        # code here 
        return A*B;


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        A,B=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.multiplication(A,B))
        print("~")
# } Driver Code Ends