class TimeMap:

    def __init__(self):
        self.nums = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        new_element = []
        new_element.append(key)
        new_element.append(value)
        new_element.append(timestamp)
        self.nums.append(new_element)

        
    def get(self, key: str, timestamp: int) -> str:
        index = -1
        while index*-1 <= len(self.nums):
            if self.nums[index][0] == key and self.nums[index][2] <= timestamp:
                return self.nums[index][1]
            index -= 1 
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)