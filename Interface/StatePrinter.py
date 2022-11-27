import os
from Controllers.GameState import GameState
from ImportedScripts.CMDTextColorizer.ColorizeText import colored
from Controllers.ASCIIConverter import getASCIIFromNumberStartingAt0

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def getSingleStateRowString(list:list, rowIndex:int):
    size = len(list[rowIndex])
    rowStr = ""
    for i in range(0, size):
        if i ==0:
            rowStr += " " if (rowIndex + 1) < 10 else ""
            rowStr+= str(rowIndex + 1) + colored("\u01c1","yellow")
            rowStr += " " + colored(list[rowIndex][i], "green" if list[rowIndex][i] == "X" else "magenta") + " |"
        elif i == size - 1:
            #rowStr += colored("   \u01c1","yellow")
            rowStr += " " + colored(list[rowIndex][i], "green" if list[rowIndex][i] == "X" else "magenta")  + colored(" \u01c1", "yellow")
        else:
            rowStr += " " + colored(list[rowIndex][i], "green" if list[rowIndex][i] == "X" else "magenta") + " |"
    return rowStr

def getDashRowSeparatorString(rowSize):
    str = ""
    for i in range(0, rowSize):
        str += "   --- " if i == 0 else "--- "
    return str

def getHorizontalEqualsRowSeparatorString(rowSize):
    str = ""
    for i in range(0, rowSize):
        str += colored("   === ", "yellow") if i == 0 else colored("=== ", "yellow")
    return str

def getColumnLettersString(rowSize):
    str = ""
    for i in range(0, rowSize):
        str += f'    {getASCIIFromNumberStartingAt0(i)} ' if i == 0 else f'  {getASCIIFromNumberStartingAt0(i)} '
    return str

def printCurrentState(state:GameState) -> None:
    print(getColumnLettersString(state.colDim))
    for i in range(state.rowDim-1, -1, -1):
        print(getHorizontalEqualsRowSeparatorString(state.colDim)) if i == state.rowDim-1 else print(getDashRowSeparatorString(state.colDim))
        print(getSingleStateRowString(state.stateMatrix, i))

    print(getHorizontalEqualsRowSeparatorString(state.colDim))