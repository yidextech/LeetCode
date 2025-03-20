class MyHashMap:

    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        self.get(key)
        if self.exists:
            self.hashMap[self.valueIndex][1] = value
        else:
            self.hashMap.append([key, value])
        
    def get(self, key: int) -> int:

        self.exists = False
        for i in range(len(self.hashMap)):
            if key == self.hashMap[i][0]:
                self.valueIndex = i
                self.exists = True
                return self.hashMap[i][1]
        return -1

    def remove(self, key: int) -> None:
        self.get(key)
        if self.exists:
            self.hashMap.pop(self.valueIndex)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)