class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        start, end = 0, 0
        step = 0
        while end < len(nums) - 1:
            step += 1
            new_end = end + 1
            while start <= end:
                new_end = max(new_end, nums[start] + start)
                start += 1
            end = new_end
        return step