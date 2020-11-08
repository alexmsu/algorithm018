class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, start, temp, res):
            if start == len(nums):
                res.append(temp[:])
                return
            
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                temp.append(nums[start])
                helper(nums, start + 1, temp, res)
                nums[i], nums[start] = nums[start], nums[i]
                temp.pop()
            
        res = []
        helper(nums, 0, [], res)
        return res