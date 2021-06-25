class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Idea is to sort by position because cars can't pass
        # Then make an array of how long it takes the furthest car to get to destination
        # that's one fleet
        # Then figure out the time for the next car in list
        # If less than previous, then it's added into previous fleet because that would mean it has to pass
        # So don't count that as a fleet. Time is gonna equal to previous time
        # Keep going down list til end. Times should increase
        # Answer will be number of unique arrival times
        
        # Cars array will be positions and speed values of each car in descending order
        cars = [[pos, vel] for pos, vel in zip(position, speed)]
        
        cars.sort(reverse=True)
        
        ans = []
        
        # Iterate through and calculate time it takes to reach target from furthest car
        for pos, sp in cars:
            # Calculate time it takes to reach end
            time = (target - pos) / sp
            # If this time is faster or equal to the last one, the answer is the last one
            if ans and time <= ans[-1]:
                ans.append(ans[-1])
            # else, this is a unique time, so we just add it
            else:
                ans.append(time)
                
        # Our answer is the number of unique times in ans
        return len(set(ans))
            