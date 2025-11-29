class Solution:
    def countSetBits(self,n):
        # code here
        count = 0
        i = 0
        while (1 << i) <= n:
            next_power = 1 << (i + 1)
            half_power = 1 << i
            complete_blocks = (n + 1) // next_power
            count += complete_blocks * half_power
            remainder = (n + 1) % next_power
            count += max(0, remainder - half_power)
            i += 1
        return count
     