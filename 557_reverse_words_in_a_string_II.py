class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        reversed_words = []

        for word in words:
            rev = word[::-1]
            reversed_words.append(rev)

        return " ".join(reversed_words)
    
    
# examples
s1 = "Let's take LeetCode contest"
s2 = "Mr Ding"
print(Solution().reverseWords(s1))
print(Solution().reverseWords(s2))