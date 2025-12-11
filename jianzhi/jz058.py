#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @param n int整型
# @return string字符串
#
class Solution:
    def LeftRotateString(self, str: str, n: int) -> str:
        # write code here
        if len(str) == 0:
            return ""
        n = n % len(str)
        return str[n:] + str[0:n]

from typing import List
class Solution:
    # 反转函数
    def reverse(self, s: List, start: int, end: int):
        while start < end:
            self.swap(s, start, end)
            start += 1
            end -= 1

    # 交换函数
    def swap(self, s: List, a: int, b: int):
        temp = s[a]
        s[a] = s[b]
        s[b] = temp

    def LeftRotateString(self, str: str, n: int) -> str:
        # 取余，因为每次长度为n的旋转数组相当于没有变化
        s = list(str)
        m = len(s)
        if m == 0:
            return ""
        n = n % m
        # 第一次逆转全部元素
        self.reverse(s, 0, m - 1);
        # 第二次只逆转开头m个
        self.reverse(s, 0, m - n - 1)
        # 第三次只逆转结尾m个
        self.reverse(s, m - n, m - 1)
        return ''.join(s)

