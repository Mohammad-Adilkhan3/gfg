def findTwoElement( self,arr): 
        # code here
        n = len(arr)
        repeating = missing = -1
        for i in range(n):
            element = abs(arr[i])
            
            if arr[element - 1] < 0:
                repeating = element
            else:
                arr[element - 1] = -arr[element - 1]
        
        for i in range(n):
            if arr[i] > 0:
                missing = i + 1
                break
        
        return repeating, missing
