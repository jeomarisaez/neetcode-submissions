class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {}
        col_map = {}
        square_map = {}

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if i not in row_map:
                    row_map[i] = set()
                if j not in col_map:
                    col_map[j] = set()
                square_index = ((i //3) * 3) + ((j //3))
                if square_index not in square_map:
                    square_map[square_index] = set()

                if board[i][j] in row_map[i]:           
                    return False
                elif board[i][j] in col_map[j]:
                    return False
                elif board[i][j] in square_map[square_index]:
                    return False
                else:
                    row_map[i].add(board[i][j])
                    col_map[j].add(board[i][j])
                    square_map[square_index].add(board[i][j])
        return True