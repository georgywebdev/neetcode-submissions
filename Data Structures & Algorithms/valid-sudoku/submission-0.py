class Solution:
    def has_duplicates(self, nums):
        filtered_nums = [x for x in nums if x != '.']
        # print('filtered', filtered_nums)
        return len(filtered_nums) != len(set(filtered_nums))

    def isValidSudoku(self, board: List[List[str]]) -> bool:


        # Each row must contain the digits 1-9 without duplicates.
        for row in board:
            if self.has_duplicates(row):
                return False  

        # Each column must contain the digits 1-9 without duplicates.
        for col in range(len(board[0])):
            column = []

            for row in board:
                column.append(row[col])

            if self.has_duplicates(column):
                return False
        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):

                box = []

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        box.append(board[row][col])
                # print('box', box)
                if self.has_duplicates(box):
                    return False

        return True
