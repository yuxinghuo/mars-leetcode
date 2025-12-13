from collections import deque

if __name__ == '__main__':
    list1 = [1, 4, 3, 5, 3, 2, 5]
    list2 = [i for i in list1 if i > 3]
    list3 = [1, 4, 3, 5, 3, 2, 5]
    list4 = list(filter(lambda x: x > 3, list3))
    print(list2)
    print(list4)

    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")  # Terry arrives
    queue.append("Graham")  # Graham arrives
    queue.popleft()  # The first to arrive now leaves
    queue.popleft()  # The second to arrive now leaves
    print(queue)
