#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @param size int整型
# @return int整型一维数组
#
from collections import deque
from typing import List


class Solution:
    def maxInWindows(self, num: List[int], size: int) -> List[int]:
        # write code here
        if size == 0 or size > len(num):
            return []
        tempList = deque()
        res = []
        for i in range(size):
            tempList.append(num[i])
        res.append(max(tempList))
        j = 0
        for i in range(size, len(num)):
            tempList.popleft()
            tempList.append(num[i])
            res.append(max(tempList))
            j += 1

        return res
