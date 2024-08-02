class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}

        for c in s:
            if c in count_s:
                count_s[c] += 1
            else:
                count_s[c] = 1

        for c in t:
            if c in count_t:
                count_t[c] += 1
            else:
                count_t[c] = 1
        
        return count_s == count_t
    
# second solution 
# class Solution(object):
#     def isAnagram(self, s, t):
#         s_count = Counter(s)
#         t_count = Counter(t)

#         return s_count == t_count

# examples
s = "anagram"
t = "nagaram"

print(Solution().isAnagram(s,t))