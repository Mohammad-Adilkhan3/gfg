#User function Template for python3

class Solution:
    def minValue(self, arr1, arr2):
        #code here
        arr1.sort(reverse=True)
        arr2.sort()
        ans=[a*b for a,b in zip(arr1,arr2)]
        
        return sum(ans)
