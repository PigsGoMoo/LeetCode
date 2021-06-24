class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Use sliding window
        # We can preprocess an array of the first k values and the last k values
        # Then use a window of size k to iterate through and keep track of max value
        # Preprocessed array needs to be made so that the first k values and last k values
        # are in backward order
        # Ex: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] with k = 3
        # needs to be preprocessed to: [3, 2, 1, 10, 9, 8]
        # Because as you use less values in front and more values in back, it will appear in that order
        
        # Initialize
        n = len(cardPoints)
        
        preprocessed = cardPoints[k-1 : : -1] + cardPoints[n : n - k - 1: -1]
        window = preprocessed[0]
        left = right = 0
        
        # Expand window to size k
        for i in range(k-1):
            right += 1
            window += preprocessed[right]
        max_score = window
        
        # Move window + compare new score
        while right + 1 < len(preprocessed):
            # Remove left from window sum
            window -= preprocessed[left]
            # Move window
            left += 1
            right += 1
            # Add right
            window += preprocessed[right]
            
            max_score = max(window, max_score)
            
        return max_score
            
            