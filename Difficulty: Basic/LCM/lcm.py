#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
def LCM(a,b):
    # Your code here
    import math
    return math.lcm(a,b)


#{ 
 # Driver Code Starts.

t = int(input())
while(t>0):
    t-=1
    a,b = map(int,input().split())
    print(LCM(a,b)) 
    print("~")
# } Driver Code Ends