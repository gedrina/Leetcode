class Solution:
    def countCharacters(self, words, chars: str) -> int:
        from collections import Counter
        from collections import defaultdict
      

    # If we find that a word is not good we set is_good to 0
    #This ensures that only the lengths of good words are added to the result

        count = Counter(chars)
        result = 0

        for w in words:
            current = defaultdict(int)
            is_good = 1
            for char in w:
                current[char] += 1
                if char not in count or current[char] > count[char]:
                    is_good = 0
                    break
            result += len(w) * is_good
        
        return result
    
# exmaple

sol = Solution()
words = ["cat","bt","hat","tree"]
chars = "atach"

print(sol.countCharacters(words, chars))