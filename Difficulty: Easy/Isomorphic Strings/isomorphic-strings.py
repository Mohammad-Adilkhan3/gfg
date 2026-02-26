class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        if len(s1)!=len(s2): return False
        return len(set(s1))==len(set(s2))==len(set(zip(s1,s2)))