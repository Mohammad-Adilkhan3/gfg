//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

string utility(int number) {

    // write your code here
    switch(number){
        case 1:return "One";break;
        case 2: return "Two";break;
        case 3: return "Three";break;
        case 4: return "Four";break;
        case 5: return "Five";break;
        case 6: return "Six";break;
        case 7: return "Seven";break;
        case 8: return "Eight";break;
        case 9: return "Nine";break;
        default: return "Unknown";break;
    }
}


//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    while (t--) {
        int number;
        cin >> number;
        cout << utility(number) << endl;
    }
}
// } Driver Code Ends