//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

void swap(int &a, int &b) {
    // code here
    std::swap(a,b);
    
}



//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    while (t--) {
        int a, b;
        cin >> a >> b;

        swap(a, b);

        cout << a << " " << b << endl;

        cout << "~"
             << "\n";
    }
}
// } Driver Code Ends