def thirdLargest(self,a, n):
        # code here
        x=sorted(a)
        if n>2:
            return x[-3]
        else:
            return -1
