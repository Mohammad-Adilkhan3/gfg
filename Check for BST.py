def isBST(self, root):
        #code here
        def isright(root,left,right):
            if not root:
                return 1
            if left >=root.data or right <=root.data:
                return 0
            
            return (isright(root.left ,left,root.data) and isright(root.right,root.data,right))
        
        return isright(root,float("-inf"),float("inf"))
