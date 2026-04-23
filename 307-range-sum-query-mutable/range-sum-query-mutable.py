class NumArray(object):
    def __init__(self, nums):
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        self.nums = nums[:]  # copy
        
        # Build BIT
        for i in range(self.n):
            self._update_bit(i + 1, nums[i])
    
    def _update_bit(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i
    
    def update(self, index, val):
        delta = val - self.nums[index]
        self.nums[index] = val
        self._update_bit(index + 1, delta)
    
    def _query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
    
    def sumRange(self, left, right):
        return self._query(right + 1) - self._query(left)