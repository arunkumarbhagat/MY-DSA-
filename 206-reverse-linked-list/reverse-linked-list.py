class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next      # store next node
            curr.next = prev     # reverse link
            prev = curr          # move prev forward
            curr = nxt           # move curr forward
            
        return prev