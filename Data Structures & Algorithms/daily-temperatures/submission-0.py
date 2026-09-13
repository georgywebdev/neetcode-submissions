class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        # needs to be not increasing
        stack = []

        for index, temp in enumerate(temperatures):
            # item is bigger, keep popping until it's not
            while stack and temp > stack[-1][1]:
                old_index = stack[-1][0]
                stack.pop()
                output[old_index] = index - old_index

            # item is not bigger so add it
            stack.append((index, temp))

        return output


