# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle element
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # split the linked list into 2 lists
        second = slow.next
        slow.next = None
        # sort the 2nd list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # merge alternate nodes
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
