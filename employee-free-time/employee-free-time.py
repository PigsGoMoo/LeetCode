"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Grab intervals
        # Sort intervals
        # Combine intervals
        # Loop through combined and add [combined[i][1], combined[i + 1][0]] to ans
        
        # Grab intervals
        sched = []
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                sched.append([schedule[i][j].start, schedule[i][j].end])
                
        # Sort
        sched.sort()
        
        # Combine
        intervals = []
        
        for time in sched:
            
            if not intervals or intervals[-1][1] < time[0]:
                intervals.append(time)
                
            else:
                intervals[-1][1] = max(intervals[-1][1], time[1])
        
        
        # Loop through and make ans
        ans = []
        for i in range(len(intervals)):
            # If not last one
            if i+1 < len(intervals):
                ans.append(Interval(intervals[i][1], intervals[i + 1][0]))

        return ans
                