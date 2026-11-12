class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                rotten_row, rotten_col = q.popleft()
                for r, c in directions:
                    curr_row, curr_col = rotten_row + r, rotten_col + c
                    if (0 <= curr_row < len(grid)) and (0 <= curr_col < len(grid[0])):
                        if grid[curr_row][curr_col] == 1:
                            grid[curr_row][curr_col] = 2
                            fresh -= 1
                            q.append((curr_row, curr_col))
            time += 1
        return time if fresh == 0 else -1
        