#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        arr.sort()
        
    
        low = 0
        high = len(arr) - 1
        ceil = -1  
        floor = -1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ceil = arr[mid] 
                high = mid - 1   
            else:
                low = mid + 1    
        low = 0
        high = len(arr) - 1

    
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                floor = arr[mid]  
                low = mid + 1     
            else:
                high = mid - 1    

        return [floor, ceil]
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.getFloorAndCeil(x, arr)
        print(ans[0], ans[1])
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends