class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            i_middle = (l + r) // 2

            if nums[i_middle] > target:
                r = i_middle - 1
            elif nums[i_middle] < target:
                l = i_middle + 1
            elif nums[i_middle] == target:
                return i_middle
        return -1