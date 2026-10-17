class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        curr = head

        while curr:
            # check that k nodes remain
            len_ = 0
            probe = curr
            while probe and len_ < k:
                probe = probe.next
                len_ += 1
            if len_ < k:
                break

            group_start = curr
            new_head, rest = self.reverse_node(group_start, k)

            group_prev.next = new_head     # previous part -> reversed group
            group_start.next = rest        # old first node (now tail) -> rest
            group_prev = group_start       # move to the end of this group
            curr = rest

        return dummy.next

    def reverse_node(self, head, k):
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev, curr