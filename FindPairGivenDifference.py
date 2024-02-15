def findPair(self, arr, L,N):
        #code here
        arr.sort();i=0;j=1
        while j<L:
            if j>i and arr[j]-arr[i]==N:
                return True
            elif arr[j]-arr[i]>N:
                i+=1
            else:
                j+=1
        return False
