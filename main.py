from Controllers.GameManager import getAllPossibleMoves, getAllPossibleNextStates, isGameOver
from Controllers.TurnController import playTurnWithInputs
from ImportedScripts.CMDTextColorizer.ColorizeText import colored
from Interface.StatePrinter import printAllPossibleMoves, printAllPossibleNextStates, printCurrentState, clearConsole
from Controllers.GameState import GameState
from Interface.GameInitializer import intializeGame

clearConsole()

# Klasican tok igre
state:GameState = intializeGame(15,15)

isGameFinished = False

printCurrentState(state)

while not isGameFinished:
    # Otkomentarisati za prikaz liste koji su naredni moguci potezi
    #print(colored("Possible valid moves:","grey"))
    #printAllPossibleMoves(getAllPossibleMoves(state))

    # Otkomentarisati za graficki prikaz svih stanja koja su dobijena od svih narednih mogucih poteza
    #print(colored("Possible next states:","grey"))
    #printAllPossibleNextStates(getAllPossibleNextStates(state))

    state = playTurnWithInputs(state)
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
