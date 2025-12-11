#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param sequence int整型一维数组
# @return bool布尔型
#
from typing import List
class Solution:
    def VerifySquenceOfBST(self , sequence: List[int]) -> bool:
        # write code here
        # -*- coding:utf-8 -*-
        #先判断数组是否为空
        if not sequence:
            return False
        s,root=[],999999
        for i in range(len(sequence)-1,-1,-1):
            if sequence[i]>root: return False
            while s and sequence[i]<s[-1]:
                root=s.pop()
            s.append(sequence[i])
        return True