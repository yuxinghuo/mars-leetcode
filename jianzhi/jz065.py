#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num1 int整型
# @param num2 int整型
# @return int整型
#
class Solution:
    def Add(self, num1: int, num2: int) -> int:
        # write code here
        while num2 != 0:  # 进位为0时，跳出循环
            sum = num1 ^ num2  # 非进位求和
            temp = (num1 & num2) << 1  # 计算出进位
            num1 = sum  # 非进位和
            num2 = temp  # 进位
        return num1
