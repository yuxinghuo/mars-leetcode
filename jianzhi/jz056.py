#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
from typing import List


class Solution:
    def FindNumsAppearOnce(self, array: List[int]) -> List[int]:
        # write code here
        mp = dict()
        for i in array:
            if not mp.get(i):
                mp[i] = 1
            else:
                mp[i] += 1
        res = []
        for key, value in mp.items():
            if value == 1:
                res.append(key)
        return sorted(res)

    def FindNumsAppearOnce1(self, array: List[int]) -> List[int]:
        # write code here
        tmp = 0
        for i in array:
            tmp = i ^ tmp
        mask = 1
        while (tmp & mask) == 0:
            mask = mask << 1
        a, b = 0, 0
        for i in array:
            if (i & mask) == 0:
                a = a ^ i
            else:
                b = b ^ i
        if a > b:
            c = a
            a = b
            b = c
        return [a, b]

solution =Solution()
solution.FindNumsAppearOnce1([1,1,4,6])
