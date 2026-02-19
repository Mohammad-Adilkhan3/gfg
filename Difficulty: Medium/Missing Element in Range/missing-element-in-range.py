class Solution:
    def missingRange(self, arr, low, high):
        #code here
        arr_set = set(arr) #Convert list to set for O(1) lookup
        result = []
        
        for num in range (low, high + 1):
            if num not in arr_set:
                result.append(num)
                
        return result