class Solution:
    def subarrayXor(self, arr, k):
        # code here
        prefix_xor = 0
        count = 0
        freq_map = {0: 1}  # To handle cases where the prefix XOR itself equals k
        for num in arr:
            prefix_xor ^= num
            # Check if prefix_xor ^ k exists in the hash map
            if prefix_xor ^ k in freq_map:
                count += freq_map[prefix_xor ^ k]
            # Update the frequency map
            freq_map[prefix_xor] = freq_map.get(prefix_xor, 0) + 1
        
        return count


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends