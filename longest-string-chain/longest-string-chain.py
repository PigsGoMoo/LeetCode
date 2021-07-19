from functools import lru_cache
import collections
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        # Make a graph of all words and possibilities
        # If a word is abc, for example, that means it can come from
        # bc, ac, or ab as a precursor. We can map that so that each of the
        # characters are a wild card and use BFS/DFS to search upwards
        # For example, ab will move up to make *ab, a*b, or ab*
        # We'd search our graph for any of those three and continue BFS or DFS on it, keeping track
        # of depth in the process. 
        # Use memoization to prevent recalculations
        
        @lru_cache
        def dfs(s, depth):
            # print("Starting dfs. Currently at depth {} with word {}".format(depth, s))
            ans = depth
            for i in range(len(s) + 1):
                nxt = s[:i] + "*" + s[i:]
                # print("Next in sequence is: {}".format(nxt))
                if nxt in table:
                    # print("{} found in table".format(nxt))
                    for word in table[nxt]:
                        # print("Going futher down in dfs into depth of {}".format(depth + 1))
                        ans = max(ans, dfs(word, depth + 1))
                        # print("Back at depth {} with an ans of {}. Moving onto word after {}".format(depth, ans, word))
                        
            
            # print("Returning {}".format(depth))            
            return ans
        
        
        table = collections.defaultdict(list)
        for word in words:
            for i in range(len(word)):
                table[word[:i] + "*" + word[i + 1:]].append(word)
        
        # print(table)
        ans = 0
        for word in words:
            # print("Checking dfs on word: {}".format(word))
            ans = max(ans, dfs(word, 1))
            
        return ans
        