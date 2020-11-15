class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        end = 0
        for index, num in enumerate(nums):
            end = max(end, index + num)
            if end >= len(nums) - 1: return True
            if end == index: return False
        
        return False