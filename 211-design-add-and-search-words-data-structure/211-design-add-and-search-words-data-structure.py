class WordDictionary(object):
    def __init__(self):
        self.dic = collections.defaultdict(list)
    def addWord(self, word):
        self.dic[len(word)].append(word)
    def search(self, word):
        for stored_word in self.dic[len(word)]:
            if all(word[i] == stored_word[i] for i in range(len(word)) if word[i] != "."): return True
        return False