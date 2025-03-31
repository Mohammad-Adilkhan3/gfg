class Solution:
    def maxPartitions(self , s):
        # code here
        last_occurrence = {char: i for i, char in enumerate(s)}  # Store last occurrence of each character
        count = 0
        start, end = 0, 0
    
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])  # Extend end to the farthest occurrence of seen characters
            if i == end:  # Found a valid partition
                count += 1
                start = i + 1  # Move start to the next partition
    
        return count


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends