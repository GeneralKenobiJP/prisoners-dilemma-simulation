import math
from typing import List
from random import random, uniform

import numpy as np

from player import Player


class Dilemma:
    """
    Dilemma class. Simulates entire round between two players, and each turn, as well
    """
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
        self.turns_min: int = turns_min
        self.turns_max: int = turns_max

    def apply_error(self, decision: bool) -> bool:
        """
        Applies error to the given decision.
        """
        if random() <= self.error:
            return not decision
        else:
            return decision

    def step(self, debug: bool = False) -> None:
        """
        Simulates one prisoner's dilemma (a turn for both players)

        Applies error, payoff and logs the step

        :param debug: If true - print decisions
        """
        decision1: bool = bool(self.player1.strategy(self.turn, self.turns_min, self.turns_max, self.payoff_matrix,
                                                self.history1, self.history2, self.score1, self.score2))
        decision2: bool = bool(self.player2.strategy(self.turn, self.turns_min, self.turns_max, self.payoff_matrix,
                                                self.history2, self.history1, self.score2, self.score1))

        debug_string1: str = str(decision1)
        debug_string2: str = str(decision2)

        decision1 = self.apply_error(decision1)
        decision2 = self.apply_error(decision2)

        debug_string1 += "(" + str(decision1) + ")"
        debug_string2 += "(" + str(decision2) + ")"

        if debug:
            print(debug_string1 + "vs. " + debug_string2)

        if decision1 is True:
            if decision2 is True:
                self.score1 += self.payoff_matrix[0, 0]
                self.score2 += self.payoff_matrix[0, 1]
            else:
                self.score1 += self.payoff_matrix[1, 0]
                self.score2 += self.payoff_matrix[1, 1]
        else:
            if decision2 is True:
                self.score1 += self.payoff_matrix[2, 0]
                self.score2 += self.payoff_matrix[2, 1]
            else:
                self.score1 += self.payoff_matrix[3, 0]
                self.score2 += self.payoff_matrix[3, 1]

        self.history1.append(bool(decision1))
        self.history2.append(bool(decision2))

    def run(self, debug: bool = False) -> (int, int):
        """
        Runs the game for a random number of rounds that belongs to the [turns_min, turns_max] interval
        :param debug: If true - print decisions while calling another steps
        :return: score of player 1 and score of player 2
        """
        while self.turn < self.rounds:
            self.step(debug)
            self.turn += 1

        return math.floor(10*self.score1/self.rounds), math.floor(10*self.score2/self.rounds)


def compute_score(payoff_matrix: np.ndarray, own_action: bool, opponent_action: bool) -> (int, int):
    """
    Computes the score based on the payoff matrix and action of both players.
    :param payoff_matrix: Payoff matrix of the prisoner's dilemma
    :param own_action: Own action
    :param opponent_action: Opponent's action
    :return: Own score, opponent score
    """
    if own_action is True:
        if opponent_action is True:
            return payoff_matrix[0, 0], payoff_matrix[0, 1]
        else:
            return payoff_matrix[1, 0], payoff_matrix[1, 1]
    else:
        if opponent_action is True:
            return payoff_matrix[2, 0], payoff_matrix[2, 1]
        else:
            return payoff_matrix[3, 0], payoff_matrix[3, 1]