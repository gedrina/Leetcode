class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid +=1
            elif nums[mid] == 1:
                mid +=1
            else: # nums[mid] == 2
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        return nums
# Example

nums = [2,0,2,1,1,0]
print(Solution().sortColors(nums))