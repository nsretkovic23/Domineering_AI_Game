import copy
from Controllers.GameManager import getAllPossibleMoves
from Controllers.GameState import GameState
from Controllers.MinMax.HeuristicHelpers import areThereTwoFreeFieldsAbove, areThereTwoFreeFieldsBelow, areThereTwoFreeFieldsLeft, areThereTwoFreeFieldsRight, isSafeTurn

def isSafeTurnEvaluation(state:GameState):
    if isSafeTurn(state):
        return 0
    return 5


# Determine if move is creating safe turn
# It does if either tile is played in second row/column, or second to last row/column or second row/column from any tile of the same type
def isCreatingSafeTurnsEvaluation(state:GameState):
    row = state.lastPlayedMove[0]
    col = state.lastPlayedMove[1]
    acc = 0
    # If current turn is O, this means that X played last move, so we analyze X's move
    if state.currentTurn == "O":
        if col == 1 or col == state.colDim - 2:
            acc += 7
        if areThereTwoFreeFieldsLeft(state):
            acc += 5
        if areThereTwoFreeFieldsRight(state):
            acc += 5
    elif state.currentTurn == "X":
        if row == 1 or row == state.rowDim - 2:
            acc += 7
        if areThereTwoFreeFieldsBelow(state):
            acc += 5
        if areThereTwoFreeFieldsAbove(state):
            acc += 5
    return acc

def isStoppingEnemyWallEvaluation(state:GameState):
    row = state.lastPlayedMove[0]
    col = state.lastPlayedMove[1]

    doubleMultiplier = 0
    # If current turn is O, this means that X played last move, so we analyze X's move
    if state.currentTurn == "O":
        for i in range(0, state.colDim):
            if state.stateMatrix[row][i] == "O":
                doubleMultiplier += 1
            if state.stateMatrix[row+1][i] == "O":
                doubleMultiplier += 1
            if doubleMultiplier == 2:
                break
    else:
        for i in range(0, state.rowDim):
            if state.stateMatrix[i][col] == "X":
                doubleMultiplier += 1
            if state.stateMatrix[i][col+1] == "X":
                doubleMultiplier += 1
            if doubleMultiplier == 2:
                break

    return 3 * doubleMultiplier

def evaluateState(state:GameState, whoPlayed=None, whoIsOpponent = None):
    score = 0
    multiplier = -1 if state.currentTurn == "X" else 1
    score = isStoppingEnemyWallEvaluation(state) + isCreatingSafeTurnsEvaluation(state) + isSafeTurnEvaluation(state)
    
    return score * multiplier