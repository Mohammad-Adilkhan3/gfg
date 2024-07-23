def findKRotation(self, arr):
        # code here
        n= len(arr)
        min = arr[0]
        index=0
        for i in range(0,n):
            if min > arr[i]:
                min = arr[i]
                index=i
        return index  
