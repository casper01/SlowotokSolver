import collections


class TrieNode:
    def __init__(self):
        # represents children of node: letters A-Z (+ pl letters)
        self.children = collections.defaultdict(TrieNode)
        # indicates if current node is the last letter of the word
        self.isEnd = False
        # True if current node is parto of path of at least one word
        self.visited = False
        # for leafs only: contains full word
        self.word = ''


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.visited = True

    def insert(self, word):
        """
        Insert word into Trie tree
        """
        node = self.root
        for c in word:
            node = node.children[c]
            node.visited = True
        node.isEnd = True
        node.word = word

