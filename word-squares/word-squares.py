class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # Can do this with backtracking 
        # Idea is that we backtrack through each possibility
        # We can make it more efficient by pre-processing all prefixes beforehand
        # This way, we won't need to search through the array of words every time in search for prefix
        
        # All words are same length
        n = len(words[0])
        
        def backtrack(step, word_square, n):
            # Base case - if we've found solution
            if step == n:
                ans.append(word_square[:])
                return
            
            prefix = "".join([word[step] for word in word_square])
            
            # Base case - if we've hit a prefix that doesn't exist in the hash
            if prefix not in self.prefix_hash:
                return
            
            # Otherwise, iterate through hash
            for candidate in self.prefix_hash[prefix]:
                word_square.append(candidate)
                backtrack(step + 1, word_square, n)
                word_square.pop()
        
        
        # Initialize array
        ans = []
        # Preprocess words
        self.preprocess(words, n)
        # Backtrack through possibilities
        for word in words:
            word_square = [word]
            backtrack(1, word_square, n)
            
        return ans
            
        
    def preprocess(self, words, n):
        # Initialize hash
        self.prefix_hash = collections.defaultdict(list)
        
        for word in words:
            for i in range(1, n):
                prefix = word[:i]
                self.prefix_hash[prefix].append(word)
                
        