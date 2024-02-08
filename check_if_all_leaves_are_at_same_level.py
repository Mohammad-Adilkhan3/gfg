def check(self, root):
        #Code here
        if root is None:
            return True
        queue = [root]
        level = 0
        leaf_level = None
        
        while queue:
            size = len(queue)
            level += 1
            
            for i in range(size):
                node = queue.pop(0)
                
                if node.left is None and node.right is None:
                    if leaf_level is None:
                        leaf_level = level
                    elif level != leaf_level:
                        return False
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return True
