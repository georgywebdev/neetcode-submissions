class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest = 0

        for num in s:
            # if number has predecessor:
            if num - 1 not in s:
                # this is a sequence start
                current = num
                length = 1

                while current + 1 in s:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest