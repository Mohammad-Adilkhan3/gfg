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
            
        


