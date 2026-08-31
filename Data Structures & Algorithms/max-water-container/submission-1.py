class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers, shift one pointer at a time - the smaller one
        res = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            current_area = (r - l) * min(heights[l], heights[r])

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

            res = max(res, current_area)

        return res