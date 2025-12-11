#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param prices int整型一维数组
# @return int整型
#
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # write code here
        if len(prices) <= 1:
            return 0
        i, j = 0, 1
        maxValue = 0
        while i < len(prices) and j < len(prices):
            if prices[i] < prices[j]:
                maxValue = max(maxValue,prices[j] - prices[i])
                j += 1
            else:
                i = j
                j += 1
        return maxValue

