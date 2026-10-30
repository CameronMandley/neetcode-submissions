class TimeMap:

    def __init__(self):
        self.keyvals = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyvals:
            self.keyvals[key] = [[timestamp, value]]
        else:
            self.keyvals[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyvals:
            return ""
        else:
            left, right = 0, len(self.keyvals[key]) - 1
            closest = [-1, ""]
            while left <= right:
                mid = (left + right) // 2
                if self.keyvals[key][mid][0] < timestamp:
                    closest = self.keyvals[key][mid]
                    left = mid + 1
                elif self.keyvals[key][mid][0] > timestamp:
                    right = mid - 1
                else:
                    return self.keyvals[key][mid][1]
            return closest[1]
        
