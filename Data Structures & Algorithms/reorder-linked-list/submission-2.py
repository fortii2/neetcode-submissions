# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.findMidPoint(head)
        right = self.reverseLL(mid.next)
        mid.next = None

        self.mergeLL(head, right)

    def mergeLL(self, left: Optional[ListNode], right: Optional[ListNode]) -> ListNode:

        while left and right:
            leftNext = left.next
            rightNext = right.next

            left.next = right
            right.next = leftNext

            left = leftNext
            right = rightNext

        return left

    def reverseLL(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head

        new_head = self.reverseLL(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def findMidPoint(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
