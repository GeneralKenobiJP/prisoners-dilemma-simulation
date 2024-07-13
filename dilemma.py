from typing import List
from random import random, uniform

import numpy as np

from player import Player


class Dilemma:
    def __init__(self, payoff_matrix: np.ndarray, turns_min: int, turns_max: int, error: float, player1: Player, player2: Player):
        self.payoff_matrix: np.ndarray = payoff_matrix
        self.player1: Player = player1
        self.player2: Player = player2
        self.turn: int = 0
        self.history1: List[bool] = list()
        self.history2: List[bool] = list()
        self.score1: int = 0
        self.score2: int = 0
        self.error = error
        self.rounds: int = round(uniform(turns_min, turns_max))

    def apply_error(self, decision: bool) -> bool:
        """
        Applies error to the given decision.
        """
        if random() <= self.error:
            return not decision
        else:
            return decision

    def step(self) -> None:
        """
        Simulates one prisoner's dilemma (a turn for both players)

        Applies error, payoff and logs the step
        """
        decision1: bool = self.player1.strategy(self.turn, self.history1, self.history2, self.score1, self.score2)
        decision2: bool = self.player2.strategy(self.turn, self.history1, self.history2, self.score1, self.score2)

        decision1 = self.apply_error(decision1)
        decision2 = self.apply_error(decision2)

        if decision1 is True:
            if decision2 is True:
                self.score1 += self.payoff_matrix[0, 0]
                self.score2 += self.payoff_matrix[0, 1]
            else:
                self.score1 += self.payoff_matrix[1, 0]
                self.score2 += self.payoff_matrix[1, 1]
        else:
            if decision1 is True:
                self.score1 += self.payoff_matrix[2, 0]
                self.score2 += self.payoff_matrix[2, 1]
            else:
                self.score1 += self.payoff_matrix[3, 0]
                self.score2 += self.payoff_matrix[3, 1]

        self.history1.append(decision1)
        self.history2.append(decision2)

    def run(self) -> (int, int):
        """
        Runs the game for a random number of rounds that belongs to the [turns_min, turns_max] interval
        :return: score of player 1 and score of player 2
        """
        while self.turn < self.rounds:
            self.step()
            self.turn += 1

        return self.score1, self.score2




if __name__ == "__main__":
    pass

