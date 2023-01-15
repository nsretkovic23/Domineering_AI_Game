class GameState:
    def __init__(self) -> None:
        self.playerSign = ""
        self.cpuSign = ""
        self.currentTurn = ""
        self.rowDim = 0
        self.colDim = 0
        self.stateMatrix = []
        self.lastPlayedMove = []
        # Keeps track of all played turns when state is being analyzed through minimax algorithm
        # Almost always most important is the first element, because the state returned from minimax
        # Contains best move, which is the first one, other ones(if any) are appended because of the dept analysis 
        self.minMaxGeneratedTurns = []
        self.lastPlayedX = []
        self.lastPlayedO = []
