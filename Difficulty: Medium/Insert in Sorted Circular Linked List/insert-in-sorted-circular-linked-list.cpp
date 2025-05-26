/* structure for a node
class Node {
 public:
  int data;
  Node *next;

  Node(int x){
      data = x;
      next = NULL;
  }
}; */

class Solution {
  public:
    Node* sortedInsert(Node* head, int data) {
        // code here
        Node* curr = head;
        Node* prev = NULL;
        Node* dataNode = new Node(data);
        
        while(true){
            if(prev){
                int a = curr -> data;
                int b = prev -> data;
                
                if((data >= b && data <= a)){
                    Node* link = curr;
                    prev -> next = dataNode;
                    dataNode -> next = link;
                    break;
                }
                else if(curr == head) {
                    Node* link = curr;
                    prev -> next = dataNode;
                    dataNode -> next = link;
                    if(data <= head->data) head = dataNode;
                    break;
                }
            }
            
            prev = curr;
            curr = curr -> next;
        }
        
        return head;
    }
};