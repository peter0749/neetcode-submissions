class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_row = [0] * 9
        check_col = [0] * 9
        check_cell = [0] * 9
        for i in range(9):
            for j in range(9):
                cell_no = (i // 3) * 3 + (j // 3)
                val = board[i][j]
                if val == '.':
                    continue
                val = int(val)
                set_bit = (1<<val)
                # check & set row
                if check_row[i] & set_bit:
                    return False
                check_row[i] |= set_bit
                # check & set col
                if check_col[j] & set_bit:
                    return False
                check_col[j] |= set_bit
                # check & set 3x3 cell
                if check_cell[cell_no] & set_bit:
                    return False
                check_cell[cell_no] |= set_bit
        return True