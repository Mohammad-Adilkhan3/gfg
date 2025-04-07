class Solution:
    def rowWithMax1s(self, arr):
        # code here
        n,m=len(arr),len(arr[0])
        res=-1
        cnt=0
        for i in range(n):
            if 1 in arr[i] and arr[i].count(1)>cnt:
                cnt=arr[i].count(1)
                res=i
        return res
                
        


#{ 
 # Driver Code Starts
# Main execution starts here
if __name__ == "__main__":
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        input_line = input().strip()  # Read input matrix as string
        mat = eval(input_line)  # Convert string to matrix

        solution = Solution()
        result = solution.rowWithMax1s(mat)  # Get the row with the most 1s

        print(result)
        print("~")

# } Driver Code Ends