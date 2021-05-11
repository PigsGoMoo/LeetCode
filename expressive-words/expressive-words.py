class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        # Edge cases
        if not s or not words:
            return 0
        
        ans = 0
        # print("Checking for stretchies for word: {}".format(s))
        for word in words:
            viable = True
            s_left = s_right = 0
            left = right = 0
            # print("Word: {}".format(word))
            while s_right < len(s) and right < len(word):
                # Save the letter
                s_char = s[s_right]
                word_char = word[right]
                # print("First characters: {} and {}".format(s_char, word_char))
                
                # If they're not the same, exit
                if s_char != word_char:
                    # print("Not same. Exiting..")
                    viable = False
                    break
                
                # Increase the window for both sides until reach different char
                # print("Char same...time to increase window size")
                while s_right < len(s) and s[s_right] == s_char:
                    s_right += 1
                    
                s_right -= 1
                
                while right < len(word) and word[right] == word_char:
                    right += 1
                    
                right -= 1
                # print("Window size ended at {} and {}".format(s_right, right))
                
                # Compare sizes
                s_window_size = s_right - s_left + 1
                word_window_size = right - left + 1
                # print("Time to compare sizes: {} vs {}".format(s_window_size, word_window_size))
                # If word is bigger, it's not viable. If s is bigger but not >= 3, also not viable. 
                if word_window_size > s_window_size or (s_window_size > word_window_size and s_window_size < 3):
                    # print("Not viable sizes. Exiting...")
                    viable = False
                    break
                
                # Now increment left and right to hit the next char
                s_left = s_right = s_right + 1
                left = right = right + 1
                # print("Seems to pass. Next window will start at {} and {}".format(s_left, left))
            
            if s_right == len(s) and right == len(word) and viable:
                # print("Viable answer. +1")
                ans += 1
                
        return ans
                