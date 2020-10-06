class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket_length = 997
        self.bucket_array = [Bucket() for i in range(self.bucket_length)]

    def get_hash(self, val):
        return val % self.bucket_length

    def add(self, key: int) -> None:
        _hash = self.get_hash(key)
        self.bucket_array[_hash].insert(key)

    def remove(self, key: int) -> None:
        _hash = self.get_hash(key)
        self.bucket_array[_hash].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        _hash = self.get_hash(key)
        return self.bucket_array[_hash].exist(key)


class Node:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode


class Bucket:
    def __init__(self):
        # 头插法
        self.head = Node(0)

    def exist(self, val):
        pointer = self.head.next
        while pointer is not None:
            if pointer.val == val:
                return True
            pointer = pointer.next
        return False

    def insert(self, val):
        # 头插法
        if not self.exist(val):
            newNode = Node(val, self.head.next)
            self.head.next = newNode

    def delete(self, val):
        pre = self.head
        curr = self.head.next
        while curr is not None:
            if curr.val == val:
                pre.next = curr.next
                break
            pre = curr
            curr = curr.next

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
if __name__ == '__main__':
    # hashSet = MyHashSet()
    # hashSet.add(1)
    # hashSet.add(2)
    # print(hashSet.contains(1))
    # print(hashSet.contains(3))
    # hashSet.add(2)
    # print(hashSet.contains(2))
    # hashSet.remove(2)
    # print(hashSet.contains(2))
    array = [Bucket() for i in range(997)]
    array2 = [Bucket()] * 997
    print(len(array))
    print(len(array2))