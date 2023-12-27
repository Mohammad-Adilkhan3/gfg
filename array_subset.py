def isSubset( a1, a2, n, m):
    res=[]
    for i in range(m):
        if a2[i] in a1:
            a1.remove(a2[i])
        else:
            return "No"
    return "Yes"
  
