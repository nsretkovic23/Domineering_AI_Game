from ImportedScripts.CMDTextColorizer.ColorizeText import colored
from Interface.StatePrinter import printCurrentState, clearConsole
from Controllers.GameState import GameState
from Interface.GameInitializer import intializeGame

clearConsole()

state:GameState = intializeGame(15,15)

# Test matrix
# 5 x 6 test matrix
#playingFields = [[" ", " ", " ", " ", " ", " "],
#                 [" ", " ", " ", " ", " ", " "],
#                 [" ", " ", "O", "O", " ", " "],
#                 [" ", "X", " ", " ", " ", " "],
#                 [" ", "X", " ", " ", " ", " "],]


printCurrentState(state)

state.stateMatrix[5][5] = "X"
state.stateMatrix[3][3] = "O"

printCurrentState(state)


