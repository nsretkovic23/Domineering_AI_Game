from Controllers.GameManager import getAllPossibleNextStates
from Controllers.GameState import GameState

# For X, if there are free fields on row and row+1 : col-1 position 
def areThereTwoFreeFieldsLeft(state:GameState):
    row = state.lastPlayedMove[0]
    col = state.lastPlayedMove[1]
    # If X is not on the left edge, there could be free fields 
    if col > 0 and (state.stateMatrix[row][col-1] == " " and state.stateMatrix[row+1][col-1]):
        return True
    return False

def areThereTwoFreeFieldsRight(state:GameState):
    row = state.lastPlayedMove[0]
    col = state.lastPlayedMove[1]
    # If X is not on the right edge, there could be free fields 
    if col < state.colDim - 1 and (state.stateMatrix[row][col+1] == " " and state.stateMatrix[row+1][col+1]):
        return True
    return False

def areThereTwoFreeFieldsBelow(state:GameState):
    row = state.lastPlayedMove[0]
    col = state.lastPlayedMove[1]
    if row > 0 and (state.stateMatrix[row-1][col] == " " and state.stateMatrix[row-1][col+1]):
        return True
    return False

def areThereTwoFreeFieldsAbove(state:GameState):
    row = state.lastPlayedMove[0]
    col = state.lastPlayedMove[1]
    if row < state.rowDim - 1 and (state.stateMatrix[row+1][col] == " " and state.stateMatrix[row+1][col+1]):
        return True
    return False

def filterBestStates(state:GameState)-> list: 
    newStates = getAllPossibleNextStates(state)
    notSafeTurnAndAvoidedEdges = []
    notSafeTurnStates = []
    safeTurnStates = []

    for i in range(0,len(newStates)):
        if isSafeTurn(newStates[i]):
            safeTurnStates.append(newStates[i])
        else:
            if isEdgeAvoided(newStates[i]):
                notSafeTurnAndAvoidedEdges.append(newStates[i])
            else:
                notSafeTurnStates.append(newStates[i])

    if len(notSafeTurnAndAvoidedEdges) > 0:
        newStates = notSafeTurnAndAvoidedEdges
    elif len(notSafeTurnStates) > 0:
        newStates = notSafeTurnStates
    else:
        newStates = safeTurnStates
    
    return newStates

# Safe turn is a turn already "reserved" where only one player can play there
# For example safe turn for X are 2 vertical fields that O can not interrupt 
# Safe turns should be played last because they do not affect opponent in any way
# But current player should create more and more safe turns for himself through the game
def isSafeTurn(state:GameState):
    row = state.lastPlayedMove[0]
    col = state.lastPlayedMove[1]
    # If current turn is O, this means that X played last move, and we need to analyze X's move, so this is the X case
    if state.currentTurn == "O":
        # Domino-space to the left of the last played domino
        leftDomino = col-1
        #Domino-space to the right of the last played domino
        rightRomino = col+1
        # Case when X is played on the left edge of the table, doesn't mean that it's safe move because domino-space to the right decides it
        if leftDomino < 0 :
            if state.stateMatrix[row][rightRomino] == " " or state.stateMatrix[row+1][rightRomino] == " ":
                return False
        # Case when X is played on the right edge
        elif rightRomino >= state.colDim :
            if state.stateMatrix[row][leftDomino] == " " or state.stateMatrix[row+1][leftDomino] == " ":
                return False
        #Case when X is played somewhere on the board
        else:
            if state.stateMatrix[row][leftDomino] == " " or state.stateMatrix[row+1][leftDomino] == " " or state.stateMatrix[row][rightRomino] == " " or state.stateMatrix[row+1][rightRomino] == " ":
                return False
    # If current turn is X, this means that O played last move, and we need to analyze O's move, so this is the O case
    elif state.currentTurn == "X":
        # Domino-space above last played domino
        upDomino = row+1
        #Domino-space below last played domino
        downDomino = row-1
        # Case when O is played on bottom edge
        if downDomino < 0:
            if state.stateMatrix[upDomino][col] == " " or state.stateMatrix[upDomino][col+1] == " ":
                return False
        # Case when O is played on top edge
        elif upDomino >= state.rowDim:
            if state.stateMatrix[downDomino][col] == " " or state.stateMatrix[downDomino][col+1] == " ":
                return False
        # O placed somewhere on the board
        else:
            if state.stateMatrix[upDomino][col] == " " or state.stateMatrix[upDomino][col+1] == " " or state.stateMatrix[downDomino][col] == " " or state.stateMatrix[downDomino][col+1] == " ":
                return False
    
    #print(f"Je li safe? {isSafe}")
    return True

# If current turn is X we should check for O, and vice versa
def isEdgeAvoided(state:GameState):
    multiplier = -1 if state.currentTurn == "X" else 1
    #multiplier = 0.1 if state.currentTurn == "X" else 1
    
    isEdgeAvoided = True
    row = state.lastPlayedMove[0]
    col = state.lastPlayedMove[1]
    # O
    if multiplier == -1 and (row == state.rowDim-1 or row == 0):
        isEdgeAvoided = False
    #X
    elif multiplier == 1 and (col == state.colDim-1 or col == 0):
        isEdgeAvoided = False

    return isEdgeAvoided