#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return bool布尔型
#
from typing import List


class Solution:
    def IsContinuous(self, numbers: List[int]) -> bool:
        # write code here
        numbers = sorted(numbers)
        list1 = list(filter(lambda i: i != 0, numbers))
        zeroCount = len(numbers) - len(list1)
        count = 0
        for i in range(len(list1) - 1):
            if list1[i] == list1[i + 1]:
                return False
            else:
                count += list1[i + 1] - list1[i] - 1
        if zeroCount>=count:
            return True
        else:
            return False


solution = Solution()
solution.IsContinuous([0, 3, 2, 3, 4])
