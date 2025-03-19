//{ Driver Code Starts
// Initial Template for C

#include <stdio.h>


// } Driver Code Ends

// User function Template for C

int nthDay(int d, int n) {

    // write your code here
     int ans = d - (n%7);
    return ans>=0?ans:(7+ans);
}


//{ Driver Code Starts.

int main() {

    int t;
    scanf("%d", &t);
    while (t-- > 0) {
        int d, n;
        scanf("%d %d", &d, &n);
        printf("%d", nthDay(d, n));
        printf("\n");
    }
}
// } Driver Code Ends