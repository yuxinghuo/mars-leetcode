class Solution:
    def __init__(self):
        self.mod = 998244353

    # 快速乘法
    def fast(self, x: int, y: int) -> int:
        res = 0
        x %= self.mod
        y %= self.mod
        while y:
            if y & 1:
                # 加法代替乘法，防止越界
                res += x
                if res >= self.mod:
                    res -= self.mod
            y = y >> 1
            x = x << 1
            if x >= self.mod:
                x -= self.mod
        return res

    # 快速幂
    def Pow(self, x: int, y: int) -> int:
        res = 1
        while y:
            # 可以再往上乘一个
            if y & 1:
                res = self.fast(res, x)
            # 叠加
            x = self.fast(x, x)
            # 减少乘次数
            y = y >> 1
        return res

    def cutRope(self, number: int) -> int:
        # 不超过3直接计算
        if number <= 3:
            return number - 1
        # 能整除3
        if number % 3 == 0:
            return self.Pow(3, number // 3)
        # 最后剩余1
        elif number % 3 == 1:
            # 4*3^{n-1}
            return self.fast(self.Pow(3, number // 3 - 1), 4)
        # 最后剩余2
        else:
            # 2*3^n
            return self.fast(self.Pow(3, number // 3), 2)
