
class Solution:
    def longestPalindrome(self, s):
        # code here
        longest = ""
        for i in range(len(s)):
            for left, right in [(i, i), (i, i + 1)]:  # Odd and even length centers
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                if right - left - 1 > len(longest):  # Update longest palindrome
                    longest = s[left + 1:right]

        return longest


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
        print("~")
# } Driver Code Ends