class Solution:
    def findRepeatedDnaSequences(self, s: str) :
        adn = set()
        r_adn = set()

        for i in range(len(s)-10+1):
            if s[i:i+10] in adn:
                r_adn.add(s[i:i+10])
            else:
                adn.add(s[i:i+10])
        return r_adn

# example
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(Solution().findRepeatedDnaSequences(s))