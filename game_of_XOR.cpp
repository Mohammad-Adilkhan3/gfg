int gameOfXor(int N , int A[]) {
        // code here
       int res=0,i;
        for(i=0;i<N;i++){
            int f=(i+1)*(N-i);
            if((f&1)==1) res=res^A[i];
        }
        return res;
    }
int main(){
int n,a;
cin>>n;
for(int i=0;i<n;i++){
cin>>a[i];
}
res=gameOfXor(n,a);
print(res)
