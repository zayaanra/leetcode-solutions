class TimeMap:
    def __init__(self):
        self.timeMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        res = ""
        arr = self.timeMap[key]
        l, r = 0, len(arr)-1
        while l <= r:
            m = (l + r)//2
            value, timestamp_prev = arr[m]
            if timestamp_prev <= timestamp:
                l = m + 1
                res = value
            else:
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)