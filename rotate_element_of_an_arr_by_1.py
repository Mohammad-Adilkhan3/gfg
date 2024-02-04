def rotate( arr, n):
    for i in range(n):
        arr[i],arr[n-1]=arr[n-1],arr[i];
    return arr
