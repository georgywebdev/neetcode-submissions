class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {
            "(":")",
            "[":"]",
            "{":"}",
        }

        for char in s:
            # if opening bracket
            if char in char_map:
                stack.append(char)

            # if closing bracket
            else:
                if not stack:
                    return False

                # if there's a match
                if char_map[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        # stack needs to be empty at the end
        return True if not stack else False


        