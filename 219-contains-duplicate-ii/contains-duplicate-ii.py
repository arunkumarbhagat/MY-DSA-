class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lastIndex = {}

        for i, num in enumerate(nums):
            if num in lastIndex and i - lastIndex[num] <= k:
                return True
            lastIndex[num] = i

        return False
