from typing import List
# JZ3 数组中重复的数字
def duplicate(numbers: List[int]) -> int:
    coll=set();
    for i in numbers:
        if i in coll:
            return i
        else:
            coll.add(i)
    return -1


if __name__ == '__main__':
    a=duplicate(numbers=[1,2,4,7,3,2,1,4])
    print(a)
