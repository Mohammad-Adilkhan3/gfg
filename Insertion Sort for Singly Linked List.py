class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head):
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    dummy.next = head
    current = head

    while current and current.next:
        if current.val > current.next.val:
            temp = current.next
            prev = dummy

            while prev.next.val < temp.val:
                prev = prev.next

            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        else:
            current = current.next

    return dummy.next

# Function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Example usage:
if __name__ == "__main__":
    # Creating a linked list: 4 -> 2 -> 1 -> 3
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    print("Original Linked List:")
    printList(head)

    sorted_head = insertionSortList(head)

    print("\nLinked List after Insertion Sort:")
    printList(sorted_head)
