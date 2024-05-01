boolean isCircular(Node head)
    {
	// Your code here
	 if(head == null){
        return true;
    }
    Node currNode = head;
    while(currNode != null){
        currNode = currNode.next;
        if(currNode == head){
            return true;
        }
    }
    return false;
    }
}
