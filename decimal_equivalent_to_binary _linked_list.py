class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def decimalValue(head):
    decimal_value = 0
    mod = 10**9 + 7
    
    while head:
        decimal_value = (decimal_value * 2 + head.val) % mod
        head = head.next
    
    return decimal_value

# Example 1
n1 = 3
linked_list1 = ListNode(0, ListNode(1, ListNode(1)))
print(decimalValue(linked_list1))  # Output: 3

# Example 2
n2 = 4
linked_list2 = ListNode(1, ListNode(1, ListNode(1, ListNode(0))))
print(decimalValue(linked_list2))  # Output: 14
