class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        l_max = 0
        r_max = 0

        res = 0

        while l < r:
            # initializing and updating maxes
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            
            # move pointers, one with the smaller max and calculate the water level for the moved pointer
            if l_max <= r_max:
                res += l_max - height[l]
                l += 1
            else:
                res += r_max - height[r]
                r -= 1
     
        return res