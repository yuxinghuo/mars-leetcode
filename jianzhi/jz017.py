# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型 最大位数
# @return int整型一维数组
#
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        # write code here
        num = 0
        for i in range(n): num = num * 10 + 9
        return [i for i in range(1, num + 1)]
