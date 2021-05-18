class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.table = collections.defaultdict(list)
        
        for word in dictionary:
            abbrev = word[0] + str(len(word) - 2) + word[-1]
            if word not in self.table[abbrev]:
                self.table[abbrev].append(word)

    def isUnique(self, word: str) -> bool:
        abbrev = word[0] + str(len(word) - 2) + word[-1]
        if abbrev not in self.table or (len(self.table[abbrev]) == 1 and self.table[abbrev][0] == word):
            return True
        
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)