# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        length = 0
        curr = head
        dummy = ListNode(0, head)
        while curr:
            length += 1
            curr = curr.next
        curr = dummy
        k = (length - n)
        for i in range(k):
            curr = curr.next
        curr.next = curr.next.next

        return dummy.next