def kthElement(self, k, arr1, arr2):
        res=arr1+arr2
        res.sort()
        return res[k-1]
        
