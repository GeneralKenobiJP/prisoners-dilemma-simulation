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

    if __name__ == '__main__':
        unittest.main()