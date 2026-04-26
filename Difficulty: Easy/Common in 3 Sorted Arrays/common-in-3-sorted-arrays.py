class Solution:
    def commonElements(self, a, b, c):
        # code here
        x,y,z=set(a),set(b),set(c)
        return sorted(list((x.intersection(y)).intersection(z)))