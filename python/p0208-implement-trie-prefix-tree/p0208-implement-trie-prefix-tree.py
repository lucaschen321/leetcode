from collections import defaultdict


class TrieIterative:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.end_of_word = False
        self.children = defaultdict(TrieIterative)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self
        for char in word:
            trie = trie.children[(char)]

        trie.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self
        for char in word:
            if char not in trie.children:
                return False
            trie = trie.children[char]

        return trie.end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self
        for char in prefix:
            if char not in trie.children:
                return False
            trie = trie.children[char]

        return True


class TrieRecursive:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.end_of_word = False
        self.children = defaultdict(TrieRecursive)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word:
            self.children[word[0]].insert(word[1:])
        else:
            self.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return self.end_of_word

        if not self.children.get(word[0]):
            return False

        return self.children[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return True

        if not self.children.get(prefix[0]):
            return False

        return self.children[prefix[0]].startsWith(prefix[1:])

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

