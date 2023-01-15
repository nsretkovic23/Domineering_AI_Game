from Controllers.ASCIIConverter import getASCIIFromNumberStartingAt0
from Controllers.GameManager import getAllPossibleMoves, getAllPossibleNextStates, isGameOver
from Controllers.MinMax.MinMax import minimax
from Controllers.TurnController import playTurnWithInputs, playValidTurnInstantly, undoLastTurn
from ImportedScripts.CMDTextColorizer.ColorizeText import colored
from Interface.StatePrinter import printAllPossibleMoves, printAllPossibleNextStates, printCurrentState, clearConsole
from Controllers.GameState import GameState
from Interface.GameInitializer import getWhoPlaysFirst, intializeGame

clearConsole()

state:GameState = intializeGame(15,15)
isGameFinished = False
printCurrentState(state)

while not isGameFinished:
    isGameFinished = isGameOver(state)[0]

    if state.currentTurn == "X":
        if state.playerSign == "X":
            state = playTurnWithInputs(state)
        else:
            minMaxState = minimax(state, 1)
            state = playValidTurnInstantly(state, minMaxState[0].minMaxGeneratedTurns[0][0], minMaxState[0].minMaxGeneratedTurns[0][1])
    else:
        if state.playerSign == "O":
            state = playTurnWithInputs(state)
        else:
            minMaxState = minimax(state, 1)
            state = playValidTurnInstantly(state, minMaxState[0].minMaxGeneratedTurns[0][0], minMaxState[0].minMaxGeneratedTurns[0][1])
    printCurrentState(state)


print(colored(f"GAME OVER! The winner is {isGameOver(state)[1]}", "green" if isGameOver(state)[1]=="X" else "red", attrs=["bold"]))

