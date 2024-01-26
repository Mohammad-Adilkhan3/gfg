 def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        
        # code here
        arr.sort(key=lambda x: x.value/x.weight, reverse=True)

        max_value = 0.0
    
        for item in arr:
            if W == 0:
                break
    
            weight_taken = min(item.weight, W)
            max_value += (item.value / item.weight) * weight_taken
    
            W -= weight_taken
    
        return max_value
