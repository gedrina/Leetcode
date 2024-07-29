def majorityElement(nums):
        counts = {}
        
        #create hash map
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        #find mos frequent value
        for num, count in counts.items():
            if count > len(nums)//2:
                return num

# Example 1
nums1 = [3, 2, 3]
print(majorityElement(nums1))  # Output: 3

# Example 2
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums2))  # Output: 2

# second solution
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums_count = Counter(nums)

#         for key in nums_count:
#             if nums_count[key] > len(nums) // 2:
#                 return key