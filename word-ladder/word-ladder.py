class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # This is essentially a graph. We can use a dictionary to categorize all the one letter changes
        # of a word. We can use a separate dictionary to keep track of the words we've already visited - to prevent
        # any repeats. 
        # And we can use a queue to search the next possible group of numbers
        
        # Edge case
        if not endWord or not beginWord or not wordList or endWord not in wordList:
            return 0
        
        # All words will be of same length
        L = len(beginWord)
        
        # First make our dictionary of words
        combos = collections.defaultdict(list)
        
        # Iterate through each word
        for word in wordList:
            # We'll add it to the dictionary with the key where one letter is changed
            for i in range(L):
                # This will make the key as one empty value for each word.
                # If key is already made, it'll just add to the list
                # If first time seeing key, it'll make the new key and append to list.
                combos[word[:i] + "*" + word[i+1:]].append(word)
                
        # Now we use a queueue to go through each of the one-letter changes in a BFS manner
        # And initialize with the first word - our beginWord. The second part of the array is to keep track of 
        # the number of changes.
        # Deque in the collections library allows us to pop from either side of the list in O(1) time
        queue = collections.deque([(beginWord, 1)])
        
        # Initialize a set for visited values
        visited = set(beginWord)
        
        while queue:
            # Grab our word
            current_word, level = queue.popleft()
            
            # Change each letter and add each one-letter change to the queue. 
            # Return level + 1 if we've found endWord.
            for i in range(L):
                # Format of the single letter change for each char in current_word
                next_word = current_word[:i] + "*" + current_word[i + 1:]
                
                # Now find all values with this format and add to queueue
                for word in combos[next_word]:
                    # If word == endWord, return
                    if word == endWord:
                        return level + 1
                    
                    # Otherwise, add to queue + visited if we haven't seen yet
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                        
                # Then empty it so we don't go back to this point
                combos[next_word] = []
        # If we exit the while loop, that means we can't find a path
        return 0