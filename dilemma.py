from typing import List
from random import random

import numpy as np

from player import Player

class Dilemma:
    def __init__(self, payoff_matrix: dict, player1: Player, player2: Player):
        self.payoff_matrix: np.ndarray = payoff_matrix
        self.player1: Player = player1
        self.player2: Player = player2
        self.turn = 0
        self.history1: List[bool] = list()
        self.history2: List[bool] = list()
        self.score1 = 0
        self.score2 = 0
        self.error = 0

    def apply_error(self, decision: bool) -> bool:
        if random() <= self.error:
            return not decision
        else:
            return decision

    def step(self):
        decision1: bool = self.player1.strategy(self.turn, self.history1, self.history2, self.score1, self.score2)
        decision2: bool = self.player2.strategy(self.turn, self.history1, self.history2, self.score1, self.score2)

        decision1 = self.apply_error(decision1)
        decision2 = self.apply_error(decision2)

        if decision1 is True:
            if decision2 is True:
                self.score1 += self.payoff_matrix[0,0]
                self.score2 += self.payoff_matrix[0,1]
            else:
                self.score1 += self.payoff_matrix[1,0]
                self.score2 += self.payoff_matrix[1,1]
        else:
            if decision1 is True:
                self.score1 += self.payoff_matrix[2,0]
                self.score2 += self.payoff_matrix[2,1]
            else:
                self.score1 += self.payoff_matrix[3,0]
                self.score2 += self.payoff_matrix[3,1]

        self.history1.append(decision1)
        self.history2.append(decision2)
        self.turn += 1


if __name__ == "__main__":
    pass

