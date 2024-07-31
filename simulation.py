from typing import List, Dict

import numpy as np

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
        self.mode: str = mode
        self.players: List[Player] = self.init_players(players)
        self.turns_min: int = turns_min
        self.turns_max: int = turns_max
        self.payoff_matrix: np.ndarray = payoff_matrix
        self.error: float = error

    def init_players(self, players: Dict[str, int]) -> List[Player]:
        """
        Initialize the players. Call specific methods based on the mode.
        :param players: Dictionary of players as specified in the constructor
        :return: List of Players objects
        :raises: ValueError: if invalid mode of the simulation was given
        """
        if self.mode == 'round-robin':
            return self.init_players_round_robin(players)
        elif self.mode == 'evolution':
            return self.init_players_evolution(players)
        else:
            raise ValueError('Invalid mode of simulation')

    def init_players_round_robin(self, players: Dict[str, int]) -> List[Player]:
        """
        Initialize the players for the round-robin simulation
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
    def init_players_evolution(self, players: Dict[str, int]) -> List[Player]:
        """
        Initialize the players for the evolution simulation
        :param players: Dictionary of players as specified in the constructor
        :return: List of Players objects
        """
        player_list: List[Player] = []
        for player_type in players.items():
            name: str = player_type[0]
            player_list.append(Player(strategy.get_strategy(player_type[0]), name, player_type[1]))
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
        """
        Simulate an evolution tournament
        :return: Dictionary of standings - {player type, population size}
        """
        turn_limit = 50

        return standings

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

    def duel(self, player1: str, player2: str) -> (int, int):
        """
        Inside the simulation scope, duel two selected players and output the dilemma result.
        :param player1: Name of player 1
        :param player2: Name of player 2
        :return: score of player 1 and score of player 2
        """
        temp_mode = self.mode
        self.mode = 'round-robin'

        player_A = next((player for player in self.players if player.name == player1), None)
        player_B = next((player for player in self.players if player.name == player2), None)
        dilemma: Dilemma = Dilemma(self.payoff_matrix, self.turns_min, self.turns_max,
                                   self.error, player_A, player_B)
        result = dilemma.run(debug=True)

        self.mode = temp_mode
        return result

    def duel_all(self, player: str) -> None:
        """
        Inside the simulation scope, duel with each opponent as a selected player
        :param player: Name of the selected player
        """
        temp_mode = self.mode
        self.mode = 'round-robin'

        player_A = next((this_player for this_player in self.players if this_player.name == player), None)
        for opponent in self.players:
            if opponent == player:
                continue
            print("###")
            print(opponent.name)
            dilemma: Dilemma = Dilemma(self.payoff_matrix, self.turns_min, self.turns_max,
                                       self.error, player_A, opponent)
            print(dilemma.run(debug=True))
        self.mode = temp_mode



def simplest(error: float) -> None:
    """
    Simplest possible simulation
    """
    simulation: Simulation = Simulation({"always_cooperate": 20}, 10, 25, error)
    result = simulation.simulate()
    print(result)

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
        'retaliate_75': 1,
        'machine_learning': 1
    }
    suite(players, error, 10000)
    # simulation: Simulation = Simulation(players, 10, 25, error)
    # result = simulation.simulate()
    # print(result)
    # for i in range(len(players)):
    #     try:
    #         simulation.players[i].strategy(-1, -1, -1, None, None, None, 0, 0)  # Debug machine learning model
    #     except:
    #         pass


def suite(players: Dict[str, int], error: float, iterations: int) -> None:
    """
    Runs the simulation with preselected players and error rate for a given number of iterations.
    :param players: Dictionary of players
    :param error: Error chance
    :param iterations: Number of iterations
    """
    simulation: Simulation = Simulation(players, 10, 25, error)
    for i in range(iterations):
        result = simulation.simulate()
        print("\n")
        print("Run #" + str(i+1))
        print(result)
        if i != iterations - 1:
            for player in simulation.players:
                player.score = 0
    simulation.duel_all("machine_learning")
    # print("###")
    # print("always_defect")
    # print(simulation.duel("machine_learning", "always_defect"))
    # print("###")
    # print("tit_for_tat")
    # print(simulation.duel("machine_learning", "tit_for_tat"))
    # print("###")
    # print("grudger")
    # print(simulation.duel("machine_learning", "grudger"))
    # print("###")
    # print("simpleton")
    # print(simulation.duel("machine_learning", "simpleton"))
    # print("###")
    # print("retaliate_75")
    # print(simulation.duel("machine_learning", "retaliate_75"))


if __name__ == '__main__':
    exhaustive(0)
