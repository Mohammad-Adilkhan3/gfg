class Solution {
  public:
    // k is the maximum number of zeros allowed to flip
    int maxOnes(vector<int>& arr, int k) {
        // code here
        int res = 0;
    int start = 0, end = 0; 
    int cnt = 0;
    while (end < arr.size()) {
        if (arr[end] == 0)
            cnt++;
        while (cnt > k) {
            if (arr[start] == 0)
                cnt--;
            start++;
        }
        res = max(res, (end - start + 1));
        end++; 
    }
    return res; 
    }
};

