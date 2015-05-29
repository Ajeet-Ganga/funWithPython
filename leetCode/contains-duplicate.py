#https://leetcode.com/problems/contains-duplicate/

class Solution1:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if nums is None:
            return False
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return False
        nums = sorted(nums)
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if nums is None:
            return False
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return False
        d = set()

        for e in nums:
            if e in d:
                return True
            else:
                d.add(e)
        return False