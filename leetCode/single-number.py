# https://leetcode.com/problems/single-number/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        if nums is None:
            return None
        if len(nums) <  1:
            return None
        if len(nums) == 1:
            return nums[0]
        nums = sorted(nums)
        for i in range(len(nums))[::2]:
            if i+1 == len(nums):
                return nums[i]
            elif nums[i] != nums[i+1]:
                return nums[i]
        return None