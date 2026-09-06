class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)

        def backtrack(idx: int) -> bool:
            if idx == len(empties):
                return True

            r, c = empties[idx]
            b = (r // 3) * 3 + c // 3

            for digit in map(str, range(1, 10)):
                if digit in rows[r] or digit in cols[c] or digit in boxes[b]:
                    continue

                board[r][c] = digit
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[b].add(digit)

                if backtrack(idx + 1):
                    return True

                board[r][c] = '.'
                rows[r].remove(digit)
                cols[c].remove(digit)
                boxes[b].remove(digit)

            return False

        backtrack(0)