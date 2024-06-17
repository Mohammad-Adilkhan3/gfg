def InOrder(self,root):
        # code here
        result = []
        self.inorderHelper(root, result)
        return result
    
    def inorderHelper(self, node, result):
        if node is None:
            return
        
        self.inorderHelper(node.left, result)
        result.append(node.data)
        self.inorderHelper(node.right, result)


