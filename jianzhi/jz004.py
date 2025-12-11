# JZ4 二维数组中的查找
from typing import List


def Find(self, target: int, array: List[List[int]]) -> bool:
    # 判断特殊
    if len(array) == 0:
        return False
    n = len(array)
    if len(array[0]) == 0:
        return False
    m = len(array[0])
    i, j = n - 1, 0
    while i >= 0 and j < m:
        if array[i][j]>target:
            i-=1
        elif array[i][j]<target:
            j+=1
        else:
            return True
    return False
