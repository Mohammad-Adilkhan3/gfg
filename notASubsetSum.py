def findSmallest(self, arr):
        # code here
        res=1
        for i in arr:
            if i>res:
                return res
            res+=i
        return res
