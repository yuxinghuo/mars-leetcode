# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # 特殊情况判断
        if len(rotateArray) == 0:
            return 0
        # 左右指针
        i, j = 0, len(rotateArray) - 1
        while i < j:
            # 确定中点索引
            m = (i + j) // 2
            # m在左排序数组中，旋转点在 [m+1, j] 中
            if rotateArray[m] > rotateArray[j]:
                i = m + 1
            # m在右排序数组中，旋转点在 [i, m] 中
            elif rotateArray[m] < rotateArray[j]:
                j = m
            else:
                j -= 1
        # 返回结果
        return rotateArray[i]

    def minNumberInRotateArray1(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        i, j = 0, len(rotateArray)-1
        while i < j:
            m = (i + j) // 2
            if rotateArray[m] > rotateArray[j]:
                i = m + 1
            elif rotateArray[m] < rotateArray[j]:
                j = m
            else:
                j -= 1

        return rotateArray[i]
