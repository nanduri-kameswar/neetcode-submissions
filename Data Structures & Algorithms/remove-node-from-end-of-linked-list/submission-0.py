# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count nodes
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        # create dummy to handle the removal of head node
        dummy = ListNode(0, head)
        curr = dummy
        # for the count-n, move the pointer and remove the element
        for _ in range(count-n):
            curr = curr.next
        curr.next = curr.next.next
        # return the linked list
        return dummy.next
        