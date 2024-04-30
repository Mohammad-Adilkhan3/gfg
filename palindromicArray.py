def PalinArray(arr ,n):
    # Code here
    return all(str(w) == str(w)[::-1] for w in arr)
