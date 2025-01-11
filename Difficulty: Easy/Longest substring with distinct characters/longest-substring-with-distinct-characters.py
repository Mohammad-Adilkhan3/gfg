#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        n = len(s)
        char_set = set()
        max_length = 0
        left = 0
    
        for right in range(n):
            # If character at right is already in the set, remove from left until it's not
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character to the set and update max length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends