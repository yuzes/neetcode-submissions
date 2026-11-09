class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                num = board[r][c]
                if num in rows[r] or num in cols[c] or num in squares[(r//3, c//3)]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                squares[(r//3, c//3)].add(num)
        return True