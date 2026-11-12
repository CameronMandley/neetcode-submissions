class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        atlantic = set()
        pacific = set()

        visited = set()  # ADDED

        for i in range(row):
            for j in range(col):
                q.append((i, j, (i, j)))

        while q:
            i, j, origin = q.pop()

            # ADDED: Prevent revisiting the same cell from the same origin
            if (i, j, origin) in visited:
                continue
            visited.add((i, j, origin))

            # ADDED: Stop if origin already reaches both oceans
            if origin in pacific and origin in atlantic:
                continue

            for r, c in directions:
                next_r, next_c = i + r, j + c

                if (0 <= next_r < row) and (0 <= next_c < col):
                    if heights[next_r][next_c] <= heights[i][j]:
                        q.append((next_r, next_c, origin))
                elif next_r == -1:
                    pacific.add(origin)
                elif next_r == row:
                    atlantic.add(origin)
                elif next_c == -1:
                    pacific.add(origin)
                elif next_c == col:
                    atlantic.add(origin)

        result = []
        for key in atlantic:
            if key in pacific:
                result.append([key[0], key[1]])

        return result