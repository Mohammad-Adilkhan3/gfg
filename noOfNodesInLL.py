def getCount(self, head_node):
        #code here
        count = 0
        while head_node!= None:
            count+=1
            head_node = head_node.next
            
        return count

