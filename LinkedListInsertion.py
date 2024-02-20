def insertAtBegining(self,head,x):
        # code here 
        temp=Node(x)
        temp.next=head
        return temp
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here 
        if head == None :
            return Node(x)
            
        cur = head
        
        while cur.next != None:
            
            cur = cur.next
            
        cur.next = Node(x)
        return head
