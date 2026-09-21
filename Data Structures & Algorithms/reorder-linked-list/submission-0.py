# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # half
        # left: queue
        # right: stack , start at mid
        # use sentinel to save

        # count N
        cur, arr = head, []
        while cur:
            arr.append(cur)
            cur = cur.next

        cur = head

        while arr:
            cur.next = arr.pop(0)
            cur = cur.next

            if arr:
                cur.next = arr.pop(-1)
                cur = cur.next
        
        cur.next = None
    