def insert(self, alist, index, n):
        #code here
        while index>0 and alist[index] < alist[index-1]:
            alist[index],alist[index-1]=alist[index-1],alist[index]
            index-=1
        #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        if n==1:
            return
        
        for i in range(n):
            self.insert(alist,i,n)
