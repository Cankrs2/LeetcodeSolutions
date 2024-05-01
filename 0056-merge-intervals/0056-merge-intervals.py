class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        j=1
        len_intervals = len(intervals)
        while i < len_intervals-1 or j < len_intervals or len_intervals>1:
            if j == len_intervals: break
            if intervals[i][1] >= intervals[j][0]:
                intervals[i][0] = min(intervals[i][0],intervals[j][0])
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                intervals.pop(j)
            else:
                i+=1
                j+=1
                
            len_intervals = len(intervals)    
            
        return intervals
                