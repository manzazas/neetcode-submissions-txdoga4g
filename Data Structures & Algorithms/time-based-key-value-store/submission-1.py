class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((timestamp,value))
        else:
            self.time_map[key] = [(timestamp,value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        

        search = self.time_map[key]

        l = 0
        res = -1
        r = len(search) - 1
        while l <= r:
            m = (l + r) // 2
            if search[m][0] <= timestamp:
                
                res = m
                l = m + 1
            else:
                r = m - 1

        if res == -1:
            return ""

        return self.time_map[key][res][1]
        
