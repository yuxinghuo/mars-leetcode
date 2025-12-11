#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 解码
# @param nums string字符串 数字串
# @return int整型
#
class Solution:
    def solve(self, nums: str) -> int:
        if nums == "0":
            return 0
        if nums == "10" or nums == "20":
            return 1
        for i in range(1,len(nums)):
            if nums[i] == "0":
                if nums[i - 1] != "1" and nums[i - 1] != "2":
                    return 0
        dp = [1 for i in range(len(nums) + 1)]
        for i in range(2, len(nums)+1):
            if (nums[i - 2] == "1" and nums[i - 1] != "0") or (nums[i - 2] == "2" and nums[i - 1] > "0" and nums[i - 1] < "7"):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[len(nums)]
