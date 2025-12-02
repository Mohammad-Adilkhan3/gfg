def pair_sum(arr, sum):
    # code here
    for i in range(len(arr)):
        if sum-arr[i] in arr[i+1:]:
            return True
    return False