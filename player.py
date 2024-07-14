class Player:

    def __init__(self, strategy, name: str):
        self.strategy = strategy
        self.score: int = 0
        self.name: str = name
