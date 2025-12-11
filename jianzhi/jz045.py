#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return string字符串
#
from typing import List
import functools


class Solution:
    def PrintMinNumber(self, numbers: List[int]) -> str:
        # write code here
        list1 = list(map(lambda a: str(a), numbers))
        # 重载比较大小
        cmp = lambda a, b: 1 if a + b > b + a else -1
        # 排序
        list1.sort(key=functools.cmp_to_key(cmp))
        return "".join(list1)
