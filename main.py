def fromBinary(biNum: str) -> float: #Converts Binary to Decimal.
    decNum: float = 0.0
    lenBin = len(str(biNum))

    if '.' in biNum:
        decimalPoint = biNum.find('.')
        intPart = biNum[:decimalPoint]
        fractionPart = biNum[decimalPoint + 1:]

        for i in range(len(intPart)):
            decNum += int(intPart[i]) * 2 ** (len(intPart) - 1 - i)

        for i in range(len(fractionPart)):
            decNum += int(fractionPart[i]) * (1 / (2 ** (i + 1)))

    else:
        for i in range(lenBin):
            decNum += int(biNum[i]) * 2 ** (lenBin - 1 - i)
    return decNum

def fromOctal(OcNum: str) -> float: #Converts Octal to Decimal.
    decNum: float = 0
    lenOct = len(str(OcNum))

    if '.' in OcNum:
        decimalPoint = OcNum.find('.')
        intPart = OcNum[:decimalPoint]
        fractionPart = OcNum[decimalPoint + 1:]

        for i in range(len(intPart)):
            decNum += int(intPart[i]) * 8 ** (len(intPart) - 1 - i)

        for i in range(len(fractionPart)):
            decNum += int(fractionPart[i]) * (1 / (8 ** (i + 1)))

    else:
        for i in range(lenOct):
            decNum += int(OcNum[i]) * 8 ** (lenOct - 1 - i)
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
