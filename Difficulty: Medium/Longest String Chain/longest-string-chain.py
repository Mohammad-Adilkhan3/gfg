#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def longestStringChain(self, words):
        # Code here
        words.sort(key=len)
        # Step 2: Dictionary to store the longest chain ending at each word
        dp = {}
        res = 1  # At least one word exists
    
        # Step 3: Build the chain
        for word in words:
            dp[word] = 1  # Default value
            # Try removing one character at a time to check for predecessor
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]  # Remove character at index i
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            # Step 4: Update max chain length found
            res = max(res, dp[word])
        return res



#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        words = input().split()
        ob = Solution()
        res = ob.longestStringChain(words)
        print(res)
        print("~")
# } Driver Code Ends