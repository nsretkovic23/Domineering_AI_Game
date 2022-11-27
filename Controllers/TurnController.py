from Controllers.ASCIIConverter import getNumberFromASCII
from Controllers.GameState import GameState
from ImportedScripts.CMDTextColorizer.ColorizeText import colored
from Interface.StatePrinter import printCurrentState

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

def playTurn(state:GameState):
    rowInput = -1
    colInput = chr(0)

    print(colored(f'\n{state.currentTurn} Plays:', 'magenta', attrs=['bold']))

    if state.currentTurn == "X":
        while(True):
            # Send rowDim instead of rowDim-1 because row at the table that user sees starts from 1
            rowInput = getValidIntInput(0, state.rowDim, "ROW (1,2,3)")
            colInput = getValidCharToIntInput(0, state.colDim, "COLUMN (A,B,C)")

            if not isVerticalMoveValid(state.stateMatrix, state.rowDim, (rowInput, colInput)):
                print(colored("You can't place a domino here, try again!", 'red', attrs=['bold']))
            else:
                break

        state.stateMatrix[rowInput][colInput] = "X"
        state.stateMatrix[rowInput+1][colInput] = "X"

    elif state.currentTurn == "O":
        while(True):
            # Send rowDim instead of rowDim-1 because row at the table that user sees starts from 1
            rowInput = getValidIntInput(0, state.rowDim, "ROW (1,2,3)")
            colInput = getValidCharToIntInput(0, state.colDim, "COLUMN (A,B,C)")

            if not isHorizontalMoveValid(state.stateMatrix, state.colDim, (rowInput, colInput)):
                print(colored("You can't place a domino here, try again!", 'red', attrs=['bold']))
            else:
                break

        state.stateMatrix[rowInput][colInput] = "O"
        state.stateMatrix[rowInput][colInput+1] = "O"

    state.currentTurn = "O" if state.currentTurn == "X" else "X" 
    
        



    
    