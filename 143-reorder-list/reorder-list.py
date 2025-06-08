class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        second = slow.next
        prev = slow
        slow.next = None
        
        curr = second
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        second = prev  # Head of reversed second half

        # Step 3: Merge two halves
        first = head
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2