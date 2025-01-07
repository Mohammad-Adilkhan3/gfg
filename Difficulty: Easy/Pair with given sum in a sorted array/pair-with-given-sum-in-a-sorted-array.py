#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        n = len(arr)
        l, r = 0, n - 1
        count = 0
    
        while l < r:
            current_sum = arr[l] + arr[r]
            if current_sum == target:
                # Count duplicates for arr[l] and arr[r]
                if arr[l] == arr[r]:
                    freq = r - l + 1
                    count += (freq * (freq - 1)) // 2  # nC2 combinations
                    break  # No more pairs possible since all are the same
                else:
                    left_count, right_count = 1, 1
                    while l + 1 < r and arr[l] == arr[l + 1]:
                        left_count += 1
                        l += 1
                    while r - 1 > l and arr[r] == arr[r - 1]:
                        right_count += 1
                        r -= 1
                    count += left_count * right_count
                    l += 1
                    r -= 1
            elif current_sum < target:
                l += 1
            else:
                r -= 1
        
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends