class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        word1 = "".join(word1)
        word2 = "".join(word2)
        
        return word1 == word2
    
# example
word1 = ["ab", "c"]
word2 = ["a", "bc"]

print(Solution().arrayStringsAreEqual(word1,word2))

# second solution (faster)
#   s1 = ""
#   s2 = ""

#  for i in word1:
#    s1 += i
#  for j in word2:
#     s2 += j
# return s1 == s2