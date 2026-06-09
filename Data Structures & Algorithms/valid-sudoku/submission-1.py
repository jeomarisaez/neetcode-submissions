class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {i: set() for i in range(len(board))}
        col_map = {i: set() for i in range(len(board))}
        square_map = {i: set() for i in range(len(board))}

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                square_index = ((i //3) * 3) + ((j //3))

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