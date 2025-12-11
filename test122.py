import functools
from typing import List


class Solution:
    def PrintMinNumber(self, numbers: List[int]) -> str:
        lst = [str(i) for i in numbers]
        lst = list(map(lambda a: str(a), numbers))
        cmp = lambda a, b: 1 if a + b > b + a else -1
        lst.sort(key=functools.cmp_to_key(cmp))
        return "".join(lst)
