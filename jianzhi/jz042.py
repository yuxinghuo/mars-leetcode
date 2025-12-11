#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型
#
from typing import List


class Solution:
    def FindGreatestSumOfSubArray(self, array: List[int]) -> int:
        # write code here
        sum1 = 0
        max1 = array[0]
        for i in array:
            sum1 = max(sum1 + i, i)
            max1 = max(max1, sum1)
        return max1

solution =Solution()
solution.FindGreatestSumOfSubArray(array=[1,-2,3])
