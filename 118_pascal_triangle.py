class Solution:
    def generate(self, numRows: int) :
        if numRows == 1:
            return [[1]]
        triangle =[[1],[1,1]]

        if numRows == 2:
            return triangle

        for i in range(2,numRows):
            pascal = [1]
            length = len(triangle[-1])

            for i in range(0,length-1):
                start = triangle[-1]
                num_pascal = start[i] + start[i+1]
                pascal.append(num_pascal)
            pascal.append(1)
            triangle.append(pascal)
        
        return triangle
#example


sol = Solution()
num_rows = 5
print(sol.generate(num_rows))
