vector<long long int> productExceptSelf(vector<long long int>& nums, int n) {
       
        //code here   
        vector<long long int> v;

        long long product=1;
        long long left=0;
        long long i=0;

        while(i<n && left<n){
            if(left!=i)  product*=nums[i];
         
          if(i==n-1){
              left++;
              i=0;
              v.push_back(product);
              product=1;
          }
          else{
                 i++;
          }
        }
        return v;        
    }
