#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pushV int整型一维数组
# @param popV int整型一维数组
# @return bool布尔型
#
from typing import List


class Solution:
    def IsPopOrder(self, pushV: List[int], popV: List[int]) -> bool:
        n = len(pushV)
        j = 0
        temp = []
        for i in range(n):
            while j < n and (len(temp) == 0 or temp[-1] != popV[i]):
                temp.append(pushV[j])
                j += 1
            if temp[-1] == popV[i]:
                temp.pop();
            else:
                return False
        return True
