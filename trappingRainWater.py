def trappingWater(self, arr,n):
        #Code here
        arr1=[0]*n

        arr2=[]

        k=0

        maxi=float('-inf')

        for i in range(n-1,-1,-1):

            maxi=max(maxi,arr[i])

            arr1[n-1-k]=maxi

            k+=1    

        max2=float('-inf')   

        for i in range(n):

            max2=max(max2,arr[i])

            arr2.append(max2)
        newid=0
        for i in range(n):

            wid=min(arr2[i],arr1[i])

            width=wid-arr[i]

            newid+=width
        return newid
