int isPrime(int N){
        // code here
         if (N <= 1) {
        return 0;
    }
    for (int i = 2; i <= sqrt(N); i++) {
        if (N % i == 0) {
            return 0;
        }
    }
    return 1;
    }
int main(){
int n;
cin>>n;
res=isPrime(n);
cout<<res;
