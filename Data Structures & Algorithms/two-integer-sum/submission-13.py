class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, num in enumerate(nums):
            difference = target - num
            print('diff', difference)
            print('nums_dict pre', nums_dict)
            if difference in nums_dict:
                print('return', [index, nums_dict[difference]])
                return [nums_dict[difference], index]
            else: nums_dict[num] = index
            print('nums_dict after', nums_dict)
            

