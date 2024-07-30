class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s)-1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length

# second solution
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         words = s.split()
#         return len(words[-1])

# example
s ="Hello World"
print(Solution().lengthOfLastWord(s))