class Solution:
    def minDaysBloom(self, arr, k, m):
        # Code here
        n = len(arr)
        ans = -1
        s, e = 0, max(arr)

        while s <= e:
            mid = s + (e - s) // 2

            if self.check(arr, k, m, mid):
                ans = mid
                e = mid - 1
            else:
                s = mid + 1

        return ans
    def check(self, arr, k, m, mid):
        cnt = 0
        for num in arr:
            if num <= mid:
                cnt += 1
        return cnt >= m * k