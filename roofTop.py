def maxStep(self, arr):
        #Your code here
        m=0
        cnt=0
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                cnt+=1
                
            else:
                cnt=0
            m=max(m,cnt)
        return m
