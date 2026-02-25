class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find the middle using slow/fast pointers
        # After this, 'slow' will be at the start of the second half
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            temp_next = slow.next
            slow.next = prev
            prev = slow
            slow = temp_next

        # Step 3: Compare the first and second halves
        # 'prev' is now the head of the reversed second half
        left, right = head, prev
        while right:  # We only need to compare until the end of the reversed half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True