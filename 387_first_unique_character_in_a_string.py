class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        count_s = Counter(s)

        for i in range(len(s)):
            if s[i] in count_s:
                if count_s[s[i]] == 1:
                    return i
        return -1

