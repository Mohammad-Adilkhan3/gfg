def subArraySum(self,arr, tar):
        #Your code here
        prefix_sums = {}
        prefix_sum = 0
        count = 0
        prefix_sums[0] = 1
        for num in arr:
            prefix_sum += num
            if (prefix_sum - tar) in prefix_sums:
                count += prefix_sums[prefix_sum - tar]
            if prefix_sum in prefix_sums:
                prefix_sums[prefix_sum] += 1
            else:
                prefix_sums[prefix_sum] = 1
        return count
