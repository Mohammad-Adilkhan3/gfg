//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

int gcd(int a, int b) {
    // code here to calculate and return gcd of a and b
    int m=((a<b)?a:b);
    int res=1;
    for(int i=1; i<=m;i++){
        if(a%i==0 && b%i==0){
            res=i;
        }
    }
    return res;
}



//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;

    while (t--) {
        int A, B;
        cin >> A >> B;
        int ans = gcd(A, B);
        cout << ans << endl;

        cout << "~"
             << "\n";
    }
}
// } Driver Code Ends