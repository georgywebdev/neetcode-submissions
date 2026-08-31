class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        

        # prefixes
        product = 1
        for i in range(len(nums)):
            output[i] = product
            product *= nums[i]

        # suffixes
        product = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= product
            product *= nums[i]

        return output