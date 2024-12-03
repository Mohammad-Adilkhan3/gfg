class Solution:
    def minChar(self, s):
        #Write your code here
        def computeLPS(pattern):
            lps = [0] * len(pattern)
            length, i = 0, 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
            return lps
    
        # Create the augmented string
        rev_s = s[::-1]
        augmented_string = s + "$" + rev_s
    
        # Compute the LPS array for the augmented string
        lps = computeLPS(augmented_string)
    
        # Minimum characters to add = length of s - length of longest palindromic suffix
        return len(s) - lps[-1]
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends