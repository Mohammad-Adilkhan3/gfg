#User function Template for python3

class Solution:
    def findStepKeyIndex(self, arr, k, x):
        # code here
        if x in arr: return arr.index(x)
        return -1



#{ 
 # Driver Code Starts
def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1

    sol = Solution()

    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        k, x = map(int, data[index:index + 2])
        index += 2
        ans = sol.findStepKeyIndex(arr, k, x)
        results.append(ans)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends