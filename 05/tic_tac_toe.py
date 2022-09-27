import os
from collections import defaultdict

from exceptions import NegativeIndexError, TakenCellError, OneIndexError


class TicTacToeGame:
    def __init__(self):
        self.__board = [['.'] * 3 for _ in range(3)]
        self.__moves = defaultdict(list)
        self.__possible_moves = {1: 'x', 2: 'o'}
        self.__winner = None
        self.__isdone = False
        self.__max_num_of_moves = 9

    def show_board(self):
        os.system('clear')
        print('Player 1 - x, Player 2 - o')
        print('Move in form: row column')
        print('Current Board')
        print('\n'.join([' '.join([self.__board[i][j] for j in range(3)]) for i in range(3)]))

    def validate_input(self, move):
        parsed_move = None
        try:
            move = tuple(map(int, move.split()))
            if len(move) == 1:
                raise OneIndexError
            elif move[0] <= 0 or move[1] <= 0:
                raise NegativeIndexError
            elif self.__board[move[0] - 1][move[1] - 1] != '.':
                raise TakenCellError
            parsed_move = move
        except ValueError:
            print('Please provide integer input in form: row column')
        except OneIndexError:
            print('Input contains only one index. '\
                  'Please provide 2 indices')
        except NegativeIndexError:
            print('Input is out of game border boundaries (<= 0). '\
                  'Please make sure 1 <= row, col <= 3')
        except IndexError:
            print('Input is out of game border boundaries. '\
                  'Please make sure 1 <= row, col <= 3')
        except TakenCellError:
            print('This cell is taken. Please provide another coordinates')
        finally:
            return parsed_move

    def start_game(self):
        num_of_moves = 0
        self.show_board()

        player = 2
        while not self.__isdone and num_of_moves < self.__max_num_of_moves:
            player = 3 - player
            self.make_move(player)
            num_of_moves += 1
            self.__isdone, self.__winner = self.check_winner(player)

        if self.__winner is None:
            print('It\'s a tie!')
        else:
            print(f'Winner is Player {self.__winner}')

    def make_move(self, player):
        print(f'Player {player}, please, make your move')
        move = None
        while move is None:
            move = input()
            move = self.validate_input(move)
        self.__moves[player].append(move)
        self.__board[move[0] - 1][move[1] - 1] = self.__possible_moves[player]
        self.show_board()

    def check_winner(self, player):
        if len(self.__moves[player]) < 3:
            return False, None
        rows = [el[0] for el in self.__moves[player]]
        for elem in rows:
            if rows.count(elem) == 3:
                return True, player

        cols = [el[1] for el in self.__moves[player]]
        for elem in cols:
            if cols.count(elem) == 3:
                return True, player

        if set([(1, 1), (2, 2), (3, 3)]) <= set(self.__moves[player]) \
                or set([(1, 3), (2, 2), (3, 1)]) <= set(self.__moves[player]):
            return True, player

        return False, None


if __name__ == "__main__":
    game = TicTacToeGame()
    game.start_game()
