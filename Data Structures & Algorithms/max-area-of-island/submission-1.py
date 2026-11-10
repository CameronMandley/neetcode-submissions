class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        visited = set()
        islands = {}

        def bfs(row_i, col_j, key):
            nonlocal islands
            nonlocal visited

            q = collections.deque()
            q.append((row_i, col_j))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            curr_row, curr_col = q.popleft()

            for row_dir, col_dir in directions:
                r, c = curr_row + row_dir, curr_col + col_dir
                if (0 <= r < row) and (0 <= c < col) and (grid[r][c] == 1) and ((r, c) not in visited):
                    islands[key] += 1
                    visited.add((r, c))
                    bfs(r, c, key)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    islands[(i, j)] = 1
                    bfs(i, j, (i, j))
        
        maxisland = 0
        for key in islands.keys():
            maxisland = max(maxisland, islands[key])
        return maxisland

        