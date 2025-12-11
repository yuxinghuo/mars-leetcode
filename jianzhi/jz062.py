#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @param m int整型
# @return int整型
#
class Solution:
    def LastRemaining_Solution(self, n: int, m: int) -> int:
        # write code here
        if n == 0 or m == 0:
            return -1
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x
