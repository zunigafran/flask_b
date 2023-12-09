"""Utilities related to Boggle game."""

from random import choice
import string


class Boggle():

    def __init__(self):

        self.words = self.read_dict("words.txt")

    def read_dict(self, dict_path):
        dict_file = open(dict_path)
        words = [w.strip() for w in dict_file]
        dict_file.close()
        return words

    def make_board(self):
        board = []

        for y in range(5):
            row = [choice(string.ascii_uppercase) for i in range(5)]
            board.append(row)

        return board

    def check_valid_word(self, board, word):
        word_exists = word in self.words
        valid_word = self.find(board, word.upper())

        if word_exists and valid_word:
            result = "awesome"
        elif word_exists and not valid_word:
            result = "nope, not on this board"
        else:
            result = "not a word"

        return result

    def find_from(self, board, word, y, x, seen):

        if x > 4 or y > 4:
            return

        if board[y][x] != word[0]:
            return False

        if (y, x) in seen:
            return False

        if len(word) == 1:
            return True
        seen = seen | {(y, x)}

        if y > 0:
            if self.find_from(board, word[1:], y - 1, x, seen):
                return True

        if y < 4:
            if self.find_from(board, word[1:], y + 1, x, seen):
                return True

        if x > 0:
            if self.find_from(board, word[1:], y, x - 1, seen):
                return True

        if x < 4:
            if self.find_from(board, word[1:], y, x + 1, seen):
                return True

        # diagonals
        if y > 0 and x > 0:
            if self.find_from(board, word[1:], y - 1, x - 1, seen):
                return True

        if y < 4 and x < 4:
            if self.find_from(board, word[1:], y + 1, x + 1, seen):
                return True

        if x > 0 and y < 4:
            if self.find_from(board, word[1:], y + 1, x - 1, seen):
                return True

        if x < 4 and y > 0:
            if self.find_from(board, word[1:], y - 1, x + 1, seen):
                return True
        # Couldn't find the next letter, so this path is dead

        return False

    def find(self, board, word):
        """Can word be found in board?"""


        for y in range(0, 5):
            for x in range(0, 5):
                if self.find_from(board, word, y, x, seen=set()):
                    return True

        return False
