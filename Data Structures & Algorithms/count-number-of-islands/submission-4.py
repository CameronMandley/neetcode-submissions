class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        visited = set()
        row, col = len(grid), len(grid[0])

        def bfs(row_i, col_j):
            q = collections.deque()
            q.append((row_i, col_j))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            curr_row, curr_col = q.popleft()

            for row_dir, col_dir in directions:
                r, c = curr_row + row_dir, curr_col + col_dir
                if (0 <= r < row) and (0 <= c < col) and ((r, c) not in visited) and grid[r][c] == "1":
                    visited.add((r, c))
                    bfs(r, c)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    islands += 1
                    bfs(i, j)
        return islands
