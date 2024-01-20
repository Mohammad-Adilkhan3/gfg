def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        current=head
        count=0
        while current is not None:
            count+=1
            current=current.next
        count=(count//2)+1
        temp=0
        while head!=None:
            temp+=1
            if count==temp:
                return head.data
            head=head.next
