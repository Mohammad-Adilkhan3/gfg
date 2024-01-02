 def detectLoop(self, head):
        #code here
        slow = fast = head
        
        while fast and fast.next :
            fast=fast.next.next
            slow=slow.next
            
            if slow==fast:
                return True
        return False
