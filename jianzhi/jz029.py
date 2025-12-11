#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix int整型二维数组
# @return int整型一维数组
#
from typing import List

class Solution:
    def printMatrix(self , matrix: List[List[int]]) -> List[int]:
        res = list()
        n = len(matrix)
        #先排除特殊情况
        if n == 0:
            return res
        #左边界
        left = 0
        #右边界
        right = len(matrix[0]) - 1
        #上边界
        up = 0
        #下边界
        down = n - 1
        #直到边界重合
        while left <= right and up <= down:
            #上边界的从左到右
            for i in range(left, right+1):
                res.append(matrix[up][i])
            #上边界向下
            up += 1
            if up > down:
                break
            #右边界的从上到下
            for i in range(up,down+1):
                res.append(matrix[i][right])
            #右边界向左
            right -= 1
            if left > right:
                break
            i = right
            #下边界的从右到左
            while i >= left:
                res.append(matrix[down][i])
                i -= 1
            #下边界向上
            down -= 1
            if up > down:
                break
            i = down
            #左边界的从下到上
            while i >= up:
                res.append(matrix[i][left])
                i -= 1
            #左边界向右
            left += 1
            if left > right:
                break
        return res

