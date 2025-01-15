import time

def check(number: str, numeralType: str) -> bool:  # Checks the validity of a binary, octal, or hex number
    validNums = []

    if numeralType.lower() == "binary": # then
        validNums = ["0", "1", "."]
    elif numeralType.lower() == "octal":
        validNums = ["0", "1", "2", "3", "4", "5", "6", "7", "."]
    elif numeralType.lower() == "hex" or numeralType.lower() == "hexadecimal":
        validNums = ["0", "1", "2", "3", "4", "5", "6", "7",
                     "8", "9", "A", "B", "C", "D", "E", "F", "."]
    number = number.upper()

    for i in number:
        if i not in validNums:
            return False
    return True

def fromBinaryToDecimal(biNum: str) -> float:  # Converts Binary to Decimal.
    if check(biNum, "Binary"):
        decNum: float = 0
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
    else:
        print("Try a valid Binary Number")
        return -1

def fromOctalToDecimal(OcNum: str) -> float:  # Converts Octal to Decimal.
    if check(OcNum, "Octal"):
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
    else:
        print("Try a valid Octal number.")
        return -1

def fromHexToDecimal(hexNum: str) -> int:  # Converts Hexadecimal to Decimal.
    if check(hexNum, "Hex"):
        hexNum = hexNum.upper()
        decNum: int = 0
        letters = {"A": 10,
                   "B": 11,
                   "C": 12,
                   "D": 13,
                   "E": 14,
                   "F": 15
                   }
        for i in range(len(hexNum)):
            if hexNum[i] in letters:
                decNum += letters.get(hexNum[i]) * 16 ** (len(hexNum) - 1 - i)
            else:
                decNum += int(hexNum[i]) * 16 ** (len(hexNum) - 1 - i)
        return decNum
    else:
        print("Try a valid Hex number.")
        return -1

def run() -> None: # Allows the user to pick what Numeral System will be converted and input a number to be converted
    toBeConverted: str = input("What Numeral System would you like to convert to Decimal? ")

    match toBeConverted.lower():

        case "binary":
            num: str = input("Input the Binary number: ")
            convertedNum = fromBinaryToDecimal(num)
            if convertedNum != -1:
                print(f'{num} in Binary is {convertedNum} in Decimal.')

        case "octal":
            num: str = input("Input the Octal number: ")
            convertedNum = fromOctalToDecimal(num)
            if convertedNum != -1:
                print(f'{num} in Octal is {convertedNum} in Decimal.')

        case "hex":
            num: str = input("Input the Hexadecimal number: ")
            convertedNum = fromHexToDecimal(num)
            if convertedNum != -1:
                print(f'{num} in Hexadecimal is {convertedNum} in Decimal.')

        case "hexadecimal":
            num: str = input("Input the Hexadecimal number: ")
            convertedNum = fromHexToDecimal(num)
            if convertedNum != -1:
                print(f'{num} in Hexadecimal is {convertedNum} in Decimal.')

        case _:
            print("Invalid Numeral System Try Agian.\n")
            time.sleep(.5)
            run()

if __name__ == '__main__':
   run()
