import sys
import unittest
from io import StringIO
from unittest import mock

from tic_tac_toe import TicTacToeGame


@mock.patch('sys.stdout', new=StringIO())
class TestTicTacToe(unittest.TestCase):
    def test_input(self):
        with mock.patch('builtins.input', side_effect=['aaa bbb', '2', '-1 -1', '5 5', '1 2']):
            game = TicTacToeGame()
            player = 1
            game.make_move(player)
            output = sys.stdout.getvalue().strip().splitlines()
            self.assertEqual(output[1], 'Please provide integer input in form: row column')
            self.assertEqual(output[2], 'Input contains only one index. '\
                                        'Please provide 2 indices')
            self.assertEqual(output[3], 'Input is out of game border boundaries (<= 0). '\
                                        'Please make sure 1 <= row, col <= 3')
            self.assertEqual(output[4], 'Input is out of game border boundaries. '\
                                        'Please make sure 1 <= row, col <= 3')
            self.assertEqual(output[5], 'Player 1 - x, Player 2 - o')

        with mock.patch('builtins.input', side_effect=['1 2', '2 1']):
            player = 2
            game.make_move(player)
            output = sys.stdout.getvalue().strip().splitlines()
            self.assertEqual(output[12], 'This cell is taken. Please provide another coordinates')
            self.assertEqual(output[13], 'Player 1 - x, Player 2 - o')

    def test_move(self):
        game = TicTacToeGame()

        with mock.patch('builtins.input', return_value='1 2'):
            player = 1
            game.make_move(player)
            output = sys.stdout.getvalue().strip().splitlines()
            self.assertEqual(output[-3], '. x .')
            self.assertEqual(output[-2], '. . .')
            self.assertEqual(output[-1], '. . .')

        with mock.patch('builtins.input', return_value='2 1'):
            player = 2
            game.make_move(player)
            output = sys.stdout.getvalue().strip().splitlines()
            self.assertEqual(output[-3], '. x .')
            self.assertEqual(output[-2], 'o . .')
            self.assertEqual(output[-1], '. . .')

    def test_win_row(self):
        row_wins_scenarios = [(['1 1', '2 2', '1 2', '3 3', '1 3'], 1),
                              (['1 1', '2 2', '1 2', '2 1', '3 3', '2 3'], 2),
                              (['1 1', '3 2', '1 2', '3 1', '2 2', '3 3'], 2)]
        for scene, winner in row_wins_scenarios:
            with mock.patch('builtins.input', side_effect=scene):
                game = TicTacToeGame()
                game.start_game()
                output = sys.stdout.getvalue().strip().splitlines()
                self.assertEqual(output[-1], f'Winner is Player {winner}')

    def test_win_cols(self):
        col_wins_scenarios = [(['1 1', '2 2', '3 1', '1 2', '2 1'], 1),
                              (['1 2', '3 1', '2 2', '2 1', '3 2'], 1),
                              (['1 1', '3 3', '1 2', '2 3', '2 2', '1 3'], 2)]
        for scene, winner in col_wins_scenarios:
            with mock.patch('builtins.input', side_effect=scene):
                game = TicTacToeGame()
                game.start_game()
                output = sys.stdout.getvalue().strip().splitlines()
                self.assertEqual(output[-1], f'Winner is Player {winner}')

    def test_win_diag(self):
        diag_wins_scenarios = [(['1 1', '2 1', '2 2', '1 2', '3 3'], 1),
                               (['1 2', '3 1', '2 3', '2 2', '3 2', '1 3'], 2),
                               (['1 3', '3 3', '1 2', '2 2', '2 1', '1 1'], 2)]
        for scene, winner in diag_wins_scenarios:
            with mock.patch('builtins.input', side_effect=scene):
                game = TicTacToeGame()
                game.start_game()
                output = sys.stdout.getvalue().strip().splitlines()
                self.assertEqual(output[-1], f'Winner is Player {winner}')

    def test_tie(self):
        diag_tie_scenarios = [['1 1', '1 2', '1 3', '3 3', '2 2', '2 3', '2 1', '3 1', '3 2'],
                              ['3 3', '1 1', '1 3', '3 1', '2 1', '1 2', '3 2', '2 3', '2 2']]
        for scene in diag_tie_scenarios:
            with mock.patch('builtins.input', side_effect=scene):
                game = TicTacToeGame()
                game.start_game()
                output = sys.stdout.getvalue().strip().splitlines()
                self.assertEqual(output[-1], 'It\'s a tie!')


if __name__ == "__main__":
    unittest.main()
