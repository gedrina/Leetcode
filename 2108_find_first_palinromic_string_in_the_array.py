class Solution:
    def firstPalindrome(self, words) -> str:
        for word in words:
            if word == word[::-1]:  
                return word
        return "" 
        
# example
words1 = ["abc","car","ada","racecar","cool"]
words2 = ["notapalindrome","racecar"]

print(Solution().firstPalindrome(words1))  # Output: "ada"
print(Solution().firstPalindrome(words2))  # Output: "racecar"