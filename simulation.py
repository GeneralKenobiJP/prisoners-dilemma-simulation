from typing import List, Dict

import numpy as np
import numba as nb

from player import Player
import strategy


class Simulation:
    def __init__(self, players: Dict[str, int], turns_min: int, turns_max: int, mode: str = 'round-robin',
                 payoff_matrix: np.ndarray = np.array([[2, 2], [-1, 3], [3, -1], [0, 0]])) -> None:
        # self.standings: List[Dict[str, int]] = players
        self.players: List[Player] = self.init_players(players)
        self.mode: str = mode
        self.turns_min: int = turns_min
        self.turns_max: int = turns_max
        self.payoff_matrix: np.ndarray = payoff_matrix

    def init_players(self, players: Dict[str, int]) -> List[Player]:
        player_list: List[Player] = []
        for player_type in players.items():
            for i in range(player_type[1]):
                player_list.append(strategy.get_strategy(player_type[0]))
        return player_list

    def round_robin(self) -> Dict[str, int]:
        pass

    def evolution(self) -> Dict[str, int]:
        pass

    def simulate(self) -> Dict[str, int]:
        if self.mode == 'round-robin':
            return self.round_robin()
        elif self.mode == 'evolution':
            return self.evolution()
        else:
            raise ValueError("Invalid mode of the simulation")


if __name__ == '__main__':
    pass

