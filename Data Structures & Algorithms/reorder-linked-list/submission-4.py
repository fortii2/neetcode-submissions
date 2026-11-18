# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.findMid(head)
        right = mid.next
        mid.next = None
        right = self.reverseList(right)
        left = head

        dummy = ListNode()
        cur = dummy

        while left and right:
            cur.next = left
            cur = cur.next
            left = left.next

            cur.next = right
            cur = cur.next
            right = right.next

        cur.next = left if left else right

    def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre
