class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        # Create two dictionaries to store the character mappings
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            # Check if there is a conflicting mapping for char_s in s_to_t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            # Check if there is a conflicting mapping for char_t in t_to_s
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True
                
sol = Solution()
s = "paper"
t = "title"
print(sol.isIsomorphic(s,t))      

s2 = "foo"
t2 = "bar"
print(sol.isIsomorphic(s2, t2))         
            