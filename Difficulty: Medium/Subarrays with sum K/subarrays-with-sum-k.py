class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        ps,cnt=0,0
        psm={0:1}
        for i in arr:
            ps+=i
            if ps-k in psm:
                cnt+=psm[ps-k]
            psm[ps]=psm.get(ps,0)+1
        return cnt