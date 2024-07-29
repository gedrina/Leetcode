class Solution:
    def getConcatenation(self, nums):
        ans = []

        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
    
    
# class Solution:
#     def getConcatenation(self, nums):
#         return nums + nums
