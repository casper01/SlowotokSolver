from typing import List, Tuple
from dictionary import Dictionary
import settings
from trie import TrieNode


class Slowotok:
    def __init__(self):
        self.board = None
        print('Ladowanie slownika...')
        self.dictionary = Dictionary()
        print('Sukces!')
        self.usedWords = set()

    def search(self, board: List[List[int]]):
        """
        Find all correct words according to dictionary
        Limit searched sequences of characters to 
        those branches that exist in Trie tree
        """
        self.usedWords = set()
        self.board = board
        used = [0] * 4
        for i in range(4):
            used[i] = [False] * 4

        for y in range(4):
            for x in range(4):
                for word in self._search((y, x), used, self.dictionary.tree.root.children[self.board[y][x]]):
                    if word not in self.usedWords:
                        self.usedWords.add(word)
                        yield word

    def _search(self, pos: Tuple, used: List[List[bool]], actTrieNode: TrieNode):
        y, x = pos
        used[y][x] = True

        # check if actual word exists in dictionary
        if actTrieNode.isEnd:
            yield actTrieNode.word

        directions = self._getAccessiblePositons(pos, used, actTrieNode)
        for yy, xx in directions:
            yield from self._search((yy, xx), used, actTrieNode.children[self.board[yy][xx]])

        used[y][x] = False

    def _getAccessiblePositons(self, pos: Tuple, used: List[List[str]], treeNode: TrieNode) -> List[Tuple]:
        """
        Return list of all positions that are accessible
        from pos, according to game rules
        Letters already used aren't accessible
        If branch with the letter does not exist in Trie, such
        letter is also not accessible
        """
        y, x = pos
        ans = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if y + i < 0 or x + j < 0 or y + i >= len(self.board) or x + j >= len(self.board[y + i]):
                    continue
                if used[y + i][x + j]:
                    continue
                char = self.board[y + i][x + j]
                if not treeNode.children[char].visited:
                    continue
                ans.append((y + i, x + j))
        return ans
