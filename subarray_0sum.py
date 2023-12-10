def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        ps = set()
        s = 0
        for num in arr:
            s += num
            if s == 0 or s in ps:
                return True
            ps.add(s)
        return False
n=int(input())
a=list(map(int,input().split()))
print(subArrayExists(a,n))
