from Controllers.ASCIIConverter import getNumberFromASCII
from Controllers.GameState import GameState
from ImportedScripts.CMDTextColorizer.ColorizeText import colored
from Interface.StatePrinter import printCurrentState
import copy

# Position: tuple with first element being the row and second is column
def isHorizontalMoveValid(stateMatrix:list, colDim:int, position:tuple):
    row = position[0]
    col = position[1]

    if col < 0 or col >= colDim - 1:
        return False
    elif "X" in stateMatrix[row][col] or "X" in stateMatrix[row][col+1]:
        return False
    elif "O" in stateMatrix[row][col] or "O" in stateMatrix[row][col+1]:
        return False
    return True

# Position: tuple with first element being the row and second is column
def isVerticalMoveValid(stateMatrix:list, rowDim:int, position:tuple):
    row = position[0]
    col = position[1]

    if row < 0 or row >= rowDim - 1:
        return False
    elif "X" in stateMatrix[row][col] or "X" in stateMatrix[row + 1][col]:
        return False
    elif "O" in stateMatrix[row][col] or "O" in stateMatrix[row + 1][col]:
        return False
    return True

# min = min input value, max = max input value
def getValidIntInput(min:int, max:int, inputContext:str):
    inp = -1
    while(inp < min or inp > max):
        try:
            inp = int(input(colored(f"Enter {inputContext} position: ", 'yellow')))
        except:
            print(colored("Invalid input", 'red', attrs=['bold']))
    return inp - 1

# Expected input is character that gets converted to (int - 65)  
# min = min input value, max = max input value
def getValidCharToIntInput(min:int, max:int, inputContext:str):
    inp = -1
    while(inp < min or inp > max):
        try:
            asciiVal = input(colored(f"Enter {inputContext} position: ", 'yellow')).upper()
            inp = getNumberFromASCII(asciiVal)
        except:
            print(colored("Invalid input", 'red', attrs=['bold']))
    return inp

# Ova funkcija pokriva menjanje trenutnog stanja igre 
# I funkciju koja na osnovu zadatog poteza i zadatog stanja formira novo stanje igre
def playTurnWithInputs(state:GameState):
    rowInput = -1
    colInput = chr(0)

    print(colored(f'\n{state.currentTurn} Plays:', 'magenta', attrs=['bold']))

    newState = GameState()
    newState = copy.deepcopy(state)

    if newState.currentTurn == "X":
        while(True):
            # Send rowDim instead of rowDim-1 because row at the table that user sees starts from 1
            rowInput = getValidIntInput(0, newState.rowDim, "ROW (1,2,3)")
            colInput = getValidCharToIntInput(0, newState.colDim, "COLUMN (A,B,C)")

            if not isVerticalMoveValid(newState.stateMatrix, newState.rowDim, (rowInput, colInput)):
                print(colored("You can't place a domino here, try again!", 'red', attrs=['bold']))
            else:
                break

        newState.stateMatrix[rowInput][colInput] = "X"
        newState.stateMatrix[rowInput+1][colInput] = "X"
        newState.lastPlayedX = [rowInput, colInput]

    elif state.currentTurn == "O":
        while(True):
            # Send rowDim instead of rowDim-1 because row at the table that user sees starts from 1
            rowInput = getValidIntInput(0, newState.rowDim, "ROW (1,2,3)")
            colInput = getValidCharToIntInput(0, newState.colDim, "COLUMN (A,B,C)")

            if not isHorizontalMoveValid(newState.stateMatrix, newState.colDim, (rowInput, colInput)):
                print(colored("You can't place a domino here, try again!", 'red', attrs=['bold']))
            else:
                break

        newState.stateMatrix[rowInput][colInput] = "O"
        newState.stateMatrix[rowInput][colInput+1] = "O"
        newState.lastPlayedO = [rowInput, colInput]

    newState.currentTurn = "O" if newState.currentTurn == "X" else "X"
    newState.lastPlayedMove = [rowInput, colInput]

    return newState

# Only valid turns are passed as row and col arguments
def playValidTurnInstantly(state:GameState, row, col):
    newState = GameState()
    newState = copy.deepcopy(state)

    if newState.currentTurn == "X":
        newState.stateMatrix[row][col] = "X"
        newState.stateMatrix[row + 1][col] = "X"
        newState.lastPlayedX = [row, col]

    elif state.currentTurn == "O":
        newState.stateMatrix[row][col] = "O"
        newState.stateMatrix[row][col + 1] = "O"
        newState.lastPlayedO = [row, col]

    newState.currentTurn = "O" if newState.currentTurn == "X" else "X"
    newState.lastPlayedMove = [row, col]

    return newState

def undoLastTurn(state:GameState):
    if len(state.lastPlayedMove) == 0:
        return None

    earlierState = GameState()
    earlierState = copy.deepcopy(state)

    row = earlierState.lastPlayedMove[0]
    col = earlierState.lastPlayedMove[1]
    #" "
    if earlierState.stateMatrix[row][col] == "X":
        earlierState.stateMatrix[row][col] = " "
        earlierState.stateMatrix[row+1][col] = " "
    else:
        earlierState.stateMatrix[row][col] = " "
        earlierState.stateMatrix[row][col+1] = " "

    state.currentTurn == "X" if state.currentTurn == "O" else "O"
    
    return earlierState


    
        



    
    