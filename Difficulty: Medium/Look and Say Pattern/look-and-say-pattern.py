class Solution:
    def countAndSay(self, n):
        # code here
        if n == 1:
            return "1"
    
        prev = "1"
        for _ in range(2, n + 1):
            next_seq = ""
            i = 0
            while i < len(prev):
                count = 1
                while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                    count += 1
                    i += 1
                next_seq += str(count) + prev[i]
                i += 1
            prev = next_seq
        return prev


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countAndSay(n))

        print("~")
# } Driver Code Ends