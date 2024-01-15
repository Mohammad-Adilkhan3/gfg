def removeDuplicates(self, head):
        # code here
        # return head after editing list
        dict1={}
        dummy_node=Node(-1)
        curr1=dummy_node
        if head is None or head.next is None:
            return head
        curr=head
        while curr is not None:
            if curr.data not in dict1:
                dict1[curr.data]=1
                new_node=Node(curr.data)
                curr1.next=new_node
                curr1=curr1.next
            curr=curr.next
        return dummy_node.next

