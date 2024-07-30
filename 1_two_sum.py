class Solution:
    def twoSum(self, nums, target: int) :
       difference = {}

       for i, n in enumerate(nums):
            diff = target - n
            if diff in difference:
                return (difference[diff], i)
            difference[n] = i

# examples
nums =[2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))