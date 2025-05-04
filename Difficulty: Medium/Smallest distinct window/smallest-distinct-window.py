#User function Template for python3

class Solution:
    def findSubString(self, s):
        # code here
        from collections import Counter, defaultdict

        # Step 1: Identify total unique characters
        unique_chars = set(s)
        required = len(unique_chars)
        
        char_count = defaultdict(int)
        formed = 0  # number of unique characters in current window with at least 1 count
    
        left = 0
        min_len = float('inf')
    
        for right in range(len(s)):
            char_count[s[right]] += 1
            if char_count[s[right]] == 1:  # new unique char added to window
                formed += 1
    
            # Try to shrink window from the left
            while formed == required:
                min_len = min(min_len, right - left + 1)
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    formed -= 1
                left += 1
    
        return min_len
            
        
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):
        str = input()
        ob = Solution()
        print(ob.findSubString(str))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends