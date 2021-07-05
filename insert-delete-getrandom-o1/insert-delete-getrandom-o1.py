from random import choice
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.table = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.table:
            return False
        
        self.table[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.table:
            # In order to do this in O(1) time, we can swap the position of the element in the array to the end
            # and then pop it from there
            idx = self.table[val]
            last = self.arr[-1]
            # Swap
            self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
            # Update index of the last item to its new place
            self.table[last] = idx
            # pop
            self.arr.pop()
            del self.table[val]
            return True
        
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()