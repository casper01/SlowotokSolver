import re
import settings
from typing import List
from slowotok import Slowotok
from dictionary import Dictionary
from dataGetter import DataDownloader


def main():
    # load dictionary
    slowotok = Slowotok()

    while True:
        # wait for key
        print('Czekanie na dane...')
        input()
        print('Szukanie slow...')

        # read new letters (from server or from file)
        letters = DataDownloader.downloadLetters()

        # create proper board
        try:
            board = list2gameSquare(letters)
        except ValueError as e:
            print('(!) Niewlasciwe dane!')
            print('(!) ', e)
            continue

        # print this board
        for i in range(4):
            for j in range(4):
                print(board[i][j], end=' ')
            print()

        # search for answers
        answers = []
        for word in slowotok.search(board):
            answers.append(word)
        
        # sort them ascending by length of the word
        answers.sort(key=lambda x: len(x))

        # print results
        for word in answers:
            print('> ', word)
        print('Wszystko!')

    
    


def list2gameSquare(letters: List[str]) -> List[List[str]]:
    """
    Create from 1D list of letters 2D array - game board
    """
    if len(letters) != 16:
        raise ValueError('Powinno byc 16 liter! Jest ' + str(len(letters)) + ': ' + str(letters))

    arr = [0] * 4
    for i in range(4):
        arr[i] = [0] * 4

    oldI = 0
    for i in range(4):
        for j in range(4):
            arr[i][j] = letters[oldI]
            oldI += 1
    return arr

if __name__ == '__main__':
    main()
