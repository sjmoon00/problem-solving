class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = [head]
        t = head
        while t.next:
            t = t.next
            arr.append(t)
        
        N = len(arr)
        if N == 1:
            return None
         
        prev_idx = N-n-1
        if prev_idx < 0:
            head = head.next
            return head
        
        prev = arr[prev_idx]
        if prev.next.next:
            prev.next = prev.next.next
        else:
            prev.next = None
        return head