from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer

# second solution
# from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         right = [1]
#         left = [1]
#         nums_rev = nums[::-1]

#         for i in range(len(nums)-1):
#             value_r = nums[i] * right[-1]
#             right.append(value_r)
#         for j in range(len(nums)-1): 
#             value_l = nums_rev[j] * left[-1]
#             left.append(value_l)

#         left_rev = left[::-1]
#         print(left_rev)
#         print(right)
#         answer = []
#         for x in range(len(nums)):
#             answer.append(right[x]*left_rev[x])
#         return answer

# Exmaple
nums = [1,2,3,4]