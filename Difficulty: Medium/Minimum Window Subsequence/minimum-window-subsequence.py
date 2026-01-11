class Solution:
    def minWindow(self, s1, s2):
        # Code here
        n, m = len(s1), len(s2)
        min_len = float('inf')
        start = -1
        i = 0
        while i < n:
            j = 0
            while i < n:
                if s1[i] == s2[j]:
                    j += 1
                    if j == m:
                        break
                i += 1
            if j < m:
                break
            end = i
            j = m - 1
            while i >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                    if j < 0:
                        break
                i -= 1
            if end - i + 1 < min_len:
                min_len = end - i + 1
                start = i
            i += 1  # move forward for next window search

        return "" if start == -1 else s1[start:start + min_len]
                    