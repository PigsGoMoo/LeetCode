class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Brute force would be to recurse through every combination with backtracking to see if you get the 
        # possible outcome. This is 2^n complexity
        # Can be improved to n^3 with memoization because of multiple repeated recursive calls
        # Another method is to use bottom's up dynamic programming
        # Iterate the string from the bottom up and see if you can match a word with it
        # If you can, set that index of the string in the DP to true
        # Then continue. For each word in dictionary at any given substring length, we check if 
        # substring length minus word length in the DP is true (because this would be where the
        # last word would end and this one begins). If it isn't true, then we can't make a word from 
        # before this, so set this DP to false. 
        
        # Make it a set for O(1) lookup time
        words = set(wordDict) 
        # Initialize DP. First one is True
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        # Iterate through the length of s, starting from 1 to the end + 1
        for i in range(1, len(s) + 1):
            # Check each word
            for word in words:
                # If word length fits in current substring length, i
                if len(word) <= i:
                    # Find out where word would begin if put at end of substring
                    j = i - len(word)
                    # Check if dp[j], which is whether or not words can fit up to index j in string s, is true
                    # If it's true, that means the substring before this current word is in our word list
                    # Then make sure the substring matches the current word
                    if dp[j] and s[j:i] == word:
                        # If both of these are true, we set this current index to true
                        dp[i] = True
        # Return very last index
        return dp[-1]
        