class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.store[key]

        left, right = 0, len(values) - 1
        while left <= right:
            m = left + (right - left) // 2
            # include most recent timestamp
            if values[m][0] <= timestamp:
                res = values[m][1]
                left = m + 1
            else:
                right = m - 1

        return res

        
