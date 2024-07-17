from random import random
from typing import List, Tuple, Dict

import numpy as np

import dilemma
from dilemma import compute_score


def get_strategy(name: str):
    """
    Returns the strategy function pointer from the strategy name
    :param name: Strategy name
    :return: Function pointer to a specific strategy
    :raises ValueError: if invalid strategy name was given.
    """
    if name == 'always_cooperate':
        return always_cooperate
    if name == 'always_defect':
        return always_defect
    if name == 'tit_for_tat':
        return tit_for_tat
    if name == 'grudger':
        return grudger
    if name == 'pick_random':
        return pick_random
    if name == 'sus_tit_for_tat':
        return sus_tit_for_tat
    if name == 'tit_for_two_tats':
        return tit_for_two_tats
    if name == 'two_tits_for_tat':
        return two_tits_for_tat
    if name == 'pavlov':
        return pavlov
    if name == 'detective':
        return detective
    if name == 'simpleton':
        return simpleton
    if name == 'coop_75':
        return coop_75
    if name == 'retaliate_75':
        return retaliate_75
    if name == 'machine_learning':
        return machine_learning_strategy_model().machine_learning

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
    Always cooperates, unless cheated twice in a row - then defects and goes back to cooperating.
    If first move - cooperate.
    """
    if len(opponent_history) < 2:
        return True
    if opponent_history[-1] is False and opponent_history[-2] is False:
        return False
    return True

def two_tits_for_tat(turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray, own_history: List[bool],
                     opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    Always cooperates, unless cheated - then defects twice and goes back to cooperating. If first move - cooperate
    """
    if len(opponent_history) == 0:
        return True
    if opponent_history[-1] is False or len(opponent_history) == 1 or opponent_history[-2] is False:
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

    try:
        if opponent_history.index(False) <= 3:
            return False
    except ValueError:
        pass
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

class machine_learning_strategy_model:
    def __init__(self, learning_rate: float = 0.1, discount_factor: float = 0.9):
        self.q_values: Dict[Tuple[Tuple[List[bool], List[bool]], bool], float] = {}
        self.learning_rate: float = learning_rate
        self.discount_factor: float = discount_factor

    def get_state(self, own_moves: List[bool], opponent_moves: List[bool]) -> Tuple[List[bool], List[bool]]:
        return own_moves, opponent_moves

    def get_new_state(self, old_state: Tuple[List[bool], List[bool]], action: bool, opponent_action: bool) -> Tuple[List[bool], List[bool]]:
        new_state = old_state
        new_state[0].append(action)
        new_state[1].append(opponent_action)
        return new_state

    def get_previous_state(self, own_moves: List[bool], opponent_moves: List[bool]) -> Tuple[List[bool], List[bool]]:
        return own_moves[:-1], opponent_moves[:-1]

    def update_q_values(self, new_state: Tuple[List[bool], List[bool]], payoff_matrix: np.ndarray) -> None:
        state: Tuple[List[bool], List[bool]] = (new_state[0][:-1], new_state[1][:-1])
        action: bool = new_state[0][-1]
        opponent_action: bool = new_state[1][-1]
        reward: int = dilemma.compute_score(payoff_matrix, action, opponent_action)

        if (state, action) not in self.q_values.keys():
            self.q_values[state, action] = 1.0 if action is True else 0.0
        if (new_state, True) not in self.q_values.keys():
            self.q_values[new_state, True] = self.q_values[state, action] + 1.0
        if (new_state, False) not in self.q_values.keys():
            self.q_values[new_state, False] = self.q_values[state, action]

        best_future_state = max(self.q_values[new_state, True], self.q_values[new_state, False])
        self.q_values[state, action] = ((1-self.learning_rate) * self.q_values[state, action] +
                                        self.learning_rate * (reward + self.discount_factor * best_future_state))

    def machine_learning(self, turn: int, turns_min: int, turns_max: int, payoff_matrix: np.ndarray,
                         own_history: List[bool], opponent_history: List[bool], own_score: int, opponent_score: int):
        if turn > 0:
            self.update_q_values(self.get_state(own_history, opponent_history), payoff_matrix)
        state: Tuple[List[bool], List[bool]] = self.get_state(own_history, opponent_history)
        action: bool = self.q_values[state, True] >= self.q_values[state, False]
        
        return action
