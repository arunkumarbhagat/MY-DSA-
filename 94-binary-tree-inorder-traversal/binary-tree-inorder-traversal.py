class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)
            
            # Move to right subtree
            current = current.right
        
        return result        