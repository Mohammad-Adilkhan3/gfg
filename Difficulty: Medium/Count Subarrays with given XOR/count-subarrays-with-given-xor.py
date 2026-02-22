class Solution:
    def subarrayXor(self, arr, k):
        # code here
        prefix_xor=0
        cnt=0
        freq_map={0:1}
        for i in arr:
            prefix_xor ^= i
            if prefix_xor ^ k in freq_map:
                cnt+=freq_map[prefix_xor ^ k]
            freq_map[prefix_xor]=freq_map.get(prefix_xor,0)+1
        return cnt