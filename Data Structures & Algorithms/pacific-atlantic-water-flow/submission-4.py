class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:  # ADDED
            return []

        atlantic = set()
        pacific = set()
        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(len(heights)):
            pacific.add((i, 0))
            atlantic.add((i, len(heights[0]) - 1))  # FIXED

        for i in range(len(heights[0])):
            pacific.add((0, i))
            atlantic.add((len(heights) - 1, i))  # FIXED

        # CHANGED: Add each boundary cell to queue once
        q = collections.deque(pacific | atlantic)

        while q:
            island_row, island_col = q.popleft()

            for r, c in directions:
                next_r, next_c = r + island_row, c + island_col

                if (0 <= next_r < len(heights)) and \
                   (0 <= next_c < len(heights[0])) and \
                   heights[next_r][next_c] >= heights[island_row][island_col]:

                    added = False  # ADDED

                    # CHANGED: Check neighbor hasn't reached Pacific
                    if (island_row, island_col) in pacific:
                        if (next_r, next_c) not in pacific:
                            pacific.add((next_r, next_c))
                            added = True

                    # CHANGED: Check neighbor hasn't reached Atlantic
                    if (island_row, island_col) in atlantic:
                        if (next_r, next_c) not in atlantic:
                            atlantic.add((next_r, next_c))
                            added = True

                    # CHANGED: Only enqueue if new reachability found
                    if added:
                        q.append((next_r, next_c))

        results = []
        for key in atlantic:
            if key in pacific:
                results.append([key[0], key[1]])

        return results