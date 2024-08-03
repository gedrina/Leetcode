nums = [1,2,3,4]

N= len(nums)
print(N)

for i in range(1,N):

    nums[i] += nums[i-1]
print(nums)