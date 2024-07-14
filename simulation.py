from typing import List, Dict

import numpy as np
import numba as nb

from player import Player
import strategy
from dilemma import Dilemma


class Simulation:
    def __init__(self, players: Dict[str, int], turns_min: int, turns_max: int, error: float, mode: str = 'round-robin',
                 payoff_matrix: np.ndarray = np.array([[2, 2], [-1, 3], [3, -1], [0, 0]])) -> None:
        # self.standings: List[Dict[str, int]] = players
        self.players: List[Player] = self.init_players(players)
        self.mode: str = mode
        self.turns_min: int = turns_min
        self.turns_max: int = turns_max
        self.payoff_matrix: np.ndarray = payoff_matrix
        self.error: float = error

    def init_players(self, players: Dict[str, int]) -> List[Player]:
        player_list: List[Player] = []
        for player_type in players.items():
            for i in range(player_type[1]):
                name: str = player_type[0]
                if i > 0:
                    name += ' #' + str(i+1)
                player_list.append(Player(strategy.get_strategy(player_type[0]), name))
        return player_list

    def round_robin(self) -> Dict[str, int]:

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
        if self.mode == 'round-robin':
            return self.round_robin()
        elif self.mode == 'evolution':
            return self.evolution()
        else:
            raise ValueError("Invalid mode of the simulation")


if __name__ == '__main__':
    simulation: Simulation = Simulation({"always_cooperate": 20}, 10, 25, 0)
    print(simulation.simulate())

