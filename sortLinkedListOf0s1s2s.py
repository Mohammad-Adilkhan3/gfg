def segregate(self, head):
        #code here
        stack = []
        curr = head 
        while curr!=None:
            stack.append(curr.data)
            curr = curr.next 
        stack = sorted(stack)
        curr = head 
        # print(stack)
        while curr:
            curr.data = stack[-1]
            stack.pop()
            curr = curr.next
        stack = []
        curr  = head 
        while curr!=None:
            stack.append(curr.data)
            curr = curr.next 
        curr = head 
        while curr:
            curr.data = stack[-1]
            stack.pop()
            curr = curr.next 
        return head
    
