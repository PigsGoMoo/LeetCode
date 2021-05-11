class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        mapper = {}
        
        first_zero = 0
        for idx, char in enumerate(seats):
            # If first zero found
            if char == 0 and (seats[idx - 1] == 1 or idx == 0):
                # Edge case: If the edge of the row is 0, we need to double it for the calculation
                mapper[idx] = 1 if idx != 0 else 2
                first_zero = idx
                
            # If this is a continuing zero
            elif char == 0 and seats[idx - 1] == 0:
                # Edge case: Same as above
                mapper[first_zero] += 1 if first_zero != 0 else 2
                # Other edge case: If it's zero all the way to the end of the row, also double
                if idx == len(seats) - 1:
                    mapper[first_zero] *= 2
                
        space = max(mapper.values())
        
        return (space + 1) // 2