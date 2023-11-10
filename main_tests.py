import unittest

from main import Game, X_CELL, O_CELL


class TestGame(unittest.TestCase):
    def test_x_wins(self):
        game = Game()

        x_winning_combination = [1, 2, 3]
        for a in x_winning_combination:
            game.set_step(a, True)

        winner = game.check_winning_conditions()
        self.assertEqual(winner, f'Переможець {X_CELL}')
        self.assertEqual(game.who_win, None)

    def test_o_wins(self):
        game = Game()

        o_winning_combination = [1, 5, 9]
        for a in o_winning_combination:
            game.set_step(a, False)

        winner = game.check_winning_conditions()
        self.assertEqual(winner, f'Переможець {O_CELL}')
        self.assertEqual(game.who_win, None)

    def test_draw(self):
        game = Game()

        draw_combination = [1, 2, 3, 4, 6, 5, 7, 8, 9]
        for a in draw_combination:
            game.set_step(a, game.step_number % 2 == 0)

        self.assertEqual(game.check_winning_conditions(), 'Переможець O')
        self.assertIsNone(game.winner)


if __name__ == '__main__':
    unittest.main()
