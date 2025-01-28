#User function Template for python3

class Solution:
    def findPermutation(self, s):
        # Code here
        from itertools import permutations
        all_perms = permutations(s)
        # Use a set to filter out duplicates and convert back to a list of strings
        unique_perms = set("".join(p) for p in all_perms)
        # Return as a sorted list (optional, if order is desired)
        return list(unique_perms)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends