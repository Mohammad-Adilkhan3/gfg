def merge(self, root1, root2):
        # code here
        res=[]
        def inord(root,res):
            if root is None:
                return
            inord(root.left,res)
            res.append(root.data)
            inord(root.right,res)
        inord(root1,res)
        inord(root2,res)
        res.sort()
        return res
