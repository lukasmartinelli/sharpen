# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

     def __repr__(self):
         return '({},{})'.format(self.start, self.end)

class Solution:
    
    def merge_intervals(self, a, b):
        return Interval(min(a.start, b.start), max(a.end, b.end))
        
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda i: i.start)
        if len(intervals) == 0:
            return intervals

        merged_intervals = [intervals.pop(0)]
        
        # O(n)
        while len(intervals) > 0:
            prev_interval = merged_intervals[-1]
            interval = intervals.pop(0)
            
            #if interval.start < prev_internal.start and interval.end < prev_internal.start
            if prev_interval.end >= interval.start:
                merged_intervals[-1] = self.merge_intervals(prev_interval, interval)
            else:
                merged_intervals.append(interval)
                
        return merged_intervals
        
# merged: [1,6],

#A = [ (47, 76), (51, 99), (28, 78), (54, 94), (12, 72), (31, 72), (12, 55), (24, 40), (59, 79), (41, 100), (46, 99), (5, 27), (13, 23), (9, 69), (39, 75), (51, 53), (81, 98), (14, 14), (27, 89), (73, 78), (28, 35), (19, 30), (39, 87), (60, 94), (71, 90), (9, 44), (56, 79), (58, 70), (25, 76), (18, 46), (14, 96), (43, 95), (70, 77), (13, 59), (52, 91), (47, 56), (63, 67), (28, 39), (51, 92), (30, 66), (4, 4), (29, 92), (58, 90), (6, 20), (31, 93), (52, 75), (41, 41), (64, 89), (64, 66), (24, 90), (25, 46), (39, 49), (15, 99), (50, 99), (9, 34), (58, 96), (85, 86), (13, 68), (45, 57), (55, 56), (60, 74), (89, 98), (23, 79), (16, 59), (56, 57), (54, 85), (16, 29), (72, 86), (10, 45), (6, 25), (19, 55), (21, 21), (17, 83), (49, 86), (67, 84), (8, 48), (63, 85), (5, 31), (43, 48), (57, 62), (22, 68), (48, 92), (36, 77), (27, 63), (39, 83), (38, 54), (31, 69), (36, 65), (52, 68) ]
#A = [Interval(a, b) for a, b in A]
#print('Solution', Solution().merge(A))
