class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        if rowIndex == 0:
            return row
        for i in range(1, rowIndex + 1):
            new_row = [1] * (i + 1)
            for j in range(1, i):
                new_row[j] = row[j - 1] + row[j]
            row = new_row
        
        return row
    
# example
sol = Solution()
print(sol.getRow(3)) # Output: [1, 3, 3, 1]
print(sol.getRow(0)) # Output: [1]
print(sol.getRow(1)) # Output: [1, 1]
