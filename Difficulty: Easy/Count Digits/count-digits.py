#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
def countDigits(n):
    # write a code number of digits of the number
    # return the answer
    return len(str(n))
    


#{ 
 # Driver Code Starts.

t = int(input())
while(t>0):
    t-=1
    n = int(input())
    print(countDigits(n))
    print("~")
# } Driver Code Ends