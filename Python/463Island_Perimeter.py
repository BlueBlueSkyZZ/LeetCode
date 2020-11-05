from typing import List



class Solution:
    neighbour = 0
    island_count = 0

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        length = len(grid)
        visit = [[0 for i in range(width)] for j in range(length)]

        def dfs(i, j):
            if i < 0 or i >= length or j < 0 or j >= width:
                return
            visit[i][j] = 1
            self.island_count += 1
            if i-1 >= 0 and grid[i-1][j] == 1 and visit[i-1][j] == 0:
                self.neighbour += 1
                dfs(i-1, j)
            if i+1 < length and grid[i+1][j] == 1 and visit[i+1][j] == 0:
                self.neighbour += 1
                dfs(i+1, j)
            if j-1 >= 0 and grid[i][j-1] == 1 and visit[i][j-1] == 0:
                self.neighbour += 1
                dfs(i, j-1)
            if j+1 < width and grid[i][j+1] == 1 and visit[i][j+1] == 0:
                self.neighbour += 1
                dfs(i, j+1)

        for i in range(length):
            if self.island_count > 0:
                break
            for j in range(width):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
        print(self.island_count, self.neighbour)
        return 4 * self.island_count - 2 * self.neighbour

    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        length = len(grid)
        result = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    if i-1 < 0 or grid[i-1][j] == 0:
                        result += 1
                    if i+1 >= length or grid[i+1][j] == 0:
                        result += 1
                    if j-1 < 0 or grid[i][j-1] == 0:
                        result += 1
                    if j+1 >= width or grid[i][j+1] == 0:
                        result += 1
        return result

if __name__ == '__main__':
    grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    grid = [[1, 0]]
    grid = [[0, 1]]
    grid = [[1, 1], [1, 1]]
    solution = Solution()
    print(solution.islandPerimeter(grid))
