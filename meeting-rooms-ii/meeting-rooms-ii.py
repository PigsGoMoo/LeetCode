class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # We can solve this by increasing number of rooms whenever we start one before another one ends
        # This can be done by separating the start and end times into their own arrays
        # If the next start time in sequence starts before the very next one ends, we need another room
        
        # Edge case
        if not intervals:
            return 0
        
        # Initialize ans
        used_rooms = 0
        
        # Make our sorted array of start and end times
        start_times = [s for s, e in intervals]
        end_times = [e for s, e in intervals]
        start_times.sort()
        end_times.sort()
        
        # Initialize pointers
        start_ptr = 0
        end_ptr = 0
        
        # Iterate through the start times
        while start_ptr < len(start_times):
            start = start_times[start_ptr]
            end = end_times[end_ptr]
            # If start time comes after the end time, we don't need to increment used rooms
            # However, since we're incrementing every time, we'll just decrement so that net is 0
            if start >= end:
                used_rooms -= 1
                # We also need to increment end pointer cuz one ended here
                end_ptr += 1
                
            # Increment used_rooms and the start pointer every time
            used_rooms += 1
            start_ptr += 1
            
        return used_rooms