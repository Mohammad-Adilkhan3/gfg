from collections import defaultdict
class Solution:

    def maxCharGap(self, s: str) -> int:
        # code here
        if len(s)==len(set(s)):return -1
        d=dict()
        res=0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=i
            else:
                res=max(res,abs(d[s[i]]-i+1))
        return res
        
