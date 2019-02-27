from tqdm import tqdm
import settings
import collections
from trie import Trie


class Dictionary:
    def __init__(self):
        self.tree = Trie()
        self._load()

    def _load(self):
        """
        Create Trie tree from all the words
        inside dictionary that have at least specified length 
        Operation takes noticeable amount of time,
        displays loading bar
        """
        with open(settings.DICTIONARY_PATH, 'r') as f:
            words = f.readlines()

            for i in tqdm(range(len(words))):
                word = words[i].strip().upper()
                if len(word) < settings.MIN_WORD_LEN:
                    continue
                self.tree.insert(word)
