class TimeMap:

    def __init__(self):
        self.store = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: 
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        lo, hi = 0, len(values)-1
        while(lo<=hi):
            mid = (lo+hi)//2 
            if values[mid][1] <=timestamp:
                res = values[mid][0]
                lo = mid+1
            else:
                hi = mid-1
        return res