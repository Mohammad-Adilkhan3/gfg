#User function Template for python3

class Solution:
    def longestUniqueSubstring(self, S):
        # code here
        ans = 0
        hash = {}
        i = 0
        j = 0  
        while i < len(S):
            
            if S[i] in hash and hash[S[i]] >= j:
                j = hash[S[i]] + 1
            hash[S[i]] = i
            ans = max(ans, i - j + 1)
            i += 1
        return ans

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        s = input().strip()  # Read the input string

        ob = Solution()
        print(ob.longestUniqueSubstring(s))  # Call the method
        print("~")  # Print the separator

# } Driver Code Ends