from typing import List, Dict

import numpy as np
import numba as nb

from player import Player
import strategy
from dilemma import Dilemma


class Simulation:
    """
    Simulation class (main class in the program)
    """
    def __init__(self, players: Dict[str, int], turns_min: int, turns_max: int, error: float, mode: str = 'round-robin',
                 payoff_matrix: np.ndarray = np.array([[2, 2], [-1, 3], [3, -1], [0, 0]])) -> None:
        """
        Constructor of the simulation class
        :param players: Dictionary of players (strategy name, number of players of the type)
        :param turns_min: Minimum number of turns per round (i.e. 20 -> each player has min. 20 turns)
        :param turns_max: Maximum number of turns per round
        :param error: Error chance
        :param mode: Tournament mode ('round-robin', 'evolution')
        :param payoff_matrix: Dilemma payoff matrix, ndarray
            [ [coop, coop], [coop, deflect], [deflect, coop], [deflect, deflect] ]
        """
        # self.standings: List[Dict[str, int]] = players
        self.players: List[Player] = self.init_players(players)
        self.mode: str = mode
        self.turns_min: int = turns_min
        self.turns_max: int = turns_max
        self.payoff_matrix: np.ndarray = payoff_matrix
        self.error: float = error

    def init_players(self, players: Dict[str, int]) -> List[Player]:
        """
        Initialize the players
        :param players: Dictionary of players as specified in the constructor
        :return: List of Players objects
        """
        player_list: List[Player] = []
        for player_type in players.items():
            for i in range(player_type[1]):
                name: str = player_type[0]
                if i > 0:
                    name += ' #' + str(i+1)
                player_list.append(Player(strategy.get_strategy(player_type[0]), name))
        return player_list

    def round_robin(self) -> Dict[str, int]:
        """
        Simulate a round-robin tournament
        :return: Dictionary of standings - {unique player name, score}
        """
        for i in range(len(self.players)-1):
            for j in range(i+1, len(self.players)):
                dilemma: Dilemma = Dilemma(self.payoff_matrix,
                                           self.turns_min, self.turns_max, self.error, self.players[i], self.players[j])
                result: (int, int) = dilemma.run()
                self.players[i].score += result[0]
                self.players[j].score += result[1]

        self.players = sorted(self.players, key=lambda buffer_player: buffer_player.score, reverse=True)

        standings: Dict[str, int] = dict()
        for player in self.players:
            standings[player.name] = player.score

        return standings

    def evolution(self) -> Dict[str, int]:
        pass

    def simulate(self) -> Dict[str, int]:
        """
        Simulates a tournament, calls a submethod based on the mode
        :return: Dictionary of standings - {unique player name, score}
        :raises: ValueError: if invalid mode of the simulation was given
        """
        if self.mode == 'round-robin':
            return self.round_robin()
        elif self.mode == 'evolution':
            return self.evolution()
        else:
            raise ValueError("Invalid mode of the simulation")


def simplest(error: float) -> None:
    """
    Simplest possible simulation
    """
    simulation: Simulation = Simulation({"always_cooperate": 20}, 10, 25, error)
    print(simulation.simulate())

def exhaustive(error: float) -> None:
    """
    Round-robin simulation with every defined strategy participating exactly once
    """
    players: Dict[str, int] = {
        'always_cooperate': 1,
        'always_defect': 1,
        'tit_for_tat': 1,
        'grudger': 1,
        'pick_random': 1,
        'sus_tit_for_tat': 1,
        'tit_for_two_tats': 1,
        'two_tits_for_tat': 1,
        'pavlov': 1,
        'detective': 1,
        'simpleton': 1,
        'coop_75': 1,
        'retaliate_75': 1
    }
    simulation: Simulation = Simulation(players, 10, 25, error)
    print(simulation.simulate())

if __name__ == '__main__':
    # exhaustive(0)
    simulation: Simulation = Simulation({"always_cooperate": 10, "machine_learning": 10}, 10, 25, 0)
    print(simulation.simulate())
