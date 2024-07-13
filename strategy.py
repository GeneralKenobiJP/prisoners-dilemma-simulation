from typing import List

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
    :param turn:
    :param turns_min:
    :param turns_max:
    :param history1:
    :param history2:
    :param score1:
    :param score2:
    :return:
    """
    return True
