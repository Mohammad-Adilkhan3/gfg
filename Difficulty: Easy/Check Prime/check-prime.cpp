//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

//User function Template for C++

bool prime(int n){
    
    //Write your code here
    //returns a boolean value 
    int cnt=0;
    for(int i=1;i<=n;i++){
        if (n%i==0) {cnt++;}
    }
    return cnt==2;
    
}


//{ Driver Code Starts.
    
int main() {
	
	int t; cin>>t;
	
	while(t--){
	    int n; cin>>n;
        bool ans = prime(n);
        if(ans)
            cout<<"True"<<endl;
        else
            cout<<"False"<<endl;
	
cout << "~" << "\n";
}
}
// } Driver Code Ends