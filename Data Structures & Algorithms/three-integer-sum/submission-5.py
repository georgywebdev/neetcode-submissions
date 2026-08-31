class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        sorted_nums = sorted(nums)
        # print('sorted_nums', sorted_nums)
 
        for i, num in enumerate(sorted_nums):
            if sorted_nums[i] == sorted_nums[i - 1] and i != 0:
                continue
        
        
            target = 0 - num
            # print('num', num)
            # print('target', target)

            left = i + 1
            right = len(sorted_nums) - 1
            # print('left', left)
            # print('right', right)

            while left < right:
                current_sum = sorted_nums[left] + sorted_nums[right]

                # found one
                if current_sum == target:
                    triplet = [num, sorted_nums[left], sorted_nums[right]]

                    # makes it O(n^3), needs changing later
                    if triplet not in output:
                        output.append(triplet)
        
                    # print('output for current', triplet)
                    left += 1
                    right -= 1
                # sum too small
                elif current_sum < target:
                    left += 1
                # sum too large 
                else:
                    right -= 1

            # print(' ')
        
        # print('output', output)
        return output