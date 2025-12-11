#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def FindGreatestSumOfSubArray(self , array: List[int]) -> List[int]:
        # write code here
        dp=[0 for i in range(len(array))]
        dp[0]=array[0]
        maxsum=dp[0]
        left=0
        right=0
        resl=0
        resr=0
        for i in range(1,len(array)):
            right+=1
            dp[i]=max(dp[i-1]+array[i],array[i])
            if dp[i-1]+array[i]<array[i]:
                left =right
            if dp[i]>maxsum or dp[i]==maxsum and (right-left+1)>(resr-resl+1):
                maxsum=dp[i]
                resl=left
                resr=right
        return array[resl:resr+1]