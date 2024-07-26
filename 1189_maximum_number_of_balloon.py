class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        char_count = Counter(text)
        balloon = Counter('balloon')
        result = []

        for char in balloon:
            if char in char_count:
                value = char_count[char] // balloon[char]
                result.append(value)
            else:
                return 0
        
        return min(result)
    
