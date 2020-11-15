class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            if nums[lo] <= nums[hi]: return nums[lo]
            mid = (lo + hi) / 2
            
            if mid > 0 and nums[mid] < nums[mid - 1]: return nums[mid]
            elif nums[lo] <= nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1