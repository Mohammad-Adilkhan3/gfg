#User function Template for python3
class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        total_sum = sum(arr)
    
        # If total sum is not divisible by 3, we cannot split the array into three equal parts
        if total_sum % 3 != 0:
            return [-1, -1]
        
        target = total_sum // 3
        n = len(arr)
        
        current_sum, count = 0, 0
        i, j = -1, -1
    
        # Traverse the array and look for parts with sum equal to target
        for k in range(n):
            current_sum += arr[k]
            
            if current_sum == target:
                count += 1
                current_sum = 0  # Reset for next part
                
                # Mark the first and second boundaries
                if count == 1:
                    i = k
                elif count == 2:
                    j = k
                    break  # We found both boundaries
    
        # Check if we found exactly 2 boundaries for splitting into three equal parts
        if count == 2 and sum(arr[j + 1:]) == target:
            return [i, j]
        
        return [-1, -1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if (result == [-1, -1]) or len(result) != 2:
            print("false")
        else:
            sum1 = sum2 = sum3 = 0
            for i in range(len(arr)):
                if i <= result[0]:
                    sum1 += arr[i]
                elif i <= result[1]:
                    sum2 += arr[i]
                else:
                    sum3 += arr[i]

            if sum1 == sum2 == sum3:
                print("true")
            else:
                print("false")
        print("~")

# } Driver Code Ends