def segregateElements(self, arr):
        # Your code goes here
        arr_neg = list()
        arr_pos = list()
        n = len(arr)
        
        for i in range(0, n):
            if (arr[i] < 0):
                arr_neg.append(arr[i])
            else:
                arr_pos.append(arr[i])
                
        
        for i in range(0, len(arr_pos)):
            arr[i] = arr_pos[i]
        for i in range(len(arr_pos), len(arr_pos)+len(arr_neg)):
            arr[i] = arr_neg[i-len(arr_pos)]
            
        return arr
