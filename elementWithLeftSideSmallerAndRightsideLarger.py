def findElement( arr, n):
    mn = arr[0]
    mx = arr[0]
    stk = []
    for i in range(1,n-1):
        if arr[i] >= mx:
            mx = arr[i]
            stk.append(arr[i])
        elif arr[i] <= mn:
            mn = arr[i]
            stk = []
        else:
            stk = []
    if len(stk) != 0:
        if stk[0] <= arr[n-1]:
            return stk[0]
    return -1
    
