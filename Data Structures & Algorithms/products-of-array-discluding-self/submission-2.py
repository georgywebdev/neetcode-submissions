class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)

        product = 1
        for i in range(len(nums)):
            prefixes[i] = product
            product *= nums[i]

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            suffixes[i] = product
            product *= nums[i]

        output = []

        for i in range(len(nums)):
            output.append(prefixes[i] * suffixes[i])

        return output