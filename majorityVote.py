def findMajority(self, nums):
        #Your Code goes here.
        n = len(nums)
        freq = {}  # Regular dictionary
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        result = []
        for num, count in freq.items():
            if count > n // 3:
                result.append(num)
    
        return result if result else [-1]
