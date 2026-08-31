class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency dict
        counts_dict = {}
        for num in nums:
            counts_dict[num] = counts_dict.get(num, 0) + 1
        print(counts_dict)

        counts_list = []
        for key, value in counts_dict.items():
            counts_list.append([key, value])
        print(counts_list)
        sorted_list = sorted(counts_list, key=lambda x: x[1]) 
        print(sorted_list)
        k_items = sorted_list[(len(sorted_list)-k):len(sorted_list)]

        result = []
        for item in k_items:
            result.append(item[0])
        print(result)
        return result