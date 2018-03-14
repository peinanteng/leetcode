class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.summary = {}
        self.dict = set(dictionary)
        for word in self.dict:
            if len(word) <= 2:
                self.summary[word] = self.summary.get(word, 0) + 1
            else:
                newWord = word[0] + str(len(word)-2) + word[-1]
                self.summary[newWord] = self.summary.get(newWord, 0) + 1
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 2:
            newWord = word
        else:
            newWord = word[0] + str(len(word)-2) + word[-1]
        if (word in self.dict and self.summary[newWord] > 1) or \
           (word not in self.dict and newWord in self.summary):
                return False
        return True
