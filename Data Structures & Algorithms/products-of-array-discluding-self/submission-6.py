class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        suffixes = []

        product = 1
        for num in nums:
            prefixes.append(product)
            product *= num

        product = 1
        for num in reversed(nums):
            suffixes.append(product)
            product *= num
        
        suffixes.reverse()

        output = []

        for i in range(len(nums)):
            output.append(prefixes[i] * suffixes[i])

        return output