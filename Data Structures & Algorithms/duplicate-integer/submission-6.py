class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:   
        # as brute force as it gets     
        # for index_i, i in enumerate(nums):
        #     for index_j,j in enumerate(nums):
        #         print('i-j', i, j)
        #         print('nums[i]-nums[j]', index_i, index_j)
        #         if i==j and index_i != index_j:
        #             return True
        # return False

        # a bit better brute force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # hash set
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False