age = int(input("请输入你家狗狗的年龄: "))
from collections import deque

### 退出提示
input("点击 enter 键退出")

import re

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

import calendar

cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal)

if __name__ == '__main__':
    list1 = [1, 4, 3, 5, 3, 2, 5]
    list2 = [i for i in list1 if i > 3]
    list3 = [1, 4, 3, 5, 3, 2, 5]
    list4 = list(filter(lambda x: x > 3, list3))
    print(list2)
    print(list4)
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves