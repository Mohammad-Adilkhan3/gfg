def frequencyCount(self, arr, N, P):
        # code here
        for i in range(N):
            arr[i]-=1
        for i in range(N):
            # Reduce the element by 1 to match 0-based indexing
            index = (arr[i] ) % P
            if index<N:
                arr[index] += P

        for i in range(N):
            # Calculate the frequency of each element
            arr[i] //= P
    
        return arr

