def fromBinary(biNum: int) -> int: #Converts Binary to Decimal.
    decNum: int = 0
    lenBin = len(str(biNum))

    for i in range(lenBin):
        decNum += int(str(abs(biNum))[i]) * 2 ** (lenBin - 1 - i)
    return decNum

def fromOctal(octNum: int) -> int: #Converts Octal to Decimal.
    decNum: int = 0
    lenOct = len(str(octNum))

    for i in range(lenOct):
        decNum += int(str(abs(octNum))[i]) * 8 ** (lenOct - 1 - i)
    return decNum

def fromHex(hexNum: str) -> int: #Converts Hexadecimal to Decimal.
    decNum: int = 0
    letters = {"A" : 10,
               "B" : 11,
               "C" : 12,
               "D" : 13,
               "E" : 14,
               "F" : 15
               }
    for i in range(len(hexNum)):
        if hexNum[i] in letters:
            decNum += letters.get(hexNum[i]) * 16 ** (len(hexNum) - 1 - i)
        else:
            decNum += int(hexNum[i]) * 16 ** (len(hexNum) - 1 - i)
    return decNum
# Yo
# 1