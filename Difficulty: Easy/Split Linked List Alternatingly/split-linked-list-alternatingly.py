#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        cnt=0
        t1=h1=None
        t2=h2=None
        temp=head
        while temp:
            if cnt%2==0:
                if h1==None:
                    h1=t1=temp
                else:
                    t1.next=temp
                    t1=t1.next
            else:
                if h2==None:
                    h2=t2=temp
                else:
                    t2.next=temp
                    t2=t2.next
            cnt+=1
            temp=temp.next
        t1.next=None
        t2.next=None
        return [h1, h2]
            


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends