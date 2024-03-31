def findMaxForN(self, root, n):
        #Print the value of the element if it exists otherwise print -1.
        
        #code here
        if root is None:
            return None
        
        greatest = -1
        current = root
        
        while current:
            if current.key <= n:
                greatest = current.key
                current = current.right
            else:
                current = current.left
                
        return greatest
