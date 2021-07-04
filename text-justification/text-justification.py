class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Count the length of next word
        # If remaining available space is less than length, we can add that to the line
        # If remaining == maxWidth (aka first word), we don't add extra character space
        # if not, we add one space then look at length of next word
        # If it fits, add that and repeat until out of width
        # When we find a word that doesn't fit, we start to make our justification
        # For each remaining character, add a space after each word except last
        # Then generate the sentence and add to ans array
        # repeat until we're at end of words
        # For the line that contains the last word, we don't justify. Just add spaces
        # at the end til we hit width
        
        ptr = 0
        
        ans = []
        # Start our iteration
        while ptr < len(words):
            # For each line, we'll keep track of how many remaining variables
            remaining = maxWidth
            line = []
            # And while we have space left
            while ptr < len(words) and remaining - len(words[ptr]) >= 0:
                # Add word to line
                line.append(words[ptr])
                # If first word, don't add space before. If not first word, add space
                if remaining != maxWidth:
                    remaining -= 1
                # Remove length of this word from remaining
                remaining -= len(words[ptr])
                
                if remaining < 0:
                    line.pop()
                    remaining += len(words[ptr]) + 1
                    break
                # increment pointer
                ptr += 1
            
            # Outside that while loop is when we have our line. Now to add the right amount of spaces
            # We need one less space than words (cuz last word doesn't have a space after)
            if ptr < len(words):
                spaces = [' '] * (len(line) - 1)
                # Now for each remaining, we evenly distribute spaces until we run out
                if len(line) > 1:
                    extra = remaining // len(spaces)
                    remainder = remaining % len(spaces)
                # If line only has one word, we add spaces equal to the remaining characters in the line
                else:
                    spaces = ['']
                    remainder = 0
                    extra = remaining
                    
                for i in range(len(spaces)):
                    spaces[i] += ' ' * extra
                    if i + 1 <= remainder:
                        spaces[i] += ' '
                        
            # If we've reached the last line
            else:
                # Then we add only one space
                spaces = [' '] * len(line)
                spaces[-1] *= remaining
                    
            temp = ''
            for i in range(len(line)):
                temp += line[i]
                if i < len(spaces):
                    temp += spaces[i]
                    
            ans.append(temp)
            
        return ans
