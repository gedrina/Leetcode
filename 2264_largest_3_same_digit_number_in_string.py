class Solution:
    def largestGoodInteger(self, num: str) -> str: 
        present = set()

        for i in range(len(num)-2):
            if num[i] == num[i+1] == num [i+2]:
                present.add(int(num[i]))

        if present:
            largest = str(max(present))
            return largest * 3
        else:
            return ""


