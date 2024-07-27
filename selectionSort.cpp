int select(int arr[], int i)
    {
        // code here such that selectionSort() sorts arr[]
        int k=arr[i];
        for(int j=i-1;j>-1;j--){
            if(arr[j]<k){
                return j+1;
            }
            else
            arr[j+1]=arr[j];
        }
        return 0;
    }
     
    void selectionSort(int arr[], int n)
    {
       //code here
        for(int i=1;i<n;i++){
            int temp=arr[i];
            int k=select(arr,i);
            arr[k]=temp;
        }
    }
