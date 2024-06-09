def zigZag(arr, n):
    # Flag true indicates relation "<" is expected,
    # else ">" is expected. The first expected relation is "<"
    flag = True
    
    for i in range(n - 1):
        if flag:  # "<" relation expected
            # If we have a situation like A > B, we swap them
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:  # ">" relation expected
            # If we have a situation like A < B, we swap them
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        
        # Flip the flag for next iteration
        flag = not flag

    return arr
