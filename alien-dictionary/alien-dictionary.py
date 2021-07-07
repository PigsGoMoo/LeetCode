class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Looks like a graphing question
        # We evaluate the words starting with the first letter
        # The first letter of the words will be in its order
        # Then we compare all words with same first letter
        # get the order of the second characters
        # continue until can't compare anymore
        # Now we have our ordering, in the form of a graph
        # Start a queueueueueue. If indegree == 0, add to queueueueue
        # for each item in queueueueue, add it to ans array
        # then remove it from graph by reducing the indegree of all of its adjacent letters
        
        # Initialize
        adj_list = collections.defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}
        
        # We only need to compare the two words next to each other
        # and check the first character that isn't equal
        for first, second in zip(words, words[1:]):
            for a, b in zip(first, second):
                # When we hit the first set of characters that aren't equal
                if a != b:
                    # Check if already in our list
                    if b not in adj_list[a]:
                        # Add to list
                        adj_list[a].add(b)
                        # Increase in-degree
                        in_degree[b] += 1
                        
                    # then we can move onto next word cuz we know rest of this can't be compared
                    break
            # Edge case
            # If the for loop goes to completion, that means the characters are all equal for the shorter word
            # If this is the case, we need to make sure that the first word is longer than the second
            # (aka the first word is a prefix of the second). If it's the other way around, it's an invalid
            # input
            else: 
                if len(second) < len(first):
                    return ""
                
        # Now we need to go through and use topological sorting
        ans = []
        # Initialize our queueueueue with everything that has an indegree of 0
        q = collections.deque()
        for let in in_degree:
            if in_degree[let] == 0:
                q.append(let)
                    
        # Iterate through queueueueue
        while q:
            char = q.popleft()
            ans.append(char)
            
            for nei in adj_list[char]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
                        
        # When the while loop ends, we should have our answer.
        # Edge case: Make sure ans array has all the letters
        # If it doesn't, that means there's a cycle - thus invalid input
        if len(ans) < len(in_degree):
            return ""
            
        return "".join(ans)
