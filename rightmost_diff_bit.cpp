int posOfRightMostDiffBit(int m, int n)
    {
        // Your code here
        if(m==n){
            return -1;
        }
        int x=m^n;
        int p=1;
        while(x%2!=1){
            p++;
            x=x/2;
        }
        return p;
    }
int main(){
int m,n;
cin>>m>>n;
res=posOfRightMostDiffBit(m,n);
cout<<res;
