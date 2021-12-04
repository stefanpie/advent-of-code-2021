from os import lseek, truncate
from typing import List, Tuple
from pprint import pprint as pp
from warnings import filters
import numpy as np
import io

from numpy.core.fromnumeric import argmax
from numpy.lib.stride_tricks import broadcast_arrays


class BingoBoard:
    def __init__(self, input):
        self.board = self.parse_input(input)
        self.marked = np.zeros_like(self.board)
        self.winner = False
        self.winner_loc = np.zeros_like(self.board)

    def parse_input(self, input):
        board = input.splitlines()
        board = [row.split() for row in board]
        board = [list(map(int, row)) for row in board]
        board = np.array(board)
        return board
    
    def check_winner(self):
        rows = self.board.shape[0]
        cols = self.board.shape[1]
        row_sums = np.sum(self.marked, axis=1)
        col_sums = np.sum(self.marked, axis=0)

        if np.any(row_sums == cols):
            # print("winning row")
            self.winner = True
            winner_row_idx = np.argmax(row_sums == cols)
            self.winner_loc[winner_row_idx, :] = 1

        if np.any(col_sums == rows):
            # print("winning col")
            self.winner = True
            winner_col_idx = np.argmax(col_sums == rows)
            self.winner_loc[:, winner_col_idx] = 1





class BingoGame:
    def __init__(self, input):
        self.input = input
        self.boards, self.draws = self.parse_input(self.input)

    def parse_input(self, input):
        draws = input.splitlines()[0].strip().split(",")
        draws = [int(d) for d in draws]

        boards = input.split("\n\n")[1:]
        boards = [BingoBoard(b) for b in boards]
        return boards, draws
    
    def play_game(self):
        first_found = False
        score_first = 0

        last_found = False
        score_last = 0

        board_winners_last = list(map(lambda x: x.winner, self.boards))
        
        for i, d in enumerate(self.draws[:]):
            # print(f"{i}: {d}")

            for b in self.boards:
                b.marked[b.board == d] = 1
            
            # for b in self.boards:
            #     print(b.marked)

            for b in self.boards:
                b.check_winner()
            
            board_winners = list(map(lambda x: x.winner, self.boards))
            
            if any(board_winners) and not first_found:
                winning_board_idx = board_winners.index(True)
                winning_board = self.boards[winning_board_idx]
                sum_unmarked_numbers = np.sum((1-winning_board.marked) * winning_board.board)
                score_first = sum_unmarked_numbers * d
                first_found = True
            
            if all(board_winners) and first_found and not last_found:
                board_winners_xor = [a ^ b for a, b in zip(board_winners, board_winners_last)]
                winning_board_idx = board_winners_xor.index(True)
                winning_board = self.boards[winning_board_idx]
                sum_unmarked_numbers = np.sum((1-winning_board.marked) * winning_board.board)
                score_last = sum_unmarked_numbers * d
                last_found = True
            
            if first_found and last_found:
                break
            board_winners_last = board_winners

        return score_first, score_last



if __name__ == "__main__":
    
    with open("./input.txt") as f:
        input = f.read()
    
    game = BingoGame(input)
    score_first, score_last = game.play_game()

    part_1 = score_first
    print(f"Part 1: {part_1}")

    part_2 = score_last
    print(f"Part 2: {part_2}")
