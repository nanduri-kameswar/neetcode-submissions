# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr, tail = head, head
        while curr.next and curr.next.next:
            while tail.next.next:
                tail = tail.next
            temp = curr.next
            curr.next = tail.next
            tail.next.next = temp
            tail.next = None
            curr = curr.next.next
            tail = curr.next