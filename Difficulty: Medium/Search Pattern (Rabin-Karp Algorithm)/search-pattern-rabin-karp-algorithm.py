class Solution:
    def compute_lps(self,pattern):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
    
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search(self, pattern, text):
        # code here
        lps = self.compute_lps(pattern)
        result = []
    
        i = j = 0  # i -> text, j -> pattern
    
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
    
            if j == len(pattern):
                result.append(i - j + 1)  # 1-based index
                j = lps[j - 1]
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return result
                