class Solution:
    def transpose(self, mat):
        # code here
        return [list(row) for row in zip(*mat)]
        