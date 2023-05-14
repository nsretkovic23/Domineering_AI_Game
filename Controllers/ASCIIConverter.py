# A start at 0
def getASCIIFromNumberStartingAt0(num):
    if num + 65 < 65:
        return chr(65)
    elif num+65 > 90:
        return chr(90)
    else:
        return chr(num+65)

def getNumberFromASCII(asciiChar):
    num = ord(asciiChar) - 65
    return num if num >= 0 else -1
