#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @param sum int整型
# @return int整型一维数组
#
from typing import List


class Solution:
    def FindNumbersWithSum(self, array: List[int], sum: int) -> List[int]:
        # write code here
        mp = dict()
        for i in array:
            if mp.get(sum - i):
                return [mp[sum - i], i]
            if not mp.get(i):
                mp[i] = i
        return []
