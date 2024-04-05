def preorder(root):
   
    # code here
    res = []
    if root != None:
        res.append(root.data)
        ln = preorder(root.left)
        rn = preorder(root.right)
        if ln:
           for i in ln:
               res.append(i)
        if rn:
            for j in rn:
                res.append(j)
    
    return res
