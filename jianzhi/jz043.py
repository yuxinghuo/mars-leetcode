#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def NumberOf1Between1AndN_Solution(self, n: int) -> int:
        res = 0
        # MulBase = 10^i
        MulBase = 1
        # 每位数按照公式计算
        i = 0
        while MulBase <= n:
            i += 1
            # 根据公式添加
            res += (n // (MulBase * 10)) * MulBase + min(
                max(n % (MulBase * 10) - MulBase + 1, 0), MulBase
            )
            # 扩大一位数
            MulBase *= 10
        return res
