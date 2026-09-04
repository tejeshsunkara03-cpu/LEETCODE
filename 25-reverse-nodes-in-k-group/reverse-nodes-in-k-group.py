class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:

            kth = group_prev

            for _ in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next

            group_next = kth.next

            prev = group_next
            current = group_prev.next

            while current != group_next:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp