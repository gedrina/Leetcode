class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))
    
nums = [1,2,3,1]
print(Solution().containsDuplicate(nums))