#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
from typing import List


class Solution:
    def reOrderArrayTwo(self, array: List[int]) -> List[int]:
        # write code here
        i, j = 0, len(array)-1
        while i < j:
            if array[i] % 2 == 0 and array[j] % 2 == 1:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
                i += 1
                j -= 1
                continue
            if array[i] % 2 == 1:
                i += 1
            if array[j] % 2 == 0:
                j -= 1
        return array
