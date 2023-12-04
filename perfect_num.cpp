#include<iostream>
using namepace std;
int isPerfectNumber(long long N) {
        // code here
        if(N==1) return 0;
        long sum=1;
        for(long i=2;i*i<=N;i++){
            if(N%i==0){
                sum+=i;
                if(i!=N/i) sum+=N/i;
            }
        }
        if(sum==N) return 1;
        else
        return 0;
    }
int main(){
long long n;
cin>>n;
cout<<(isPerfectNumber(n))
