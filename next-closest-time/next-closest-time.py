class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        # Split the times into hours and minutes
        hours, minutes = time.split(":")
        
        # Generate all possible combinations of numbers
        # Because there's only 4 numbers and 2 digit combos, we have a max of 16 combos
        temp = hours + minutes
        combo = [a+b for a in temp for b in temp]
        # Sort for ease - makes it n log n but can do it without sorting, too
        combo.sort()
        
        # Check for the next highest minute
        for x in range(len(combo)):
            # If it's over 60, we can just toss it here to save time because we won't ever use it
            if int(combo[x]) > 60:
                combo = combo[:x]
                break
            # If we find something in the same minute, return it because that's our answer
            if int(combo[x]) > int(minutes) and int(combo[x]) < 60:
                return hours + ":" + combo[x]
                
        # If highest minute is in next hour:
        for x in combo:
            # Check if valid
            if int(x) > int(hours) and int(x) < 24:
                # We return the found hour with the first occurrence of combo because that's the smallest minute
                return x + ":" + combo[0]
            
        # Otherwise, we check for next day - which should just be combo[0]:combo[0]
        return combo[0] + ":" + combo[0]
    
        # We can optimize this code by realizing that one of the combos will be the current minutes/hours
        # So we can search for the index of it and do index + 1, as that will be the next possible value
        # This way, we don't have to loop through the entire thing.