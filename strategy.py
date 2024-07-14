from typing import List


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
    :param own_history: History of own moves 
    :param opponent_history: History of opponent moves
    :param own_score: Own current score 
    :param opponent_score: Current score of the opponent
    :return: True - cooperate / False - defect
'''


def always_cooperate(turn: int, turns_min: int, turns_max: int, own_history: List[bool], opponent_history: List[bool], own_score: int, opponent_score: int):
    """
    Always cooperates
    """
    return True
