#User function Template for python3

class Solution:
    def maxXor(self, nums):
        #code here
        trie = {}
        for num in nums:
            node = trie
            for i in range(31, -1, -1):
                node = node.setdefault((num >> i) & 1, {})
        
        max_xor = 0
        for num in nums:
            node = trie
            curr = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                opp = 1 - bit
                if opp in node:
                    curr |= (1 << i)
                    node = node[opp]
                else:
                    node = node[bit]
            max_xor = max(max_xor, curr)
        return max_xor


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxXor(arr))
        print("~")

# } Driver Code Ends