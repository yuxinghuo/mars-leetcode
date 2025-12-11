#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
from typing import List


class Solution:
    def MoreThanHalfNum_Solution(self, numbers: List[int]) -> int:
        # write code here
        hm = dict()
        for i in numbers:
            if hm.get(i):
                hm[i] += 1
            else:
                hm[i] = 1

            if hm[i] > len(numbers) // 2:
                return i
        return 0
