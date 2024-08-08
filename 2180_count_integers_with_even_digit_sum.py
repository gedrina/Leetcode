class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for number in range(1,num+1):
            current = str(number)
            suma = 0
            for digit in current:
                suma += int(digit)
            if suma % 2 == 0:
                count += 1
        return count 


# example
num = 4
print(Solution().countEven(num))

        

       

         
        