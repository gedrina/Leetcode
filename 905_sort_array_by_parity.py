class Solution:
    def sortArrayByParity(self, nums) :
        even = []
        odd = []

        for number in nums:
            if number % 2 == 0:
                even.append(number)
            else:
                odd.append(number)
        return even + odd   
    
# example 
nums = [3,1,2,4]
print(Solution().sortArrayByParity(nums))