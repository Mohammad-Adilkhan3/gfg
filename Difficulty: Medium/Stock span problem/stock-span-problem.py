class Solution:
    def calculateSpan(self, arr):
        # code here
        n = len(arr)
        stack = []  
        res = [0] * n  
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if not stack:
                res[i] = i + 1
            else:
                res[i] = i - stack[-1]
            stack.append(i)
        
        return res
        
        