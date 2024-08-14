class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        low, high = 0, x

        while low <= high:
            mid = (low + high) // 2
            sr = mid * mid 

            if sr == x:
                return mid 
            elif sr < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return high

# example 

x = 8
print(Solution().mySqrt(x))