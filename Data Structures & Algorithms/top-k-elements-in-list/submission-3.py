class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency dict
        counts_dict = {}
        for num in nums:
            counts_dict[num] = counts_dict.get(num, 0) + 1
        print(counts_dict) 
        # {1: 1, 2: 2, 3: 3}


        # buckets
        counts_list = [[] for _ in range(len(nums))]
        print(counts_list)
        for key, value in counts_dict.items():
            counts_list[value-1].append(key)
        print(counts_list)
        # [[], [1], [2], [3], [], []]

        flattened_counts = sum(counts_list, [])
        print(flattened_counts)

        result = []
        for item in flattened_counts[::-1]:
            result.append(item)
        print(result)
        # [[3], [2], [1]]
        return result[:k]
