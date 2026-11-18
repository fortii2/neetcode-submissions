# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        x, y = list1, list2

        while x and y:
            if x.val < y.val:
                cur.next = x
                x = x.next
            else:
                cur.next = y
                y = y.next

            cur = cur.next
        
        cur.next = x if x else y
        
        return dummy.next
