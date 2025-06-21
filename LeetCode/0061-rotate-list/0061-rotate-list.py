# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        N = 1
        tmp = head
        while tmp.next != None:
            tmp = tmp.next
            N += 1
        if N == 1:
            return head

        k %= N
        for _ in range(k):
            ttail = head
            while ttail.next.next != None:
                ttail = ttail.next
            tail = ttail.next
            ttail.next = None
            tail.next = head
            head = tail
        return head