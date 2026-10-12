# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        curr = head
        while curr:
            cnt+=1
            curr = curr.next
        from_start = cnt-n
        # print(from_start)
        curr = head
        idx = 0
        if from_start == 0:
            head = head.next
            return head
        while True:
            # print(idx, curr.val)
            if idx + 1 == from_start:
                if not curr.next and not curr.next.next:
                    curr = None
                    break
                else:
                    curr.next = curr.next.next
                    # print(curr.val)
                    break
            curr = curr.next
            idx+=1
        return head