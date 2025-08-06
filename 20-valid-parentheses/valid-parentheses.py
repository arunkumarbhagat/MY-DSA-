class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                if (char == ')' and stack.pop() != '(') or \
                   (char == '}' and stack.pop() != '{') or \
                   (char == ']' and stack.pop() != '['):
                    return False
        return not stack
   