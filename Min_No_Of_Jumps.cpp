int minJumps(int arr[], int n){
        // Your code here
        int maxi=0;
       int maxrange=0;
       int jump=0;
       if(n==1){
           return 0;
       }
       if(arr[0]==0){
           return -1;
       }
       for(int i=0;i<n;i++){
           maxi=max(maxi,i+arr[i]);
           if(maxrange==i){
               maxrange=maxi;
               jump++;
               if(maxrange>=n-1){
                   return jump;
               }
           }
       }
       return -1;
    }
