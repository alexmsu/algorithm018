class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, start, res):
            if start == len(nums) - 1:
                if nums not in res:
                    res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                helper(nums, start + 1, res)        
                nums[start], nums[i] = nums[i], nums[start]
        
        nums.sort()
        res = []
        helper(nums, 0, res)
        return res