def deleteAlt(self, head):
        # code here
        temp=head
        while temp and temp.next :
            temp.next=temp.next.next
            temp=temp.next
        return head
