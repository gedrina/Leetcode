class Solution:
    def searchInsert(self, nums, target: int) -> int:
        low, high = 0, len(nums)-1

        while low <= high:
            medium = (low+high)//2
            if nums[medium] == target:
                return medium
            elif nums[medium] > target:
                high = medium - 1
            else:
                low = medium + 1
        return low
    
# example
nums = [1,3,5,6]
target = 2
print(Solution().searchInsert(nums,target))