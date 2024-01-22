struct Node* reverseList(struct Node *head)
    {
        // code here
        // return head of reversed list
         if(head==NULL){
                return head ;
            }
        Node* prev=NULL;
        Node* curr=head;
        Node* nex=head;
        while(curr !=NULL){
            nex=curr->next;
            curr->next=prev;
            prev=curr;
            curr=nex;
        }
        return prev;
    


    }
