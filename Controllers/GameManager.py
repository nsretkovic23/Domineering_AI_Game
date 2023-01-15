from Controllers.ASCIIConverter import getASCIIFromNumberStartingAt0
from Controllers.GameState import GameState
from Controllers.TurnController import isHorizontalMoveValid, isVerticalMoveValid, playValidTurnInstantly
import copy

from Interface.StatePrinter import printCurrentState

def canXPlay(state:GameState):
    for colIndex in range(0, state.colDim):
        isFound = False
        # Don't check the last row
        # If dimension is 5 and  there is no space at 4th row
        # We don't care if there is at 5th because domino is placed downwards in state
        for rowIndex in range(0, state.rowDim - 1):
            if state.stateMatrix[rowIndex][colIndex] == " " and state.stateMatrix[rowIndex+1][colIndex] == " ":
                isFound = True
                break
        if isFound:
            break
    return isFound

def canOPlay(state:GameState):
    for rowIndex in range(0,state.rowDim):
        isFound = False
        # Don't check the last column
        # If dimension is 5 and  there is no space at 4th column
        # We don't care if there is at 5th because domino is placed from left-to right in state
        for colIndex in range(0, state.colDim - 1):
            if state.stateMatrix[rowIndex][colIndex] == " " and state.stateMatrix[rowIndex][colIndex + 1] == " ":
                isFound = True
                break
        if isFound:
            break
    return isFound

def isGameOver(state:GameState):
    if not canXPlay(state):
        return(True, "O")
    elif not canOPlay(state):
        return(True, "X")
    else:
        return (False, "")

def getAllPossibleMoves(state:GameState):
    listOfPossibleMoves = []

    for rowIndex in range(0,state.rowDim):
        for colIndex in range(0, state.colDim):
            if state.currentTurn == "X":
                if isVerticalMoveValid(state.stateMatrix, state.rowDim, (rowIndex, colIndex)):
                    listOfPossibleMoves.append([rowIndex, colIndex])
            elif state.currentTurn == "O":
                if isHorizontalMoveValid(state.stateMatrix, state.colDim, (rowIndex, colIndex)):
                    listOfPossibleMoves.append([rowIndex, colIndex])

    return listOfPossibleMoves

def getAllPossibleNextStates(currentState:GameState):
    possibleMoves = getAllPossibleMoves(state = currentState)
    possibleNextStates = []

    for i in range(0, len(possibleMoves)):
        nextState = playValidTurnInstantly(currentState, possibleMoves[i][0], possibleMoves[i][1])
        nextState.minMaxGeneratedTurns.append([possibleMoves[i][0], possibleMoves[i][1]])
        possibleNextStates.append(nextState)
    
    return possibleNextStates