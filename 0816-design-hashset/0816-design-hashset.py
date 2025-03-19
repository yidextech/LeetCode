class MyHashSet:

    def __init__(self):
        self.hashSet = []
    def add(self, key: int) -> None:
        if not(self.contains(key)):
            self.hashSet.append(key)
    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashSet.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hashSet:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)