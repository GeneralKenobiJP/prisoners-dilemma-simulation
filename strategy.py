from random import random
from typing import List

import numpy as np


def get_strategy(name: str):
    """
    Returns the strategy function pointer from the strategy name
    :param name: Strategy name
    :return: Function pointer to a specific strategy
    :raises ValueError: if invalid strategy name was given.
    """
    if name == 'always_cooperate':
        return always_cooperate
    else:
        raise ValueError('Invalid strategy name.')


'''
Strategies available for players of the prisoner's dilemma.

Parameter scheme:
    :param turn: Current turn number
    :param turns_min: Minimum number of turns in the game
    :param turns_max: Maximum number of turns in the game
    :param payoff_matrix: Payoff matrix of the simulation
    :param own_history: History of own moves 
    :param opponent_history: History of opponent moves
    :param own_score: Own current score 
    :param opponent_score: Current score of the opponent
    :return: True - cooperate / False - defect
'''


def always_cooperate(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    Always cooperates
    """
    return True

def always_defect(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    Always defects
    """
    return False

def tit_for_tat(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    If first move - cooperate. Otherwise - always copy the opponent's move
    """
    if len(opponent_history) == 0:
        return True

    return opponent_history[-1]

def grudger(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    Always cooperates unless the opponent defects - then always defects
    """
    if opponent_history.__contains__(False):
        return False
    return True

def pick_random(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    Picks his stance at random
    """
    return random() < 0.5

def sus_tit_for_tat(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    If first move - defect. Otherwise - always copy the opponent's move
    """
    if len(opponent_history) == 0:
        return False
    return opponent_history[-1]

def tit_for_two_tats(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    Always cooperates, unless cheated twice in a row - then defects and goes back to cooperating
    """
    if opponent_history[-1] is False and opponent_history[-2] is False:
        return False
    return True

def two_tits_for_tat(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    Always cooperates, unless cheated - then defects twice and goes back to cooperating
    """
    if opponent_history[-1] is False or opponent_history[-2] is False:
        return False
    return True

def pavlov(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    Cooperates if the opponent moved the same as the player, otherwise defects. If first move - cooperates
    """
    if len(opponent_history) == 0:
        return True
    if opponent_history[-1] == own_history[-1]:
        return True
    return False

def detective(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    Starts with Cooperate, Cheat, Cooperate, Cooperate. Afterwards:
    if opponent defected at least once - always defect,
    otherwise - always cooperate
    """
    if len(opponent_history) == 0:
        return True
    if len(opponent_history) == 1:
        return False
    if len(opponent_history) == 2:
        return True
    if len(opponent_history) == 3:
        return True

    if opponent_history.index(False) <= 3:
        return False
    return True

def simpleton(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    If the last move earned points, repeat the last move. Otherwise, do opposite of the last move.
    If first move - cooperate
    """
    if len(opponent_history) == 0:
        return True
    if opponent_history[-1] is True:
        if own_history[-1] is True:
            return payoff_matrix[0, 0] > 0
        return payoff_matrix[1, 0] > 0

    if own_history[-1] is True:
        return payoff_matrix[2, 0] > 0
    return payoff_matrix[3, 0] > 0

def coop_75(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    Cooperate with probability of 0.75
    """
    return random() < 0.75

def retaliate_75(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    If cheated - defect with probability of 0.75. Otherwise - cooperate
    """
    if len(opponent_history) == 0 or opponent_history[-1] is True:
        return True
    return random() >= 0.75
