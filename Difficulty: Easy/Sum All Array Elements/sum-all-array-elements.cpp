//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++
#include<math.h>

int arraySum(int arr[], int size) {
    // Just return the sum of the list
    // Don't print here
    int res=0;
    for(int i=0;i<size;i++){
        res+=arr[i];
    }
    return res;
}


//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        int numbers[n];
        for (int i = 0; i < n; i++) {
            cin >> numbers[i];
        }
        cout << arraySum(numbers, n) << endl;

        cout << "~"
             << "\n";
    }

    return 0;
}
// } Driver Code Ends