class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        window_max = 0        
        l = 0

        for r in range(len(s)):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1

            s_set.add(s[r])
            window_max = max(window_max, r - l + 1)

        return window_max      
