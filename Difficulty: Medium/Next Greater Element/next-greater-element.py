# User function Template for python3
class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        n=len(arr)
        result=[-1]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while(stack and arr[i]>=arr[stack[-1]]):
                stack.pop()
            if stack:
                result[i]=arr[stack[-1]]
            else:
                result[i]=-1
            stack.append(i)
        return result

        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends