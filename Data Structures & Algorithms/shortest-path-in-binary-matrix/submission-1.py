class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        N = len(grid)

        # no path from (0, 0) to (N - 1)(N - 1) possible
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1

        # start top left (0, 0)
        q = deque([(0, 0, 1)])
        visited = set((0, 0))
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        while q:
            r, c, length = q.popleft()

            # end bottom right (N - 1, N - 1)
            if r == N -1 and c == N - 1:
                return length
            
            # search all directions
            for dr, dc in directions:
                row, col = r + dr, c + dc
                # must be unvisited empty path  
                if (0 <= row < N and 0 <= col < N 
                    and grid[row][col] == 0 and (row, col) not in visited):
                    q.append((row, col, length + 1))
                    visited.add((row, col))

        return -1
        