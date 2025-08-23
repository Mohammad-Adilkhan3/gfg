class Solution {
  public:
      bool isPossible(vector<int>& arr, int k, int maxPages) {
    int totalStudents = 1, currentSum = 0;
    
    for (int pages : arr) {
        currentSum += pages;
        if (currentSum > maxPages) {
            totalStudents++;
            currentSum = pages;  
        }
    }
    return totalStudents <= k;
}

    int findPages(vector<int> &arr, int k) {
        // code here
        if (k > arr.size()) return -1;  
    
    int beg = 0, end = 0;
    for (int pages : arr) {
        beg = max(beg, pages);  
        end += pages;           
    }
    
    int ans = beg;
    while (beg <= end) {
        int mid = (beg + end) / 2;
        if (isPossible(arr, k, mid)) {
            ans = mid;
            end = mid - 1;  
        } else {
            beg = mid + 1; 
        }
    }
    return ans;
    }
};
