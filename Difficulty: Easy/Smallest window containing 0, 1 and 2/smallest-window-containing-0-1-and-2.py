class Solution:
    def smallestSubstring(self, S):
        # code here
        n = len(S)
        count = [0, 0, 0]
        start = 0
        min_len = float('inf')
        found = False
    
        for end in range(n):
            count[int(S[end])] += 1
    
            while all(count):
                found = True
                min_len = min(min_len, end - start + 1)
                count[int(S[start])] -= 1
                start += 1
    
        return min_len if found else -1
