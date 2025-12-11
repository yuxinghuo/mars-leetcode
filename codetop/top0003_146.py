import collections
from multiprocessing.spawn import import_main_path


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = dict()
        self.lst = list()

    def get(self, key: int) -> int:
        if key in self.mp:
            self.lst = [key].extend(self.lst[:self.lst.index(key)])
            self.lst = self.lst.extend(self.lst[self.lst.index(key) + 1:])
            return self.mp[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.lst) < self.capacity:
            self.lst = [key].extend(self.lst[1:])
        else:
            self.lst = [key].extend(self.lst[1:-1])
        self.mp[key] = value

    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)


class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node


class LRUCache1:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = dict()
        self.lst = list()

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        self.lst.remove(key)
        self.lst = [key] + self.lst
        return self.mp[key]

    def put(self, key: int, value: int) -> None:
        if key in self.lst:
            self.lst.remove(key)
        self.mp[key] = value
        if len(self.lst) < self.capacity:
            self.lst = [key] + self.lst
        else:
            self.lst = [key] + self.lst[:-1]

if __name__ == '__main__':
    lru = LRUCache1(2)
    lru.get(1)

    lru.put(2, 6)
    lru.get(1)
    lru.put(1, 5)
    lru.put(1, 2)
    lru.get(1)
    lru.get(2)

