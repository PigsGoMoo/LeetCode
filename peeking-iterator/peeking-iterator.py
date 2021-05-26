# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

# class PeekingIterator:
#     def __init__(self, iterator):
#         """
#         Initialize your data structure here.
#         :type iterator: Iterator
#         """
        
#         self.val = iterator
#         self.next = iterator.next()
        

#     def peek(self):
#         """
#         Returns the next element in the iteration without advancing the iterator.
#         :rtype: int
#         """
#         return self.next
        

#     def next(self):
#         """
#         :rtype: int
#         """
#         if self.hasNext():
#             ans = self.val
#             self.val = self.next
#             self.next = self.next.next()
#             return ans
#         else:
#             return None
        

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return self.next is not None

class PeekingIterator:
    def __init__(self, iterator):
        self._next = iterator.next()
        self._iterator = iterator

    def peek(self):
        return self._next

    def next(self):
        if self._next is None:
            raise StopIteration()
        to_return = self._next
        self._next = None
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        return to_return

    def hasNext(self):
        return self._next is not None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].