#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param number int整型 
# @return int整型
#
def cutRope( number: int) -> int:
    # write code here
    dp = [0 for i in range(number + 1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4, number + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * dp[i - j])
    return dp[number]

print(cutRope(8))