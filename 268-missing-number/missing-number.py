class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = nums[-1]
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
