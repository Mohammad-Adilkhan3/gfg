//{ Driver Code Starts
// Initial function template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
      bool isPossible(vector<int>& arr, int k, int maxPages) {
    int totalStudents = 1, currentSum = 0;
    
    for (int pages : arr) {
        currentSum += pages;
        if (currentSum > maxPages) {
            totalStudents++;
            currentSum = pages;  // Start new allocation
        }
    }
    return totalStudents <= k;
}

    int findPages(vector<int> &arr, int k) {
        // code here
        if (k > arr.size()) return -1;  // If students are more than books
    
    int beg = 0, end = 0;
    for (int pages : arr) {
        beg = max(beg, pages);  // Maximum single page count
        end += pages;           // Sum of all pages
    }
    
    int ans = beg;
    while (beg <= end) {
        int mid = (beg + end) / 2;
        if (isPossible(arr, k, mid)) {
            ans = mid;
            end = mid - 1;  // Reduce the search space
        } else {
            beg = mid + 1;  // Increase the search space
        }
    }
    return ans;
    }
};

//{ Driver Code Starts.

int main() {
    int test_case;
    cin >> test_case;
    cin.ignore();
    while (test_case--) {

        int d;
        vector<int> arr, brr, crr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        getline(cin, input);
        ss.clear();
        ss.str(input);
        while (ss >> number) {
            crr.push_back(number);
        }
        d = crr[0];
        int n = arr.size();
        Solution ob;
        int ans = ob.findPages(arr, d);
        cout << ans << endl;

        cout << "~"
             << "\n";
    }
    return 0;
}
// } Driver Code Ends