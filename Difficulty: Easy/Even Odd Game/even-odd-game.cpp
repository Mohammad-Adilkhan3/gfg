//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

string utility(int n) {

    // write your code here
    if (n%2!=0) {return "You"; } else {return "Friend";}
}


//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    while (t--) {
        int number;
        cin >> number;
        cout << utility(number);
        cout << endl;

        cout << "~"
             << "\n";
    }
}
// } Driver Code Ends