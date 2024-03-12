int Maximize(int arr[], int n)
    {
        // Complete the function
        Arrays.sort(arr);
        long ans =0;
        
        for(int i =0 ;i<n;i++){
            ans = (ans+(long)arr[i]*i)%1000000007 ;
        }
        return (int)ans;
        
    }   
