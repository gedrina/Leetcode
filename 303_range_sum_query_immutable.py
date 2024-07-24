class NumArray:

    def __init__(self, nums):
        self.nums = nums

    
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
    
# example
nums = [-2, 0, 3, -5, 2, -1]
num_array = NumArray(nums)

print(num_array.sumRange(0, 2))  # Output: 1
print(num_array.sumRange(2, 5))  # Output: -1
