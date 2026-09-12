class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_map = {}
        l = 0
        max_freq = 0
        res = 0
        for r in range(len(s)):

            window_map[s[r]] = window_map.get(s[r], 0) + 1
            max_freq = max(max_freq, window_map[s[r]])

        
            while (r - l + 1) - max_freq > k :
                window_map[s[l]] -= 1
                l += 1

            # window is valid here
            res = max(res, r - l + 1)

        return res


