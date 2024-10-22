#User function Template for python3

class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        n = len(arr)
        prefix_diff = {0: 1}  
        count_x = 0
        count_y = 0
        result = 0
        for num in arr:
            if num == x:
                count_x += 1
            if num == y:
                count_y += 1
            diff = count_x - count_y
            if diff in prefix_diff:
                result += prefix_diff[diff]
            if diff in prefix_diff:
                prefix_diff[diff] += 1
            else:
                prefix_diff[diff] = 1
        
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends