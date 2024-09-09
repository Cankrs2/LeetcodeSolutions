class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        values = counter.values()
        set_values = set(values)
        return len(set_values) == len(values)