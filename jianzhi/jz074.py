#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param sum int整型
# @return int整型二维数组
#
from typing import List


class Solution:
    def FindContinuousSequence(self, sum: int) -> List[List[int]]:
        # write code here
        if sum == 1:
            return []
        i, j = 1, 1
        res = []

        tempSum = 1
        while i <= sum // 2 + 1 and j <= sum // 2 + 1:

            if tempSum == sum:
                tempList = [p for p in range(i, j + 1)]
                res.append(tempList)
                tempSum = tempSum - i
                i += 1
            elif tempSum < sum:
                j += 1
                tempSum = tempSum + j
            else:
                tempSum = tempSum - i
                i += 1
        return res
