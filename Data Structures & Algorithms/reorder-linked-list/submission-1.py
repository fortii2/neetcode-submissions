# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur, arr = head, []
        while cur:
            arr.append(cur)
            cur = cur.next

        p, q = 0, len(arr) - 1
        cur = head
        while p <= q:
            cur.next = arr[p]
            cur = cur.next
            p += 1
            
            if p <= q:
                cur.next = arr[q]
                cur = cur.next
                q -= 1
        
        cur.next = None
    