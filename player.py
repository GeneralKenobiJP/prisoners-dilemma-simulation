class Player:
    """
    Player class
    """
    def __init__(self, strategy, name: str, score: int = 0):
        """
        Constructor for the player class
        :param strategy: Function pointer to the strategy function.
            Takes as input:
                turn: int, turns_min: int, turns_max: int, own_history: List[bool],
                opponent_history: List[bool], own_score: int, opponent_score: int
            Outputs:
                boolean decision (true - cooperate, false - deflect)
        :param name: Unique name, constructed as <strategy_name> + #num (for #1, the #1 is omitted)
        :param score: Starting score of the player. Usually 0. Starting population size for the evolution simulation
        """
        self.strategy = strategy
        self.score: int = score  # For the evolution simulation - population size
        self.name: str = name
