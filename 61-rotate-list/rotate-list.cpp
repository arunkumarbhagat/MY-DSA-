class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0) return head;

        ListNode* curr = head;
        int len = 1;
        while (curr->next) {
            curr = curr->next;
            len++;
        }

        curr->next = head; // Make it circular
        k = k % len;
        int breakPoint = len - k;
        
        while (breakPoint--) curr = curr->next;

        head = curr->next;
        curr->next = nullptr;
        return head;
    }
};