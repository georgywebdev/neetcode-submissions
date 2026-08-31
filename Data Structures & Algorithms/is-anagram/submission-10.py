class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars = {}
        t_chars = {}
        for s_char, t_char in zip(s, t):
            s_chars[s_char] = s_chars.get(s_char, 0) + 1
            t_chars[t_char] = t_chars.get(t_char, 0) + 1
        return s_chars == t_chars