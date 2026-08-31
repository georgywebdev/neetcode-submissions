class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # print(numbers)
        left = 0
        right = len(numbers) - 1
        # print("left", left)
        # print("right", right)

        

 
        
        while left < right and numbers[left] + numbers[right] != target:
            # sum too small  → left += 1
            if (numbers[left] + numbers[right]) < target:
                left += 1
            # sum too large  → right -= 1
            else:
                right -= 1
        else: 
            return [left + 1, right + 1]


