class Solution:
    def isMonotonic(self, nums) -> bool:
        increasing, decreasing = True, True
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                decreasing = False
            if nums[i] > nums[i + 1]:
                increasing = False
        return increasing or decreasing

