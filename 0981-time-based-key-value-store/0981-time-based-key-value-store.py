class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = [(value, timestamp)]
        else:
            self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.dic:
            l = 0
            r = len(self.dic[key]) - 1
            
            while l <=r:
                mid = (l+r)//2
                if self.dic[key][mid][1] == timestamp:
                    return self.dic[key][mid][0]
                elif self.dic[key][mid][1] < timestamp:
                    res = self.dic[key][mid][0]
                    l = mid+1
                else:
                    r = mid-1
        return res
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)