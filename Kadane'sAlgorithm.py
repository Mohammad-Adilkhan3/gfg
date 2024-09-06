def maxSubArraySum(self,arr):
        ##Your code here
        s = arr[0]
        cnt=0
        for i in range(len(arr)):
            cnt += arr[i]
            s = max(cnt, s)
            
            if cnt < 0:
                cnt = 0
        return s
