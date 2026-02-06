class Solution:
    def smallestDiff(self,a, b, c):
        #code here.
        a.sort()
        b.sort()
        c.sort()
        n=len(a)
        best_diff=float("inf")
        i=j=k=0
        while i<n and j<n and k<n:
            curr=[a[i],b[j],c[k]]
            M=max(curr)
            m=min(curr)
            diff=M-m
            if diff<best_diff:
                best_diff=diff
                res=curr
            if a[i]==m:i+=1
            elif b[j]==m:j+=1
            elif c[k]==m:k+=1
        return sorted(res)[::-1]
