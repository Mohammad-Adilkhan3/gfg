def printPat(n):
    #Code here
    word = ""
    lst = range(n, 0, -1)
    for i in lst:
        for j in lst:
            for _ in range(i):
                word = word + str(j) + " "
        word+="$"
            
    print(word) 
 
