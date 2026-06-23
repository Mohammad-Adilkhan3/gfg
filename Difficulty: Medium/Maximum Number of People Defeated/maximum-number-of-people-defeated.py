class Solution:
    def maxPeopleDefeated(self, p):
        # code here
        i = 1
        while p>=i*i:
            p, i = p-i*i, i+1
        return i-1