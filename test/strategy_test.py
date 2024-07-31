import unittest

import numpy as np

import strategy

class strategy_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payoff_matrix: np.ndarray = np.array([[2, 2], [-1, 3], [3, -1], [0, 0]])

    def test_always_cooperate(self):
        self.assertEqual(True,
                         strategy.always_cooperate(1, 10, 15, self.payoff_matrix, [], [], 0, 0))
        self.assertEqual(True,
                         strategy.always_cooperate(2, 10, 15, self.payoff_matrix, [True], [False], -1, 3))
    def test_always_defect(self):
        self.assertEqual(False,
                         strategy.always_defect(1, 10, 15, self.payoff_matrix, [], [], 0, 0))
        self.assertEqual(False,
                         strategy.always_defect(2, 10, 15, self.payoff_matrix, [False], [True], 3, -1))
    def test_tit_for_tat(self):
        self.assertEqual(True,
                         strategy.tit_for_tat(1, 10, 15, self.payoff_matrix, [], [], 0, 0))
        self.assertEqual(True,
                         strategy.tit_for_tat(2, 10, 15, self.payoff_matrix, [True], [True], 2, 2))
        self.assertEqual(False,
                         strategy.tit_for_tat(2, 10, 15, self.payoff_matrix, [True], [False], -1, 3))
        self.assertEqual(True,
                         strategy.tit_for_tat(3, 10, 15, self.payoff_matrix, [True, False], [False, True], 2, 2))
    def test_grudger(self):
        self.assertEqual(True,
                         strategy.grudger(1, 10, 15, self.payoff_matrix, [], [], 0, 0))
        self.assertEqual(True,
                         strategy.grudger(2, 10, 15, self.payoff_matrix, [True], [True], 2, 2))
        self.assertEqual(False,
                         strategy.grudger(2, 10, 15, self.payoff_matrix, [True], [False], -1, 3))
        self.assertEqual(False,
                         strategy.grudger(3, 10, 15, self.payoff_matrix, [True, False], [False, True], 2, 2))
    def test_sus_tit_for_tat(self):
        self.assertEqual(False,
                         strategy.sus_tit_for_tat(1, 10, 15, self.payoff_matrix, [], [], 0, 0))
        self.assertEqual(False,
                         strategy.sus_tit_for_tat(2, 10, 15, self.payoff_matrix, [False], [False], 0, 0))
        self.assertEqual(True,
                         strategy.sus_tit_for_tat(2, 10, 15, self.payoff_matrix, [False], [True], 3, -1))
        self.assertEqual(False,
                         strategy.sus_tit_for_tat(3, 10, 15, self.payoff_matrix, [False, True], [True, False], 2, 2))
    def test_tit_for_two_tats(self):
        self.assertEqual(True,
                         strategy.tit_for_two_tats(1, 10, 15, self.payoff_matrix, [], [], 0, 0))
        self.assertEqual(True,
                         strategy.tit_for_two_tats(2, 10, 15, self.payoff_matrix, [True], [False], -1, 3))
        self.assertEqual(True,
                         strategy.tit_for_two_tats(2, 10, 15, self.payoff_matrix, [True], [True], 2, 2))
        self.assertEqual(False,
                         strategy.tit_for_two_tats(3, 10, 15, self.payoff_matrix, [True, True], [False, False], -2, 6))
        self.assertEqual(True,
                         strategy.tit_for_two_tats(4, 10, 15, self.payoff_matrix, [True, True, False], [False, False, True], 1, 5))
    def test_two_tits_for_tat(self):
        self.assertEqual(True,
                         strategy.two_tits_for_tat(1, 10, 15, self.payoff_matrix, [], [], 0, 0))
        self.assertEqual(False,
                         strategy.two_tits_for_tat(2, 10, 15, self.payoff_matrix, [True], [False], -1, 3))
        self.assertEqual(True,
                         strategy.two_tits_for_tat(2, 10, 15, self.payoff_matrix, [True], [True], 2, 2))
        self.assertEqual(False,
                         strategy.two_tits_for_tat(3, 10, 15, self.payoff_matrix, [True, False], [False, True], 2, 2))
        self.assertEqual(True,
                         strategy.two_tits_for_tat(4, 10, 15, self.payoff_matrix, [True, False, False], [False, True, True], 1, 5))
    def test_pavlov(self):
        self.assertEqual(True,
                         strategy.pavlov(1, 10, 15, self.payoff_matrix, [], [], 0, 0))
        self.assertEqual(False,
                         strategy.pavlov(2, 10, 15, self.payoff_matrix, [True], [False], -1, 3))
        self.assertEqual(True,
                         strategy.pavlov(2, 10, 15, self.payoff_matrix, [True], [True], 2, 2))
        self.assertEqual(True,
                         strategy.pavlov(2, 10, 15, self.payoff_matrix, [False], [False], 0, 0))
        self.assertEqual(False,
                         strategy.pavlov(2, 10, 15, self.payoff_matrix, [False], [True], 0, 0))
        self.assertEqual(False,
                         strategy.pavlov(3, 10, 15, self.payoff_matrix, [True, False], [False, True], 2, 2))
        self.assertEqual(True,
                         strategy.pavlov(4, 10, 15, self.payoff_matrix, [True, False], [False, False], 1, 5))
    def test_detective(self):
        self.assertEqual(True,
                         strategy.detective(1, 10, 15, self.payoff_matrix, [], [], 0, 0))
        self.assertEqual(False,
                         strategy.detective(2, 10, 15, self.payoff_matrix, [True], [False], -1, 3))
        self.assertEqual(False,
                         strategy.detective(2, 10, 15, self.payoff_matrix, [True], [True], 2, 2))
        self.assertEqual(False,
                         strategy.detective(2, 10, 15, self.payoff_matrix, [False], [False], 0, 0))
        self.assertEqual(False,
                         strategy.detective(2, 10, 15, self.payoff_matrix, [False], [True], 0, 0))
        self.assertEqual(True,
                         strategy.detective(3, 10, 15, self.payoff_matrix, [True, False], [False, True], 2, 2))
        self.assertEqual(True,
                         strategy.detective(4, 10, 15, self.payoff_matrix, [True, False], [False, False], 1, 5))
        self.assertEqual(True,
                         strategy.detective(4, 10, 15, self.payoff_matrix, [True, False, True],
                                                   [False, True, True], 1, 5))
        self.assertEqual(True,
                         strategy.detective(5, 10, 15, self.payoff_matrix, [True, False, True, True],
                                            [True, True, True, True], 1, 5))
        self.assertEqual(True,
                         strategy.detective(6, 10, 15, self.payoff_matrix, [True, False, True, True, True],
                                            [True, True, True, True, False], 1, 5))
        self.assertEqual(False,
                         strategy.detective(5, 10, 15, self.payoff_matrix, [True, False, True, True],
                                            [True, True, False, True], 1, 5))
        self.assertEqual(False,
                         strategy.detective(6, 10, 15, self.payoff_matrix, [True, False, True, True, True],
                                            [True, True, False, True, True], 1, 5))
    def test_simpleton(self):
        self.assertEqual(True,
                         strategy.simpleton(1, 10, 15, self.payoff_matrix, [], [], 0, 0))
        self.assertEqual(False,
                         strategy.simpleton(2, 10, 15, self.payoff_matrix, [True], [False], -1, 3))
        self.assertEqual(True,
                         strategy.simpleton(2, 10, 15, self.payoff_matrix, [True], [True], 2, 2))
        self.assertEqual(True,
                         strategy.simpleton(2, 10, 15, self.payoff_matrix, [False], [False], 0, 0))
        self.assertEqual(False,
                         strategy.simpleton(2, 10, 15, self.payoff_matrix, [False], [True], 0, 0))
        self.assertEqual(False,
                         strategy.simpleton(3, 10, 15, self.payoff_matrix, [True, False], [False, True], 2, 2))
        self.assertEqual(True,
                         strategy.simpleton(4, 10, 15, self.payoff_matrix, [True, False], [False, False], 1, 5))

    if __name__ == '__main__':
        unittest.main()