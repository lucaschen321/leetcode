class WordDictionary:
    def __init__(self, children=None):
        """
        Initialize your data structure here.
        """
        self.end_of_word = False
        self.children = {}

    def addWordIterative(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        trie = self
        for char in word:
            if char not in trie.children:
                trie.children[char] = WordDictionary()
            trie = trie.children[char]

        trie.end_of_word = True

    def addWordRecursive(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if word:
            if word[0] not in self.children:
                self.children[word[0]] = WordDictionary()
            self.children[word[0]].addWord(word[1:])
        else:
            self.end_of_word = True

    def searchIterative(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        stack = [(self, word)]
        while stack:
            trie, word = stack.pop()
            if not word:
                if trie.end_of_word:
                    return True
            else:
                if word[0] == ".":
                    for child in trie.children.values():
                        stack.append((child, word[1:]))
                else:
                    if word[0] in trie.children:
                        stack.append((trie.children[word[0]], word[1:]))

        return False

    def searchRecursive(self, word: str) -> bool:
        if not word:
            return self.end_of_word

        if word[0] == ".":
            return any(child.search(word[1:]) for child in self.children.values())  # <any> does short circuiting
        else:
            if word[0] not in self.children:
                return False

            return self.children[word[0]].search(word[1:])
