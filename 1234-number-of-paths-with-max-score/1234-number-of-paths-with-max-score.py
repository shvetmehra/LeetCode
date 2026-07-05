class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10 ** 9 + 7
        rows, cols = len(board), len(board[0])

        grid = []
        for row in board:
            current = []
            for cell in row:
                if cell == 'X':
                    current.append(-1)
                elif cell in ('S', 'E'):
                    current.append(0)
                else:
                    current.append(int(cell))
            grid.append(current)

        memo = {}

        def dfs(r, c):
            if r >= rows or c >= cols or grid[r][c] == -1:
                return (float("-inf"), 0)

            if r == rows - 1 and c == cols - 1:
                return (0, 1)

            if (r, c) in memo:
                return memo[(r, c)]

            best_score = float("-inf")
            path_count = 0

            for nr, nc in [(r + 1, c), (r, c + 1), (r + 1, c + 1)]:
                score, ways = dfs(nr, nc)

                if score > best_score:
                    best_score = score
                    path_count = ways
                elif score == best_score:
                    path_count += ways

            if best_score == float("-inf"):
                memo[(r, c)] = (float("-inf"), 0)
            else:
                memo[(r, c)] = (best_score + grid[r][c], path_count)

            return memo[(r, c)]

        score, ways = dfs(0, 0)

        if score == float("-inf"):
            return [0, 0]

        return [score % MOD, ways % MOD]