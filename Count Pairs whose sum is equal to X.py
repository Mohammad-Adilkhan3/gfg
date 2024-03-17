class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def countPairs(head1, head2, x):
    # Initialize a set to store elements of the first linked list
    set1 = set()
    
    # Add elements of the first linked list to the set
    current = head1
    while current:
        set1.add(current.val)
        current = current.next
    
    # Iterate through the elements of the second linked list
    # and check if there exists a complement element in set1
    count = 0
    current = head2
    while current:
        complement = x - current.val
        if complement in set1:
            count += 1
        current = current.next
    
    return count

# Example usage:
# Create the first linked list: 1->2->3->4->5->6
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(6)

# Create the second linked list: 11->12->13
head2 = ListNode(11)
head2.next = ListNode(12)
head2.next.next = ListNode(13)

# Given value
x = 15

# Count distinct pairs whose sum is x
print(countPairs(head1, head2, x))  # Output: 3
