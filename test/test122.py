from typing import List
import functools

# 将给定的整数数组重新排列，使得将它们连接起来组成一个最小的数字

class Solution:
    def PrintMinNumber(self, numbers: List[int]) -> str:
        lst = [str(i) for i in numbers]
        lst = list(map(lambda a: str(a), numbers))
        cmp = lambda a, b: 1 if a + b > b + a else -1
        lst.sort(key=functools.cmp_to_key(cmp))
        return "".join(lst)


def main():
    solution = Solution()

    # 测试用例1
    numbers1 = [3, 32, 321]
    print(solution.PrintMinNumber(numbers1))  # 预期输出: "321323"

    # 测试用例2
    numbers2 = [10, 2]
    print(solution.PrintMinNumber(numbers2))  # 预期输出: "102"

    # 测试用例3
    numbers3 = [1, 20, 5, 9]
    print(solution.PrintMinNumber(numbers3))  # 预期输出: "12059"

    # 测试用例4 (空列表)
    numbers4 = []
    print(solution.PrintMinNumber(numbers4))  # 预期输出: ""

    # 测试用例5 (单个数字)
    numbers5 = [42]
    print(solution.PrintMinNumber(numbers5))  # 预期输出: "42"


if __name__ == "__main__":
    main()
