# Q1. LC 206 Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.
def reverseList(self, head: ListNode):
    prev = None
    curr = head
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    head = prev
    return head

# Alternative way of reversing linked list
def reverseList(head, prev=None):
    if not head:
        return prev
    next = head.next
    head.next = prev
    return self.reverseList(next, head)


# Q2. LC 21 Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes
# of the first two lists.
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = curr = ListNode(0)
    
    while l1 and l2:
        if l1.val > l2.val:
            curr.next = l2
            l2 = l2.next
        else:
            curr.next = l1
            l1 = l1.next
        curr = curr.next
        
    # This is when one linkedlist gets completely empty, and so we join the other non-empty list
    curr.next = l1 or l2
    
    # Alternatively, replace that with
    if l1 is None:
        curr.next = l2
    elif l2 is None:
        curr.next = l1
        
    return dummy.next


# Q3 LC. 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
# connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false

# The idea is to use slow and fast pointer, if there is a cycle, then eventually the fast pointer will catch up to the
# slow pointer

def hasCycle(self, head: ListNode) -> bool:
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # Check if the slow pointer is the same as the fast pointer, if it is, then there is a cycle
        if slow == fast:
            return True
    return False


# Q4 LC 234 Given the head of a singly linked list, return true if it is a palindrome.

