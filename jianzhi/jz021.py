#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
from typing import List


class Solution:
    def reOrderArray(self, array: List[int]) -> List[int]:
        # write code here
        list1 = []
        list2 = []
        for i in range(len(array)):
            if array[i] % 2 == 1:
                list1.append(array[i])
            else:
                list2.append(array[i])

        return list1+list2
