def maxPathSum(self, arr1, arr2):
        # Code here
        c1 = c2 = 0
        i, j = 0, 0
        while(i < len(arr1) and j < len(arr2)):
            if(arr1[i]<arr2[j]):
                c1+=arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                c2+=arr2[j]
                j += 1
            else:
                c1 = max(c1, c2) + arr1[i]
                c2 = c1
                i += 1
                j += 1
        while i < len(arr1):
            c1+=arr1[i]
            i += 1
        while j < len(arr2):
            c2+=arr2[j]
            j += 1
        return max(c1, c2)
                
        
