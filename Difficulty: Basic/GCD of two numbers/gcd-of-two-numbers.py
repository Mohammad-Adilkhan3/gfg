
class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        import math
        return math.gcd(a,b)



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.gcd(a, b)
        
        print(res)
        

        print("~")
# } Driver Code Ends