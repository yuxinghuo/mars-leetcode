list1 = [1, 2, 3, 4, 5, 6]
print(list1[-3:])

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
# print(tuple(result))
print(list(result))
map1 = {x: x+x for x in numbers}
print(map1)
