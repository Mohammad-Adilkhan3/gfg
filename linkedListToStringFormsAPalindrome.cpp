bool compute(Node* head) {
        // Your code goes here
        string temp="";
        while(head){
            temp+=head->data;
            head=head->next;
        }
        int i=0,j=temp.size()-1;
        while(i<j){
            if(temp[i]!=temp[j])return false;
            i++;
            j--;
        }
        return true;
    }
