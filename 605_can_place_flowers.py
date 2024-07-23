class Solution:
    def canPlaceFlowers(self, flowerbed,  n: int):
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        
        return (n <= 0)   
    
    
# example1

sol = Solution()
flowerbed = [1,0,0,0,1]
n = 2
print(sol.canPlaceFlowers(flowerbed,n))

# example2

sol = Solution()
flowerbed = [1,0,0,0,1]
n = 1
print(sol.canPlaceFlowers(flowerbed,n))