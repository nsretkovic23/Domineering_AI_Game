from ImportedScripts.CMDTextColorizer.ColorizeText import colored
from Interface.StatePrinter import printCurrentState, clearConsole
from Controllers.GameState import GameState

clearConsole()

# Test matrix
# 5 x 6 test matrix
playingFields = [[" ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " "],
                 [" ", " ", "O", "O", " ", " "],
                 [" ", "X", " ", " ", " ", " "],
                 [" ", "X", " ", " ", " ", " "],]

state = GameState()
state.rowDim = 5
state.colDim = 6
state.stateMatrix = playingFields

printCurrentState(state)


