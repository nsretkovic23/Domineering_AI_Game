from Controllers.GameManager import isGameOver
from Controllers.TurnController import playTurn
from ImportedScripts.CMDTextColorizer.ColorizeText import colored
from Interface.StatePrinter import printCurrentState, clearConsole
from Controllers.GameState import GameState
from Interface.GameInitializer import intializeGame

clearConsole()

# Klasican tok igre
state:GameState = intializeGame(15,15)

isGameFinished = False

printCurrentState(state)

while not isGameFinished:
    playTurn(state)
    isGameFinished = isGameOver(state)[0]
    printCurrentState(state)

print(colored(f"GAME OVER! The winner is {isGameOver(state)[1]}", "green" ,attrs=["bold"]))


# Testiranje stampanja proizvoljnog stanja igre

#state:GameState = GameState
# 5 x 6 test matrix
#playingFields = [[" ", " ", " ", " ", " ", " "],
#                 [" ", " ", " ", " ", " ", " "],
#                 [" ", " ", "O", "O", " ", " "],
#                 [" ", "X", " ", " ", " ", " "],
#                 [" ", "X", " ", " ", " ", " "],]
#
#
#state.stateMatrix = playingFields
#state.rowDim = len(playingFields)
#state.colDim = len(playingFields[0])
#state.currentTurn = "X"
#printCurrentState(state)


