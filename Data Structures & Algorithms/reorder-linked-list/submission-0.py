# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next:
            return 
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            # print("slow : ", slow.val)
            # print("fast : ", fast.val)
            slow = slow.next 
            fast = fast.next.next
        # print("slow : ", slow.val)
        # print("fast : ", fast.val)
        
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        second = prev
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
