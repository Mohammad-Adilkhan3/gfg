def reverse(self, head):
        #code here
        if not head or head.next == head:
            return head
        
        prev = None
        curr = head
        
        original_head = head
        
        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
            if curr == original_head:
                break
        
        head.next = prev
        head = prev  
        
        return head
            
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        #code here
        if not head:
            return None
        if head.data == key and head.next == head:
            return None
        prev = None
        curr = head
        
        while curr.data != key:
            prev = curr
            curr = curr.next
            if curr == head:
                return head
        if curr == head:
            last = head
            while last.next != head:
                last = last.next
            head = head.next
            last.next = head
        else:
            prev.next = curr.next
        
        return head
