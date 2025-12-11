#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param index int整型
# @return int整型
#
class Solution:
    def GetUglyNumber_Solution(self, index: int) -> int:
        # write code here
        if index == 1:
            return 1
        count = 1
        i = 1
        while count < index:
            i += 1
            if self.ifnum(i):
                count += 1

        return i

    def ifnum(self, num: int):
        while num % 2 == 0: num = num / 2
        while num % 3 == 0: num = num / 3
        while num % 5 == 0: num = num / 5
        return num == 1


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param index int整型
# @return int整型
#
class Solution:
    def GetUglyNumber_Solution(self, index: int) -> int:
        # write code here
        if index <= 6:
            return index
        i2, i3, i5 = 0, 0, 0
        res = [i for i in range(index)]
        res[0] = 1
        for i in range(1, index):
            res[i] = min(res[i2] * 2, min(res[i3] * 3, res[i5] * 5))
            if res[i] == res[i2] * 2:
                i2 += 1
            if res[i] == res[i3] * 3:
                i3 += 1
            if res[i] == res[i5] * 5:
                i5 += 1
        return res[index - 1]


solution = Solution()
print(solution.GetUglyNumber_Solution(1500))
