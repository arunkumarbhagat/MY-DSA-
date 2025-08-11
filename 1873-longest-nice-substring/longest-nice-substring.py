class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s) < 2:
            return ""

        
        for i, ch in enumerate(s):
            if ch.swapcase() not in s:
               
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left if len(left) >= len(right) else right
        
      
        return s
       