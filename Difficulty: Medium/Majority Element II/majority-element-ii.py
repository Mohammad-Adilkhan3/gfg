class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n = len(arr)
        freq = {}  # Regular dictionary
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        result = []
        for num, count in freq.items():
            if count > n // 3:
                result.append(num)
        result.sort()
    
        return result 
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends