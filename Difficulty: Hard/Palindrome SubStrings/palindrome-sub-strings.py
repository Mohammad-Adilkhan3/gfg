#User function Template for python3

class Solution:

    def countPS(self, s):
        # code here
        res, n = 0, len(s)
        for i in range(n):
            for left, right in [(i, i), (i, i + 1)]:  # Odd & Even length
                while left >= 0 and right < n and s[left] == s[right]:
                    if right - left + 1 >= 2:  # Count only length ≥ 2
                        res += 1
                    left -= 1
                    right += 1
        return res


