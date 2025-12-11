#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param grid int整型二维数组
# @return int整型
#
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # write code here
        rows = len(grid)
        lows = len(grid[0])
        for i in range(rows):
            for j in range(lows):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = max(grid[i][j - 1] + grid[i][j], grid[i - 1][j] + grid[i][j])
        return grid[rows-1][lows-1]
