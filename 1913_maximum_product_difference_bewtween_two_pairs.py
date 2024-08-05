class Solution:
    def maxProductDifference(self, nums) -> int:
        sorted_nums = sorted(nums)
        max1, max2 = sorted_nums[-1] , sorted_nums[-2]
        min1, min2 = sorted_nums[0], sorted_nums[1]

        return (max1*max2) - (min1*min2)
    
# example
nums = [5,6,2,7,4]
print(Solution().maxProductDifference(nums))

# second solution
# class Solution:
#     def maxProductDifference(self, nums: List[int]) -> int:
#         max1 = max(nums)
#         min1 = min(nums)
#         nums.remove(max1)
#         nums.remove(min1)
        
#         max2 = max(nums)
#         min2 = min(nums)

#         return (max1*max2) - (min1*min2) 

        


# bubble sort

# class Solution:
#     def maxProductDifference(self, nums) -> int:
#         sorted_nums = sorted(nums)
#         max1, max2 = sorted_nums[-1] , sorted_nums[-2]
#         min1, min2 = sorted_nums[0], sorted_nums[1]

#         return (max1*max2) - (min1*min2)

