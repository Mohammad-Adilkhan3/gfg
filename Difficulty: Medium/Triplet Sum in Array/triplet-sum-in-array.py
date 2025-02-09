#User function Template for python3
class Solution:
    # Function to find if there exists a triplet in the array arr[] which sums up to target.
    def hasTripletSum(self, arr, target):
        # Your Code Here
        arr.sort()
        n=len(arr)
        res=0
        for i in range(n):
            j=i+1
            k=n-1
            while j<k:
                res=arr[i]+arr[j]+arr[k]
                if res <target:
                    j+=1
                elif res>target:
                    k-=1
                else:
                    return True
        return False
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input().strip())  # Number of test cases
    while tc > 0:
        arr = list(map(int, input().strip().split()))  # Read array
        target = int(input().strip())  # Read the target sum
        ob = Solution()
        print("true"
              if ob.hasTripletSum(arr, target) else "false")  # Output result
        tc -= 1

# } Driver Code Ends